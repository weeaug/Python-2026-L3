import math

def ex1():
    radius = int(input("Enter circle radius: "))
    area = round(math.pi * radius ** 2)
    print(f"Circle area = {area:.1f}")
#ex1()

def ex2():
    celsius = int(input("Enter the temperature in Celsius: "))
    fahrenheit = round((celsius * 9/5) + 32)
    print(f"{celsius} (C) = {fahrenheit:.1f} (F)")
#ex2()

def ex3():
    num = int(input("Enter a number: "))
    if num <= 1:
        print(f"{num} is a NOT prime number")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is a NOT prime number")
#ex3()

def ex4():
    num = int(input("Enter a number: "))
    if num <= 0:
        print("Please enter a positive number")
    else:
        divisor_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisor_sum += i
        if divisor_sum == num:
            print(f"{num} is a perfect number")
        else:
            print(f"{num} is a NOT perfect number")
#ex4()

def ex5():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    user_color = input("What is your favorite color? ").strip().lower()
    if user_color in colors:
        index = colors.index(user_color)
        print(f"Your color is at index {index} in my list")
    else:
        print("Sorry, I could not find your color")
#ex5()

def ex6():
    range1 = list(range(7))
    print("range1:", range1)
    range2 = list(range(1, 11, 3))
    print("range2:", range2)
    range3 = list(range(5, 0, -1))
    print("range3:", range3)
    range4 = list(range(6, -3, -2))
    print("range4:", range4)
#ex6()

def ex7():
    def remove_dollar_sign(s):
        return s.replace("$", "")
    string = str(input("Enter the string: "))
    clean_string = remove_dollar_sign(string)
    print(clean_string)
#ex7()

def ex8():
    def extract_even(I):
        return [num for num in I if num % 2 == 0]
    numbers = [1, 4, 5, -1, 10]
    new_list = extract_even(numbers)
    print(new_list)
#ex8()

def ex9():
    def factorial(n):
        result = 1
        for i in range (1, n + 1):
            result *= i
        return result
    number = int(input("Enter a number: "))
    print(f"The factorial of {number} is: {factorial(number)}")
#ex9()

def ex10():
    def get_divisors(n):
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors
    number = int(input("Enter a number: "))
    result = get_divisors(number)
    print(f"The divisors of {number} are: {result}")
#ex10()

def ex11():
    def calculate_distance(x1, y1, x2, y2):
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance
    print("Enter the first point:")
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    print("Enter the second point:")
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    result = calculate_distance(x1, y1, x2, y2)
    print(f"The distance between two points is: {result:.2f}")
#ex11()

def ex12():
    def draw_pattern(m, n):
        for i in range(m):
            if i == 0 or i == m - 1:
                print("* " * n)
            else:
                print("* " + "  " * (n - 2) + "*")
    draw_pattern(4, 5)
#ex12()