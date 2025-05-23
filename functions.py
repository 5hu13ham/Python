#fibonacci series
import itertools


def fibo(n):
    a, b = 0, 1
    series = []
    print('[', end='')
    for i in range(n+1):
        if i < n:
            print(a, end=', ')
        else:
            print(a, end='')
        series.append(a)
        a, b = b, a+b

    print(']')
    print(series)

    return series

print(fibo(10))

a = fibo
print("Running a fibonacci series")
a(10)

#another function

def ask_user(prompt, retries = 4, reminder = "Please try again"):
    for i in itertools.count():
        response = input(prompt).lower()

        if response in {'y', 'ye', 'yep', 'yo', 'yeah', 'yea', 'yes'}:
            print ('true')
            break

        if response in {'n', 'no', 'nope', 'nop', 'nah', 'na'}:
            print ('false')
            break

        retries = retries - 1
        if retries < 0:
            print(reminder)
            raise ValueError('invalid user response')
        print(reminder)


ask_user("Do you want to continue? y/n: ")

#default value
print("new testing started")
i = 1
i = 6
def argum(arg = i):
    print(arg)

i = 7
argum()

