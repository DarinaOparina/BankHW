import pytest
from src.decorators import log


@pytest.mark.parametrize("action, expected", [
    ("success", "test_func ok\n"),
    ("error", "test_func error: ZeroDivisionError. Inputs: (), {}\n")
])
def test_log_console(capsys, action, expected):
    """Тестирует вывод в консоль"""
    @log()
    def test_func():
        if action == "error":
            raise ZeroDivisionError
        return "ok"

    if action == "error":
        with pytest.raises(ZeroDivisionError):
            test_func()
    else:
        test_func()

    assert capsys.readouterr().out == expected


@pytest.mark.parametrize("action, expected", [
    ("success", "test_func_file ok\n"),
    ("error", "test_func_file error: ValueError. Inputs: (), {}\n")
])
def test_log_file(tmp_path, action, expected):
    """Тестирует вывод в файл"""
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def test_func_file():
        if action == "error":
            raise ValueError
        return "ok"

    if action == "error":
        with pytest.raises(ValueError):
            test_func_file()
    else:
        test_func_file()

    assert log_file.read_text(encoding="utf-8") == expected
