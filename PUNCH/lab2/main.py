import threading
import math

results = []

def f(x):
    print('+')
    results.append(math.sqrt(x))

def g(x):
    results.append(x * x)

def checkResults():
    return len(results) == 2

def main():
    x = input()

    t1 = threading.Thread(target=f, args=(x,))
    t2 = threading.Thread(target=g, args=(x,))

    t1.start()
    t2.start()

    while not checkResults():
        print('running...')

    print('DONE\n\n')
    result = results[0] * results[1]
    print(result)

if __name__ == '__main__': main()
