import sys
from pathlib import Path
import pytest
from src.decorators import log

sys.path.append(str(Path(__file__).parent.parent))


def read_log_file(filename):
    """Чтение содержимого лог-файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def test_log_to_console(capsys):
    """Тестирование логирования в консоль."""
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()
    output = captured.out

    assert "add started at" in output
    assert "add ok at" in output
    assert "Result: 5" in output
    assert result == 5


def test_log_error_to_console(capsys):
    """Тестирование логирования ошибок в консоль."""
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    output = captured.out

    assert "divide started at" in output
    assert "divide error: ZeroDivisionError" in output
    assert "Inputs: (1, 0), {}" in output


def test_log_to_file(tmp_path):
    """Тестирование логирования в файл."""
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(3, 4)
    log_content = read_log_file(log_file)

    assert "multiply started at" in log_content
    assert "multiply ok at" in log_content
    assert "Result: 12" in log_content
    assert result == 12


def test_log_with_kwargs(tmp_path):
    """Тестирование с именованными аргументами."""
    log_file = tmp_path / "kwargs_log.txt"

    @log(filename=str(log_file))
    def greet(name, title="Mr"):
        return f"Hello, {title} {name}"

    result = greet(name="Smith", title="Dr")
    log_content = read_log_file(log_file)

    assert "greet started at" in log_content
    assert "greet ok at" in log_content
    assert "Hello, Dr Smith" in result


def test_log_with_empty_args(capsys):
    """Тестирование функции без аргументов."""
    @log()
    def no_args():
        return "OK"

    result = no_args()
    captured = capsys.readouterr()

    assert "no_args started at" in captured.out
    assert "no_args ok at" in captured.out
    assert result == "OK"


def test_log_with_exception_args(tmp_path):
    """Тестирование логирования аргументов при исключении."""
    log_file = tmp_path / "exception_args.log"

    @log(filename=str(log_file))
    def process_data(data, threshold=0.5):
        if len(data) < 3:
            raise ValueError("Data too short")
        return data * 2

    with pytest.raises(ValueError):
        process_data([1, 2], threshold=0.8)

    log_content = read_log_file(log_file)
    assert "process_data error: ValueError" in log_content
    assert "Inputs: ([1, 2],), {'threshold': 0.8}" in log_content


@pytest.fixture(autouse=True)
def cleanup(request, tmp_path):
    """Фикстура для очистки временных файлов."""
    def remove_test_files():
        test_files = [
            tmp_path / "test_log.txt",
            tmp_path / "kwargs_log.txt",
            tmp_path / "exception_args.log"
        ]
        for file in test_files:
            if file.exists():
                file.unlink()

    request.addfinalizer(remove_test_files)
