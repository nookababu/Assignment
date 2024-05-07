import functools
import inspect

def memoize(max_cache_size=None):
    def decorator(func):
        cache = {}
        if max_cache_size is None:
            max_cache_size = float('inf')

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal cache
            key = inspect.signature(func).bind(*args, **kwargs).arguments
            key_str = str(key)
            
            if key_str not in cache:
                result = func(*args, **kwargs)
                if len(cache) >= max_cache_size:
                    cache.popitem() 
                cache[key_str] = result            
            return cache[key_str]        
        return wrapper
    return decorator
@memoize(max_cache_size=10)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5)) 
print(fibonacci(10)) 