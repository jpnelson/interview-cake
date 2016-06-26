import random


def rand7():
    return random.randint(1, 7)


def rand5():

    x = rand7()

    while x > 5:
        x = rand7()

    return x

if __name__ == '__main__':
    print rand5()
