# Group multiple tests in one class

class TestClass:
    def test_one(self):
        x = "this"
        # to check if "h" exists in variable x
        assert "h" in x

    def test_two(self):
        x = "hello"
        # to check if x(string) has attribite named "check"
        assert hasattr(x, "check")