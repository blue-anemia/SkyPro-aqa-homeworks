import pytest
from calculator import Calculator

calculator = Calculator()


# маркер для пропуска теста
@pytest.mark.skip(reason="починить тест позже")
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9


# маркер параметризации теста
@pytest.mark.parametrize("num1, num2, result", [(4, 5, 9), (-6, -10, -16), (5.61, 4.29, 9.9)])
def test_sum_positive_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result


# для пометки теста ожидаемого как провальный - для негативного теста, strict = True - чтобы
# упавший тест был помечен как пройден, а не упавший тест - как проваленный
@pytest.mark.xfail(strict=True)
def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16


# собственный маркер
@pytest.mark.positive_test
# затем в терминале надо прописать pytest -m positive_test для запуска теста только помеченных этим маркером
def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0


@pytest.mark.positive_test
def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)
    assert res == 9.9


@pytest.mark.positive_test
def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10


@pytest.mark.positive_test
def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5


def test_div_by_zero():
    calculator = Calculator()

    # здесь пишу исключение для теста с ошибкой
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)


def test_avg_empty_list():
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0


def test_avg_positive_list():
    calculator = Calculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res = calculator.avg(numbers)
    assert res == 5
