#!/usr/bin/env python3
"""
Redis basic exercise
"""

import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs
    for a particular function in Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store inputs
        self._redis.rpush(input_key, str(args))

        # Execute function
        result = method(self, *args, **kwargs)

        # Store outputs
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.
    """
    redis_instance = method.__self__._redis
    method_name = method.__qualname__

    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        print(
            f"{method_name}(*{inp.decode('utf-8')}) -> "
            f"{out.decode('utf-8')}"
        )


class Cache:
    """Cache class using Redis"""

    def __init__(self) -> None:
        """Initialize the Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random UUID key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
