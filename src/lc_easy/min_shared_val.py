# https://www.glassdoor.com/Interview/Wix-Software-Engineer-Interview-Questions-EI_IE391615.0,3_KO4,21_IP4.htm?filter.jobTitleFTS=Software+Engineer
# Given two arrays, return the index of the minimal value present in both arrays, or -1 if non exists.

def min_val_present(arr1, arr2):
    i = 0
    j = 0

    min_val = None

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                if (not min_val) or (arr1[i] < min_val):
                    min_val = arr1[i]
    return min_val

cases = [ 
    {
        'input':  [[1,345,2,8,5],[5,8,2,9,11]],
        'solution': 2
    },
    # {
    #     'input': "]",
    #     'solution': False
    # },
    # {
    #     'input': "(])",
    #     'solution': False
    # },
]

def passed():
    return "passed".upper()

def failed():
    return "failed".upper()

def pass_fail(is_correct: bool):
    return passed() if is_correct else failed()

def test():
    for i, case in enumerate(cases, 1):
        answer = min_val_present(case['input'][0], case['input'][1])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test()