import threading

counter = 0
lock = threading.Lock()

def incrementer():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1

def decrementer():
    global counter
    for _ in range(100_000):
        with lock:
            counter -= 1

t1 = threading.Thread(target=incrementer)
t2 = threading.Thread(target=decrementer)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Końcowa wartość licznika: {counter}")

