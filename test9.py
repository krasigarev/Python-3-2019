def print_top_triangle(n):
    for row in range(1, n+1):
        for col in range(1, row+1):
            print(f"{col} ", end='')
        print()


def print_botton_triangle(n):
    for row in range(1, n):
        for col in range(1, n-row+1):
            print(f"{col} ", end='')
        print()


def print_triangle(n):
    print_top_triangle(n)
    print_botton_triangle(n)


if __name__ == "__main__":
    number = int(input())
    print_triangle(number)

