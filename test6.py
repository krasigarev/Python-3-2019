def define_sign(num):
    if num < 0:
        print(f"The number {num} is negative.")
    elif num == 0:
        print("The number 0 is zero.")
    else:
        print(f"The number {num} is positive.")


if __name__=="__main__":
    number = int(input())
    define_sign(number)
    