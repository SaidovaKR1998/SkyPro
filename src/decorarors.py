from functools import wraps
import datetime


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Записываем начало выполнения функции
            start_time = datetime.datetime.now()
            func_name = func.__name__
            log_message_start = f"{func_name} started at {start_time}\n"

            if filename:
                with open(filename, 'a') as f:
                    f.write(log_message_start)
            else:
                print(log_message_start, end='')

            try:
                result = func(*args, **kwargs)
                # Логируем успешное завершение
                end_time = datetime.datetime.now()
                log_message_ok = f"{func_name} ok at {end_time}. Result: {result}\n"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message_ok)
                else:
                    print(log_message_ok, end='')
                return result
            except Exception as e:
                # Логируем ошибку
                end_time = datetime.datetime.now()
                log_message_error = (
                    f"{func_name} error: {type(e).__name__} at {end_time}. "
                    f"Inputs: {args}, {kwargs}\n"
                )
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message_error)
                else:
                    print(log_message_error, end='')
                raise  # Пробрасываем ошибку дальше

        return wrapper

    return decorator