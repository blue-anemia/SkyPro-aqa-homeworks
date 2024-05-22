import pytest
from String_utils import StringUtils

# Создаем экземпляр StringUtils для тестов
utils = StringUtils()


@pytest.mark.parametrize(
    "input,expected",
    [("skypro", "Skypro"), ("SKYPRO", "Skypro"), ("sky pro", "Sky pro")],
)
@pytest.mark.positive_test
def test_capitilize(input, expected):
    assert utils.capitilize(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("", ""),
        (" ", " "),
        ("999", "999"),
        (333, 333),
        ("123 abc", "123 abc"),
        (None, None),
        ("!", "!"),
    ],
)
@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_capitilize_negative(input, expected):
    assert utils.capitilize(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
        ("   skypro   ", "skypro   "),
        ("skypro   ", "skypro   "),
        ("   ", ""),
    ],
)
@pytest.mark.positive_test
def test_trim(input, expected):
    assert utils.trim(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("", ""),
        (1.2, 1.2),
        (678, 678),
        (None, None),
        (True, True),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
    ],
)
@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_trim_negative(input, expected):
    assert utils.trim(input) == expected


@pytest.mark.parametrize(
    "input,delimiter,expected",
    [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1;2;3", ";", ["1", "2", "3"]),
        ("", ",", []),
        ("a|b|c", "|", ["a", "b", "c"]),
    ],
)
@pytest.mark.positive_test
def test_to_list(input, delimiter, expected):
    assert utils.to_list(input, delimiter) == expected


@pytest.mark.parametrize(
    "input,delimiter,expected",
    [
        ("a b c d", " ", ["a", "b", "c", "d"]),
        (",,,", ",", ["", "", "", ""]),
        ("skypro", ",", ["skypro"]),
    ],
)
@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_to_list_negative(input, delimiter, expected):
    assert utils.to_list(input, delimiter) == expected


@pytest.mark.parametrize(
    "input,symbol,expected",
    [("SkyPro", "S", True), ("SkyPro", "U", False), ("", "a", False)],
)
@pytest.mark.positive_test
def test_contains(input, symbol, expected):
    assert utils.contains(input, symbol) == expected


@pytest.mark.parametrize(
    "input,symbol,expected", [("SkyPro", "s", False), ("SkyPro", "yP", False)]
)
@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_contains_negative(input, symbol, expected):
    assert utils.contains(input, symbol) == expected


@pytest.mark.parametrize(
    "input,symbol,expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("", "a", ""),
        ("SkyPro", "SkyPro", ""),
        ("123", "1", "23"),
        ("hello world!", "o", "hell wrld!"),
    ],
)
@pytest.mark.positive_test
def test_delete_symbol(input, symbol, expected):
    assert utils.delete_symbol(input, symbol) == expected


@pytest.mark.parametrize(
    "input,symbol,expected",
    [("SkyPro", "H", "SkyPro"), ("", "", ""), (None, None, None), (123, 1, 123)],
)
@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_delete_symbol_negative(input, symbol, expected):
    assert utils.delete_symbol(input, symbol) == expected


@pytest.mark.parametrize(
    "input,symbol,expected",
    [("SkyPro", "S", True), ("SkyPro", "P", False), ("", "S", False)],
)
@pytest.mark.positive_test
def test_starts_with(input, symbol, expected):
    assert utils.starts_with(input, symbol) == expected


@pytest.mark.parametrize(
    "input,symbol,expected",
    [("skyPro", "S", False), ("SkyPro", "k", False), ("", "S", True)],
)
@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_starts_with_negative(input, symbol, expected):
    assert utils.starts_with(input, symbol) == expected


@pytest.mark.parametrize(
    "input,symbol,expected",
    [("SkyPro", "o", True), ("SkyPro", "y", False), ("", "o", False)],
)
@pytest.mark.positive_test
def test_end_with(input, symbol, expected):
    assert utils.end_with(input, symbol) == expected


@pytest.mark.parametrize(
    "input,symbol,expected",
    [("SkyPro", "O", False), ("SkyPro", "Pro", True), ("", "o", True)],
)
@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_end_with_negative(input, symbol, expected):
    assert utils.end_with(input, symbol) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("", True),
        (" ", True),
        ("SkyPro", False),
        ("Hello World!", False),
        ("123", False),
        (" Hello world!", False),
        ("   Hello!   ", False),
    ],
)
@pytest.mark.positive_test
def test_is_empty(input, expected):
    assert utils.is_empty(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [("  ", False), ("", False), ("Sky Pro", True), ("   Sky Pro   ", True)],
)
@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_is_empty_negative(input, expected):
    assert utils.is_empty(input) == expected


@pytest.mark.parametrize(
    "lst,joiner,expected",
    [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
        (["Sky", "Pro"], ", ", "Sky, Pro"),
        (["Sky", "Pro"], "-", "Sky-Pro"),
        ([], ", ", ""),
        (["hello"], ", ", "hello"),
    ],
)
@pytest.mark.positive_test
def test_list_to_string(lst, joiner, expected):
    assert utils.list_to_string(lst, joiner) == expected


@pytest.mark.parametrize(
    "lst,joiner,expected",
    [
        ([1, "2", 3.0], ", ", "1, 2, 3.0"),
        (["a", "b", "c"], ":", "a:b:c"),
        ("a:b:c", ", ", "a:b:c"),
        (123, ", ", 123),
        (None, ", ", None),
        (["Sky", "Pro"], ", ", True),
    ],
)
@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_list_to_string_negative(lst, joiner, expected):
    assert utils.list_to_string(lst, joiner) == expected


if __name__ == "__main__":
    pytest.main()
