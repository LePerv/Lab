import threading
import math
import time

results = []

def f(x):
    print('f')
    results.append(math.sqrt(int(x)))

def g(x):
    print('g')
    while True:
        foo = True
    results.append(int(x) * int(x))

def checkResults():
    return len(results) == 2

def main():
    x = input()

    t1 = threading.Thread(target=f, args=(x,))
    t2 = threading.Thread(target=g, args=(x,))

    startTime = time.time()

    t1.start()
    t2.start()

    while not checkResults() and time.time() - startTime < 10:
        needBreak = False
        for x in results:
            if x == 0:
                needBreak = True
        if needBreak:
            break

    print('DONE\n\n')
    result = 1
    for x in results:
        result *= x
    print(result)

if __name__ == '__main__': main()
