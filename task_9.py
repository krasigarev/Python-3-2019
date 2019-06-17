def find_result(num_str):
    num_even = 0
    num_odd = 0

    for char in num_str:

        if char == '-':
            continue
        num = int(char)

        if num % 2 == 0:
            num_even += num
        else:
            num_odd += num

    return num_odd * num_even



if __name__ == '__main__':
    string_num = input()
    print(find_result(string_num))

