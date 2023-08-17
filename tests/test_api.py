import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 1, 1) == 2

    def test_multiply_seccess(self):
        assert self.calculator.multiply(self, 3, 5) == 15

    def test_substraction_success(self):
        assert self.calculator.subtraction(self, 4, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(self,1, 0)


    def teardown(self):
        print('Dыполнение метода Teardown')