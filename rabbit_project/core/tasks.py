from tokenize import Double
from celery import shared_task
import time


@shared_task
def calculate_fibonacci(num: int) -> int:
    if num <= 0:
        return 0
    if num <= 2:
        return 1
    result = calculate_fibonacci(num-1) + calculate_fibonacci(num-2)
    return result


@shared_task
def calculate_factorial(num: int) -> int:
    if num < 1:
        return 1
    result = num * calculate_factorial(num-1)
    return result


@shared_task
def celery_sleep(sec: int) -> int:
    t = time.process_time()
    time.sleep(sec)
    elapsed_time = time.process_time() - t
    return elapsed_time*1000
