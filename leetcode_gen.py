#!/usr/bin/env python3

import os
import re
import sys
import json
import requests
from typing import Dict, List, Optional, Any

class LeetCodeGraphQLGenerator:
    def __init__(self, base_dir=os.path.join(os.path.realpath(os.path.dirname(__file__)), 'src')):
        self.base_dir = base_dir
        self.graphql_url = "https://leetcode.com/graphql/"
        self.session = requests.Session()
        
        # Set headers to mimic browser requests
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://leetcode.com/'
        })
    
    def search_problems(self, search_term: str) -> List[Dict[str, Any]]:
        """Search for problems by title or number"""
        query = """
        query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
            problemsetQuestionList: questionList(
                categorySlug: $categorySlug
                limit: $limit
                skip: $skip
                filters: $filters
            ) {
                total: totalNum
                questions: data {
                    acRate
                    difficulty
                    frontendQuestionId: questionFrontendId
                    title
                    titleSlug
                    paidOnly: isPaidOnly
                    topicTags {
                        name
                        slug
                    }
                }
            }
        }
        """
        
        variables = {
            "categorySlug": "",
            "skip": 0,
            "limit": 50,
            "filters": {}
        }
        
        # If search term is numeric, search by problem number
        if search_term.isdigit():
            variables["filters"] = {"searchKeywords": search_term}
        else:
            # Search by title keywords
            variables["filters"] = {"searchKeywords": search_term}
        
        try:
            response = self.session.post(
                self.graphql_url,
                json={"query": query, "variables": variables},
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            if "data" in data and "problemsetQuestionList" in data["data"]:
                return data["data"]["problemsetQuestionList"]["questions"]
            else:
                print(f"No data found. Response: {data}")
                return []
                
        except Exception as e:
            print(f"Error searching problems: {e}")
            return []
    
    def get_problem_details(self, title_slug: str) -> Optional[Dict[str, Any]]:
        """Get detailed problem information including content and examples"""
        # First try the simpler query
        query = """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                titleSlug
                content
                difficulty
                topicTags {
                    name
                    slug
                }
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                sampleTestCase
                exampleTestcases
            }
        }
        """
        
        variables = {"titleSlug": title_slug}
        
        try:
            response = self.session.post(
                self.graphql_url,
                json={"query": query, "variables": variables},
                timeout=10
            )
            
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 400:
                # Try alternative query structure
                return self._try_alternative_query(title_slug)
            
            response.raise_for_status()
            
            data = response.json()
            if "data" in data and "question" in data["data"] and data["data"]["question"]:
                return data["data"]["question"]
            else:
                print(f"No question data found. Response: {data}")
                return self._try_alternative_query(title_slug)
                
        except Exception as e:
            print(f"Error fetching problem details: {e}")
            return self._try_alternative_query(title_slug)
    
    def _try_alternative_query(self, title_slug: str) -> Optional[Dict[str, Any]]:
        """Try alternative GraphQL query structure"""
        # Minimal query that should work
        query = """
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionFrontendId
                title
                difficulty
                content
                codeSnippets {
                    lang
                    code
                }
            }
        }
        """
        
        try:
            response = self.session.post(
                self.graphql_url,
                json={"query": query, "variables": {"titleSlug": title_slug}},
                timeout=10
            )
            
            if response.status_code != 200:
                print(f"Alternative query also failed with status: {response.status_code}")
                print(f"Response: {response.text[:500]}")
                return None
            
            data = response.json()
            if "data" in data and "question" in data["data"] and data["data"]["question"]:
                return data["data"]["question"]
            else:
                print(f"Alternative query returned no data: {data}")
                return None
                
        except Exception as e:
            print(f"Alternative query error: {e}")
            return None
    
    def extract_examples_from_content(self, content: str) -> List[Dict[str, Any]]:
        """Extract examples from problem content HTML"""
        examples = []
        
        # Remove HTML tags and decode entities more thoroughly
        import re
        import html
        
        # First decode HTML entities
        clean_content = html.unescape(content)
        
        # Remove HTML tags
        clean_content = re.sub(r'<[^>]+>', ' ', clean_content)
        
        # Additional entity decoding
        clean_content = clean_content.replace('&nbsp;', ' ')
        clean_content = clean_content.replace('&lt;', '<')
        clean_content = clean_content.replace('&gt;', '>')
        clean_content = clean_content.replace('&amp;', '&')
        clean_content = clean_content.replace('&quot;', '"')
        clean_content = clean_content.replace('&#39;', "'")
        
        # Look for example patterns
        example_pattern = r'Example\s+\d+:\s*Input:\s*([^\n]+?)(?:\s*Output:\s*([^\n]+?))?(?=Example\s+\d+:|$)'
        matches = re.findall(example_pattern, clean_content, re.DOTALL | re.IGNORECASE)
        
        for match in matches:
            input_str, output_str = match
            input_str = input_str.strip()
            output_str = output_str.strip() if output_str else ""
            
            if input_str:
                example = {
                    'input': self._parse_example_value(input_str),
                    'solution': self._parse_example_value(output_str) if output_str else 'TODO: Add expected output'
                }
                examples.append(example)
        
        # If no examples found, try alternative patterns
        if not examples:
            # Try to find Input: and Output: pairs
            input_output_pattern = r'Input:\s*([^\n]+)\s*Output:\s*([^\n]+)'
            matches = re.findall(input_output_pattern, clean_content, re.IGNORECASE)
            
            for match in matches:
                input_str, output_str = match
                example = {
                    'input': self._parse_example_value(input_str.strip()),
                    'solution': self._parse_example_value(output_str.strip())
                }
                examples.append(example)
        
        return examples[:3]  # Limit to first 3 examples
    
    def _parse_example_value(self, value_str: str) -> Any:
        """Parse example value string into appropriate Python type"""
        import html
        
        # Decode HTML entities first
        value_str = html.unescape(value_str.strip())
        
        # Remove common prefixes
        value_str = re.sub(r'^(Input:|Output:|Example\s+\d+:)', '', value_str, flags=re.IGNORECASE).strip()
        
        # Remove surrounding quotes if present
        if value_str.startswith('"') and value_str.endswith('"'):
            value_str = value_str[1:-1]
        elif value_str.startswith("'") and value_str.endswith("'"):
            value_str = value_str[1:-1]
        
        # Handle special cases
        # if '=' in value_str:
        #     # create a dictionary-like structure
        #     parts = value_str.split(',')
        #     result = {}
        #     for part in parts:
        #         key, val = part.split('=', 1)
        #         result[key.strip()] = self._parse_example_value(val.strip())
        #     return result

        # Handle LeetCode format like "letters = ["c","f","j"], target = "a""
        if '=' in value_str and any(keyword in value_str.lower() for keyword in ['letters', 'target', 'nums', 'arr']):
            # Try to extract just the parameter values
            # For now, return the cleaned string - user can manually parse
            return value_str
        
        # Try to parse as Python literal
        try:
            # Handle common LeetCode formats
            if value_str.startswith('[') and value_str.endswith(']'):
                return eval(value_str)
            elif value_str.startswith('"') and value_str.endswith('"'):
                return value_str[1:-1]  # Remove quotes
            elif value_str.isdigit() or (value_str.startswith('-') and value_str[1:].isdigit()):
                return int(value_str)
            elif value_str.replace('.', '').replace('-', '').isdigit():
                return float(value_str)
            elif value_str.lower() in ['true', 'false']:
                return value_str.lower() == 'true'
            else:
                return value_str
        except:
            return value_str
    
    def extract_python_code_template(self, code_snippets: List[Dict[str, Any]]) -> Dict[str, str]:
        """Extract Python function template from code snippets"""
        python_code = None
        function_name = "solution"
        
        # Find Python code snippet
        for snippet in code_snippets:
            if snippet.get("langSlug") == "python3" or snippet.get("langSlug") == "python":
                python_code = snippet.get("code", "")
                break
        
        if python_code:
            # Extract function name
            func_match = re.search(r'def\s+(\w+)\s*\(', python_code)
            if func_match:
                function_name = func_match.group(1)
            
            # Clean up the code template and fix indentation
            lines = python_code.split('\n')
            cleaned_lines = []
            
            for line in lines:
                if line.strip():  # Skip empty lines for now
                    # Ensure proper indentation (4 spaces)
                    if line.startswith('class '):
                        # Remove class line - we'll add our own
                        continue
                    elif line.strip().startswith('def '):
                        # Function definition gets 4 spaces
                        cleaned_line = '    ' + line.strip()
                        cleaned_lines.append(cleaned_line)
                    elif line.strip().startswith('"""') or line.strip().startswith('"""'):
                        # Docstring gets 8 spaces
                        cleaned_line = '        ' + line.strip()
                        cleaned_lines.append(cleaned_line)
                    elif line.strip().startswith(':') or '"""' in line:
                        # Continuation of docstring
                        cleaned_line = '        ' + line.strip()
                        cleaned_lines.append(cleaned_line)
                    else:
                        # Function body gets 8 spaces
                        cleaned_line = '        ' + line.strip()
                        cleaned_lines.append(cleaned_line)
                else:
                    cleaned_lines.append('')  # Keep empty lines
            
            # Join lines back together
            python_code = '\n'.join(cleaned_lines)
            
            return {
                'function_name': function_name,
                'code_template': python_code
            }
        
        return {
            'function_name': function_name,
            'code_template': f'    def {function_name}(self):\n        pass'
        }
    
    def get_difficulty_dir(self, difficulty: str) -> str:
        """Map difficulty to directory name"""
        difficulty_map = {
            'Easy': 'lc_easy',
            'Medium': 'lc_medium',
            'Hard': 'lc_hard'
        }
        return difficulty_map.get(difficulty, 'medium')
    
    def create_file_structure(self, problem_data: Dict[str, Any]) -> str:
        """Create directory structure and return file path"""
        difficulty_dir = self.get_difficulty_dir(problem_data['difficulty'])
        
        # Create directory
        dir_path = os.path.join(self.base_dir, difficulty_dir)
        os.makedirs(dir_path, exist_ok=True)
        
        # Create filename
        problem_id = problem_data['questionFrontendId']
        title_slug = problem_data['titleSlug']
        filename = f"{problem_id}_{title_slug}.py"
        
        return os.path.join(dir_path, filename)
    
    def generate_template(self, problem_data: Dict[str, Any], code_info: Dict[str, str], examples: List[Dict[str, Any]]) -> str:
        """Generate the complete Python template"""
        problem_url = f"https://leetcode.com/problems/{problem_data['titleSlug']}/"
        
        template = f"# {problem_url}\n"
        template += f"class Solution:\n"
        
        # Add the function template (should already be properly indented)
        code_template = code_info['code_template']
        template += code_template + '\n\n'
        
        # Add test cases
        template += "cases = ["
        
        for i, example in enumerate(examples):
            template += f"\n    {{\n        'input': {repr(example['input'])},\n        'solution': {repr(example['solution'])}\n    }}"
            if i < len(examples) - 1:
                template += ","
        
        template += f"\n]\n\n"
        template += f"from tests import TestSuite\n"
        template += f"test_suite = TestSuite(\n"
        template += f"    **{{\n"
        template += f"        'testcases': cases,\n"
        template += f"        'func': Solution().{code_info['function_name']}\n"
        template += f"    }}\n"
        template += f")\n"
        template += f"test_suite.run_tests()"
        
        return template
    
    def interactive_problem_selection(self, problems: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Let user select from multiple matching problems"""
        if not problems:
            print("No problems found.")
            return None
        
        if len(problems) == 1:
            return problems[0]
        
        print(f"\nFound {len(problems)} matching problems:")
        print("-" * 80)
        
        for i, problem in enumerate(problems, 1):
            difficulty_color = {
                'Easy': '🟢',
                'Medium': '🟡', 
                'Hard': '🔴'
            }.get(problem['difficulty'], '⚪')
            
            paid_indicator = '💰' if problem.get('paidOnly', False) else ''
            
            print(f"{i:2d}. #{problem['frontendQuestionId']:4s} - {problem['title']}")
            print(f"     {difficulty_color} {problem['difficulty']} {paid_indicator}")
            print(f"     Slug: {problem['titleSlug']}")
            print()
        
        while True:
            try:
                choice = input(f"Select problem (1-{len(problems)}) or 'q' to quit: ").strip()
                if choice.lower() == 'q':
                    return None
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(problems):
                    return problems[choice_num - 1]
                else:
                    print(f"Please enter a number between 1 and {len(problems)}")
                    
            except ValueError:
                print("Please enter a valid number or 'q' to quit")
    
    def create_fallback_template(self, problem_info: Dict[str, Any]) -> str:
        """Create a basic template when detailed info isn't available"""
        problem_url = f"https://leetcode.com/problems/{problem_info['titleSlug']}/"
        
        template = f"# {problem_url}\n"
        template += f"class Solution:\n"
        template += f"    def solution(self):\n"
        template += f"        # TODO: Implement solution for {problem_info['title']}\n"
        template += f"        pass\n\n"
        
        template += "cases = [\n"
        template += "    {\n"
        template += "        'input': 'TODO: Add input from problem description',\n"
        template += "        'solution': 'TODO: Add expected output'\n"
        template += "    }\n"
        template += "]\n\n"
        
        template += "from tests import TestSuite\n"
        template += "test_suite = TestSuite(\n"
        template += "    **{\n"
        template += "        'testcases': cases,\n"
        template += "        'func': Solution().solution\n"
        template += "    }\n"
        template += ")\n"
        template += "test_suite.run_tests()"
        
        return template
    
    def process_problem(self, search_term: str):
        """Main function to process a problem"""
        print(f"Searching for: {search_term}")
        
        # Search for problems
        problems = self.search_problems(search_term)
        
        if not problems:
            print("No problems found. Try a different search term.")
            return
        
        # Let user select if multiple matches
        selected_problem = self.interactive_problem_selection(problems)
        if not selected_problem:
            return
        
        print(f"\nFetching details for: #{selected_problem['frontendQuestionId']} - {selected_problem['title']}")
        
        # Get detailed problem information
        problem_details = self.get_problem_details(selected_problem['titleSlug'])
        if not problem_details:
            print("Failed to fetch problem details")
            return
        
        # Extract examples from content
        examples = self.extract_examples_from_content(problem_details.get('content', ''))
        if not examples:
            examples = [{
                'input': 'TODO: Add input from problem description',
                'solution': 'TODO: Add expected output'
            }]
        
        # Extract Python code template
        code_info = self.extract_python_code_template(problem_details.get('codeSnippets', []))
        
        # Create file
        filepath = self.create_file_structure(problem_details)
        
        # Check if file exists
        if os.path.exists(filepath):
            response = input(f"File {filepath} already exists. Overwrite? (y/N): ")
            if response.lower() != 'y':
                print("Aborted.")
                return
        
        # Generate and write template
        template = self.generate_template(problem_details, code_info, examples)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(template)
        
        print(f"\n✅ Created: {filepath}")
        print(f"📊 Difficulty: {problem_details['difficulty']}")
        print(f"📝 Function: {code_info['function_name']}")
        print(f"🧪 Test cases: {len(examples)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python leetcode_graphql_generator.py <problem_number_or_title>")
        print("\nExamples:")
        print("  python leetcode_graphql_generator.py 744")
        print("  python leetcode_graphql_generator.py \"find smallest letter\"")
        print("  python leetcode_graphql_generator.py \"two sum\"")
        sys.exit(1)
    
    search_term = " ".join(sys.argv[1:])
    
    generator = LeetCodeGraphQLGenerator()
    try:
        generator.process_problem(search_term)
    except KeyboardInterrupt:
        print("\n\nAborted by user")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
