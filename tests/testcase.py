import inspect
from typing import Any, Optional, Union, Dict, List, Tuple
from dataclasses import dataclass
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored output
init()

class TestCaseInputError(Exception):
    pass

class TestCaseSolutionError(Exception):
    pass

@dataclass
class TestResult:
    passed: bool
    input_value: Any
    expected: Any
    received: Any
    index: int
    error: Optional[Exception] = None

class Response:
    def __init__(self, **kwargs):
        self.index = kwargs.get('index')
        self.input = kwargs.get('input')
        self.expected = kwargs.get('expected')
        self.received = kwargs.get('received')
        self.error = kwargs.get('error')

    def _format_value(self, value: Any) -> str:
        if isinstance(value, (list, tuple, set)):
            return f"{type(value).__name__}({value})"
        return str(value)

    def explain(self) -> None:
        print(f"\nTest Case {self.index}:")
        print(f"Input:    {self._format_value(self.input)}")
        print(f"Expected: {self._format_value(self.expected)}")
        print(f"Received: {self._format_value(self.received)}")
        if self.error:
            print(f"Error: {str(self.error)}")

    def disclose(self) -> None:
        raise NotImplementedError("Subclasses must implement disclose()")

class Success(Response):
    def disclose(self) -> None:
        print(f"{Fore.GREEN}✓ PASSED{Style.RESET_ALL}")

class Failure(Response):
    def disclose(self) -> None:
        print(f"{Fore.RED}✗ FAILED{Style.RESET_ALL}")

class TestCase:
    def __init__(self, **kwargs):
        self.index: int = kwargs.get('index', 0)
        self.input: Any = kwargs.get('input')
        self.func: callable = kwargs.get('func', lambda x: x)
        self.solution: Any = kwargs.get('solution')
        self.validate_input()

    def validate_input(self) -> None:
        if self.input is None:
            raise TestCaseInputError(f"Test case {self.index}: Input must be provided")
        if self.solution is None:
            raise TestCaseSolutionError(f"Test case {self.index}: Solution must be provided")

    def determine_call_method(self) -> Tuple[str, Any]:
        """
        Determines how to call the function based on its signature and the input type.
        Returns a tuple of (method, processed_input) where method is one of:
        - 'as_is': Pass input as is
        - 'args': Unpack as positional arguments
        - 'kwargs': Unpack as keyword arguments
        """
        try:
            sig = inspect.signature(self.func)
            params = sig.parameters

            # If input is not a collection type, always pass as is
            if not isinstance(self.input, (list, tuple, dict)):
                return 'as_is', self.input

            # For dictionaries, check if keys match parameter names
            if isinstance(self.input, dict):
                param_names = set(params.keys())
                input_keys = set(self.input.keys())
                if input_keys.issubset(param_names):
                    return 'kwargs', self.input
                return 'as_is', self.input

            # For lists/tuples, check if the length matches required positional arguments
            if isinstance(self.input, (list, tuple)):
                required_params = sum(1 for p in params.values() 
                                    if p.default == inspect.Parameter.empty 
                                    and p.kind != inspect.Parameter.VAR_POSITIONAL)
                
                # If we have a perfect match of required parameters
                if len(self.input) == required_params:
                    return 'args', self.input
                
                # If there's a *args parameter and we have multiple items
                if any(p.kind == inspect.Parameter.VAR_POSITIONAL for p in params.values()):
                    return 'args', self.input
                
                # If we have exactly one parameter and it's not variadic
                if len(params) == 1 and not any(p.kind == inspect.Parameter.VAR_POSITIONAL for p in params.values()):
                    return 'as_is', self.input

            return 'as_is', self.input
        except Exception as e:
            print(f"{Fore.YELLOW}Warning: Could not determine call method: {str(e)}{Style.RESET_ALL}")
            return 'as_is', self.input

    def run_test(self) -> TestResult:
        try:
            call_method, processed_input = self.determine_call_method()
            
            if call_method == 'args':
                result = self.func(*processed_input)
            elif call_method == 'kwargs':
                result = self.func(**processed_input)
            else:  # 'as_is'
                result = self.func(processed_input)

            return TestResult(
                passed=result == self.solution,
                input_value=self.input,
                expected=self.solution,
                received=result,
                index=self.index
            )
        except Exception as e:
            return TestResult(
                passed=False,
                input_value=self.input,
                expected=self.solution,
                received=None,
                index=self.index,
                error=e
            )

    def determine_result(self) -> Union[Success, Failure]:
        test_result = self.run_test()
        response_class = Success if test_result.passed else Failure
        return response_class(
            index=test_result.index,
            input=test_result.input_value,
            expected=test_result.expected,
            received=test_result.received,
            error=getattr(test_result, 'error', None)
        )

class TestSuite:
    def __init__(self, **kwargs):
        self.testcases: List[Dict] = kwargs.get('testcases', [])
        self.func: callable = kwargs.get('func', lambda x: x)
        self.results: List[Union[Success, Failure]] = []

    def run_tests(self) -> None:
        total = len(self.testcases)
        passed = 0
        failed = 0

        print(f"\n{Fore.CYAN}Running {total} test cases...{Style.RESET_ALL}\n")

        for i, testcase in enumerate(self.testcases, 1):
            try:
                tc = TestCase(
                    index=i,
                    input=testcase.get('input'),
                    solution=testcase.get('solution'),
                    func=self.func
                )
                result = tc.determine_result()
                self.results.append(result)
                
                if isinstance(result, Success):
                    passed += 1
                else:
                    failed += 1

                result.disclose()
                result.explain()
                print("-" * 50)  # Separator between test cases

            except Exception as e:
                print(f"{Fore.RED}Error in test case {i}: {str(e)}{Style.RESET_ALL}")
                failed += 1

        # Print summary
        print(f"\n{Fore.CYAN}Test Summary:{Style.RESET_ALL}")
        print(f"Total Tests: {total}")
        print(f"Passed: {Fore.GREEN}{passed}{Style.RESET_ALL}")
        print(f"Failed: {Fore.RED}{failed}{Style.RESET_ALL}")
        print(f"Success Rate: {Fore.CYAN}{(passed/total)*100:.1f}%{Style.RESET_ALL}\n")