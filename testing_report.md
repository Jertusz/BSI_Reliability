# Testing report
## Used libraries:
- [Pylint](https://pypi.org/project/pylint/) - static code checking for known PEP8 errors
- [Pytest](https://pypi.org/project/pytest/) - Test driver for our tests
- [Pytest-cov](https://pypi.org/project/pytest-cov/)- Pytest plugin which allows us to generate
- [Poetry](https://pypi.org/project/poetry/) - easier maintenance of virtual environment

## Testing methodology
First `pylint exercise_1.py` command was run to check for linting errors.
Than `pytest test_exercise1.py --cov --cov-report=html` was run to generate coverage of tests for `exercise_1.py` file.

## Pylint run results
Running `pylint exercise_1.py` gave the following result:
```bash
************* Module exercise_1
exercise_1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
exercise_1.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
exercise_1.py:8:0: C0116: Missing function or method docstring (missing-function-docstring)
exercise_1.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
exercise_1.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
exercise_1.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
exercise_1.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
exercise_1.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
exercise_1.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)

-------------------------------------------------------------------
Your code has been rated at 7.43/10
```
### Conclusions
All of the above errors are related to missing docstrings which were left out on purpose due to the nature of functions. The function names and parameters are self explanatory, which allows us to don't put docstrings inside every one of them.
### Possible fixes
There are two ways of taking care of the errors.
Putting in docstrings (recommended).
Adding a comment at the beginning of the file which would exclude these types of errors from being checked (`missing-module-docstring` & `missing-function-docstring`)

## Pytest run results
After running the command `pytest test_exercise1.py --cov --cov-report=html ` the result we got was as follows:
```bash
==================================================================== test session starts ====================================================================
platform linux -- Python 3.9.6, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/js/pjatk/bsi/BSI_Reliability
plugins: cov-3.0.0
collected 10 items                                                                                                                                          

test_exercise1.py ..........                                                                                                                          [100%]

----------- coverage: platform linux, python 3.9.6-final-0 -----------
Coverage HTML written to dir htmlcov


==================================================================== 10 passed in 0.03s =====================================================================
```
Which suggests that the code is written correctly and all tests are passing. The coverage wasn't explicitly shown, it was written to a file instead which can be checked under the `htmlcov/exercise_1_py.html` directory. The file provides a detail overview of lines that were skipped during testing.
To get explicit coverage report in console the following command was run: `pytest test_exercise1.py --cov`
Which resulted in a following log:
```bash
==================================================================== test session starts ====================================================================
platform linux -- Python 3.9.6, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/js/pjatk/bsi/BSI_Reliability
plugins: cov-3.0.0
collected 10 items                                                                                                                                          

test_exercise1.py ..........                                                                                                                          [100%]

----------- coverage: platform linux, python 3.9.6-final-0 -----------
Name                Stmts   Miss  Cover
---------------------------------------
exercise_1.py          35     10    71%
test_exercise1.py      21      0   100%
---------------------------------------
TOTAL                  56     10    82%


==================================================================== 10 passed in 0.03s =====================================================================
```
### Conclusions
After further investigation it has been decided that for `exercise_1.py` coverage of 71% is fully acceptable as running the `main` function and all functions inside shouldn't be tested due to varying user input.

### Possible fixes
All functions used inside `exercise_1.py` except main, could be moved to a separate module, to allow proper testing without having less than 100% of code coverage

