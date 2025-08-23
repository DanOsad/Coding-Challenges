
class TestCaseInputError(Exception):
    pass

class TestCaseSolutionError(Exception):
    pass

class Response:
    def __init__(self, *args, **kwargs):
        self.index = kwargs.pop('index', None)
        self.input = kwargs.pop('input', None)
        self.func = kwargs.pop('func', None)
        self.solution = kwargs.pop('solution', None)

    def explain(self):
        print()

    def disclose(self):
        print('RESULT')

class Success(Response):
    def __init__(self):
        super().__init__()

    def disclose(self):
        print('PASSED')

class Failure(Response):
    def __init__(self):
        super().__init__()

    def disclose(self):
        print('FAILED')

class TestCase:
    def __init__(self, *args, **kwargs):
        self.index = kwargs.pop('index', None)
        self.input = kwargs.pop('input', None)
        self.func = kwargs.pop('func', lambda x: x)
        self.solution = kwargs.pop('solution', None)
        self.response = None

    def validate_input(self):
        if not self.input:
            raise TestCaseInputError("Input must be provided")
        if not self.solution:
            raise TestCaseSolutionError("Solution must be provided")

    def check_for_nested_elements(self):
        # if isinstance(self.input, (list, tuple, set)):
        # for element in self.input:
        if isinstance(self.input, (list, tuple, set)):
            return True
        return False

    def run_test(self):
        print(f"Running test case {self.index} with input: {self.input} and expected solution: {self.solution}")
        
        if isinstance(self.input, (list, tuple, set)):
            if self.check_for_nested_elements():
                result = self.func(*self.input)
            else:
                result = self.func(self.input)
        elif isinstance(self.input, dict):
            result = self.func(**self.input)
        else:
            result = self.func(self.input)
        print(f'Got result: {result}')
        return result
    
    def determine_result(self):
        result = self.run_test()
        return Success() if result == self.solution else Failure()
    
class TestSuite:
    def __init__(self, **kwargs):
        self.testcases = kwargs.pop('testcases', [])
        self.func = kwargs.pop('func', lambda x: x)

    def run_tests(self):
        for i, testcase in enumerate(self.testcases, 1):
            tc = TestCase(
                **{   
                    'index': i,
                    'input': testcase.get('input', None),
                    'solution': testcase.get('solution', None),
                    'func': self.func
                }
            )
            result = tc.determine_result()
            result.disclose()
            result.explain()