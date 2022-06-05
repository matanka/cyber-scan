import time
import random


def background_task():

    delay = random.randint(2, 10)
    time.sleep(delay)
    print(f"Simulating {delay} second delay")

    if bool(random.getrandbits(1)):
        print("Task completed")
        return True
    else:
        error = "some random error"
        print(error)
        raise Exception(error)
