print("hello world")


def count_down(count):
    if count == 0:
        print('Go!')
    else:
        print(count)
        count_down(count - 1)
# count_down(10)


def find(low, high):
    mid = (high + low) // 2
    answer = input("Is it %d? (l/h/y): " % mid)
    print("answer = ", answer.upper())
    if (answer != 'l') and (answer != 'h'):
        print("Got it!")
    else:
        if answer == 'l':
            find(low, mid)
        else:
            find(mid+1, high)


find(0, 100)
