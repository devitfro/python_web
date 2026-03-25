import time

def retry(times, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}, try {i+1}")
                    time.sleep(delay)
            raise Exception("All retries failed")
        return wrapper
    return decorator