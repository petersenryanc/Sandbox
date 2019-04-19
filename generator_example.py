def main():
    range_of_nums = int(input("Enter amount of numbers: "))
    for i in inclusive_range(range_of_nums):
        print(i, end=' ')
    print()


def inclusive_range(*args):
    numargs = len(args)
    start = int(input("Enter the starting number: "))
    step = int(input("Enter the step size: "))
    if numargs < 1:
        raise TypeError("Expected at least 1 argument, got {}.".format(numargs))
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("Expected at most 3 arguments, got {}.".format(numargs))

    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == '__main__':
    main()
