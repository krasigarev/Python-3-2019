base = float(input())
height = float(input())


def calculate_triangle_area(num1, num2):
    area = (num1 * num2) / 2
    return area


if __name__ == "__main__":
    print(f"{calculate_triangle_area(base, height):.12g}")




