import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 5, 9) == 14

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 10, 8) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(self, 7, 0)

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 4, 4) == 16

    def test_division_success(self):
        assert self.calculator.division(self, 20, 4) == 5

    def teardown(self):
        print('Выполнение метода Teardown')