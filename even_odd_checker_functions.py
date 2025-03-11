def get_integer_input():
    number = int(input("Enter an Integer: "))
    return number

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    number = get_integer_input()
    n1 = number
    number = check_even_odd(number)
    print(f"{n1} is an {number} number")

if __name__ == "__main__":
    main()