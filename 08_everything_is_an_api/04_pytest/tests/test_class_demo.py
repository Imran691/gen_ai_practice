class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1              # value of variable "value" updated to 1
        assert self.value == 1      # To check if value = 1 (pass)

    def test_two(self):
        assert self.value == 1      # To check if value = 1 (fail)