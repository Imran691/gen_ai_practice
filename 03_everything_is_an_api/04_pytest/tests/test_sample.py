def func(x):
    return x + 1

# keyword "test" is used before the function to be tested
# CLI command "pytest" to run tests of all files prefixed with the keyword "test" in the directory
# In order to run individual test use "pytest file_name"
# In order to not get the information in console, use "pytest -q file_name"
# In order to run multiple files prefixed with test keyword "pytest test*.py"
def test_answer():
    assert func(3) == 5