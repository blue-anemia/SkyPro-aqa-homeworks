import pytest
from String_utils import StringUtils

# Создаем экземпляр StringUtils для тестов
utils = StringUtils()


@pytest.mark.positive_test
def test_capitilize():
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("SKYPRO") == "Skypro"
    assert utils.capitilize("sky pro") == "Sky pro"


@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_capitilize_negative():
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("999") == "999"
    assert utils.capitilize(333) == 333
    assert utils.capitilize("123 abc") == "123 abc"
    assert utils.capitilize(None) == None
    assert utils.capitilize("!") == "!"


@pytest.mark.positive_test
def test_trim():
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro") == "skypro"
    assert utils.trim("   skypro   ") == "skypro   "
    assert utils.trim("skypro   ") == "skypro   "
    assert utils.trim("   ") == ""


@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_trim_negative():
    assert utils.trim("") == ""
    assert utils.trim(1.2) == 1.2
    assert utils.trim(678) == 678  # тут баг?
    assert utils.trim(None) == None
    assert utils.trim(True) == True
    assert utils.trim([1, 2, 3, 4]) == [1, 2, 3, 4]  # и тут баг?


@pytest.mark.positive_test
def test_to_list():
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1;2;3", ";") == ["1", "2", "3"]
    assert utils.to_list("") == []
    assert utils.to_list("a|b|c", "|") == ["a", "b", "c"]


@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_to_list_negative():
    assert utils.to_list("a b c d", " ") == ["a", "b", "c", "d"]
    assert utils.to_list(",,,") == ["", "", "", ""]
    assert utils.to_list("skypro") == ["skypro"]  # не совсем понимаю ОР


@pytest.mark.positive_test
def test_contains():
    assert utils.contains("SkyPro", "S") == True
    assert utils.contains("SkyPro", "U") == False
    assert utils.contains("", "a") == False


@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_contains_negative():
    assert utils.contains("SkyPro", "s") == False
    assert utils.contains("SkyPro", "yP") == False


@pytest.mark.positive_test
def test_delete_symbol():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol("SkyPro", "SkyPro") == ""
    assert utils.delete_symbol("123", "1") == "23"
    assert utils.delete_symbol("hello world!", "o") == "hell wrld!"


@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_delete_symbol_negative():
    assert utils.delete_symbol("SkyPro", "H") == "SkyPro"
    assert utils.delete_symbol("", "") == ""
    assert utils.delete_symbol(None, None) == None
    assert utils.delete_symbol(123, 1) == 123


@pytest.mark.positive_test
def test_starts_with():
    assert utils.starts_with("SkyPro", "S") == True
    assert utils.starts_with("SkyPro", "P") == False
    assert utils.starts_with("", "S") == False


@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_starts_with_negative():
    assert utils.starts_with("skyPro", "S") == False
    assert utils.starts_with("SkyPro", "k") == False
    assert utils.starts_with("", "S") == True


@pytest.mark.positive_test
def test_end_with():
    assert utils.end_with("SkyPro", "o") == True
    assert utils.end_with("SkyPro", "y") == False
    assert utils.end_with("", "o") == False


@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_end_with_negative():
    assert utils.end_with("SkyPro", "O") == False
    assert utils.end_with("SkyPro", "Pro") == True
    assert utils.end_with("", "o") == True


@pytest.mark.positive_test
def test_is_empty():
    assert utils.is_empty("") == True
    assert utils.is_empty(" ") == True
    assert utils.is_empty("SkyPro") == False
    assert utils.is_empty("Hello World!") == False
    assert utils.is_empty("123") == False
    assert utils.is_empty(" Hello world!") == False
    assert utils.is_empty("   Hello!   ") == False


@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_is_empty_negative():
    assert utils.is_empty("  ") == False
    assert utils.is_empty("") == False
    assert utils.is_empty("Sky Pro") == True
    assert utils.is_empty("   Sky Pro   ") == True


@pytest.mark.positive_test
def test_list_to_string():
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert utils.list_to_string([]) == ""
    assert utils.list_to_string(["hello"]) == "hello"


@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_list_to_string_negative():
    assert utils.list_to_string([1, "2", 3.0]) == "1, 2, 3.0"
    assert utils.list_to_string(["a", "b", "c"], ":") == "a:b:c"
    assert utils.list_to_string("a:b:c") == "a:b:c"
    assert utils.list_to_string(123) == 123
    assert utils.list_to_string(None) == None
    assert utils.list_to_string(["Sky", "Pro"]) == True


if __name__ == "__main__":
    pytest.main()
