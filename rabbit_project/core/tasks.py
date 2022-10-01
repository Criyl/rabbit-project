from celery import shared_task
import time

from core.models import Fibonacci


@shared_task()
def calculate_fibonacci(num: int) -> int:
    if num <= 1:
        return 0
    if num <= 3:
        return 1
    result = calculate_fibonacci(num-1) + calculate_fibonacci(num-2)
    return result


@shared_task
def factorial(num: int) -> int:
    if num < 1:
        return 1
    return num*factorial(num-1)


@shared_task
def sleep(seconds: float) -> bool:
    time.sleep(seconds)
    return True
