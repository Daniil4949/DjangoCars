from celery import shared_task


@shared_task()
def foo(x=1, y=3):
    print(f"x + y = {x + y}")
    return f"x + y = {x + y}"
