n = int(input())


def print_top_button(num):
    print('-'*(num*2))


def print_body(number):
    for i in range(1, number - 1):
        print('-' + "\\/" * int((2*number-2)/2) + '-')


print_top_button(n)
print_body(n)
print_top_button(n)
