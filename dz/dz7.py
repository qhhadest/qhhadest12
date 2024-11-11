
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} of {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
def validate_positive(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) and arg > 0 for arg in args):
            raise ValueError("All arguments must be positive numbers")
        return func(*args, **kwargs)
    return wrapper

def add_prefix_suffix(prefix="", suffix=""):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}{result}{suffix}"
        return wrapper
    return decorator


@count_calls
@validate_positive
@add_prefix_suffix(prefix="Result: ", suffix="!")
def add(a, b):
    return a + b

print(add(3, 5))
print(add(7, 2))

