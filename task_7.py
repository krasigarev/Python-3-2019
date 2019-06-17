# task_7  moeto reshenie

type_value = input()


def type_init(argument):
    if type_value == 'int':
        num_1 = int(input())
        num_2 = int(input())
        if num_1 > num_2:
            print(num_1)
        else:
            print(num_2)


def type_char(argument):
    if type_value == 'char':
        char_1 = input()
        char_2 = input()
        if ord(char_1) > ord(char_2):
            print(str(char_1))
        else:
            print(str(char_2))

    elif type_value == 'string':
        str_1 = input()
        str_2 = input()
        if len(str_1) > len(str_2):
            print(str_1)
        else:
            print(str_2)


def print_type():
    type_init(type_value)
    type_char(type_value)


print_type()

