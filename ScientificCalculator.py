pi = 3.1415926535
e = 2.7182818284

class CustomError(Exception):
    pass

# 1. Basic Arithmetic Operations
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise CustomError("Cannot divide by zero.")
    return a / b

def modulus(a, b):
    if b == 0:
        raise CustomError("Cannot take modulus with zero.")
    return a % b

# 2. Advanced Mathematical Functions
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

def square_root(a):
    if a < 0:
        raise CustomError("Square root of negative number is not defined.")
    if a == 0:
        return 0
    guess = a
    tolerance = 1e-10
    while True:
        next_guess = 0.5 * (guess + a / guess)
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess

def fac(a):
    if a < 0:
        raise CustomError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

def exp(x, terms=20):
    result = 1.0
    numerator = 1.0
    denominator = 1.0
    for i in range(1, terms):
        numerator *= x
        denominator *= i
        result += numerator / denominator
    return result

def custom_ln(x, terms=100):
    if x <= 0:
        raise CustomError("ln(x) is undefined for x <= 0.")
    k = 0
    while x > 2:
        x /= 2
        k += 1
    while x < 0.5:
        x *= 2
        k -= 1
    y = (x - 1) / (x + 1)
    y_squared = y * y
    result = 0.0
    power = y
    denominator = 1
    for _ in range(terms):
        result += power / denominator
        power *= y_squared
        denominator += 2
    ln2 = 0.69314718056
    return 2 * result + k * ln2

def sin(x, in_degrees=False, terms=10):
    if in_degrees:
        x = DegreeToRadian(x)
    result = 0.0
    sign = 1
    for n in range(terms):
        power = 2 * n + 1
        fact = 1
        for i in range(1, power + 1):
            fact *= i
        result += sign * (x ** power) / fact
        sign *= -1
    return result

def cosi(x, in_degrees=False, terms=10):
    if in_degrees:
        x = DegreeToRadian(x)
    result = 0.0
    sign = 1
    for n in range(terms):
        power = 2 * n
        fact = 1
        for i in range(1, power + 1):
            fact *= i
        result += sign * (x ** power) / fact
        sign *= -1
    return result

def tang(x, in_degrees=False, terms=10):
    if in_degrees:
        x = DegreeToRadian(x)
    cos_val = cosi(x, False, terms)
    if abs(cos_val) < 1e-10:
        raise CustomError("Tangent undefined for angle (cos(x) ≈ 0).")
    sin_val = sin(x, False, terms)
    return sin_val / cos_val

# 3. Number System Conversions
def convert_base(input_str, from_base, to_base):
    base_map = {1: 2, 2: 8, 3: 10, 4: 16}
    try:

        #converts number of any base to int
        decimal_value = int(input_str, base=base_map[from_base])
    except ValueError:
        raise CustomError("Invalid number for the chosen input base.")

    if to_base == 1:
        return bin(decimal_value)
    elif to_base == 2:
        return oct(decimal_value)
    elif to_base == 3:
        return str(decimal_value)
    elif to_base == 4:
        return hex(decimal_value)
    else:
        raise CustomError("Invalid output base.")

# 4. Angle and Unit Handling
def RadianToDegree(radian):
    return radian * (180 / pi)

def DegreeToRadian(degree):
    return degree * (pi / 180)




if __name__ == "__main__":
    while(True):
        try:
            print("\nChoose an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Modulus")
            print("6. Power")
            print("7. Square Root")
            print("8. Factorial")
            print("9. Exponential")
            print("10. Natural Log (ln)")
            print("11. Sine")
            print("12. Cosine")
            print("13. Tangent")
            print("14. Radian to Degree")
            print("15. Degree to Radian")
            print("16. Number System Conversion")

            choice = int(input("Enter your choice (1-16): "))

            if choice in [1, 2, 3, 4, 5, 6]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if choice == 1:
                    print("Result:", add(a, b))
                elif choice == 2:
                    print("Result:", sub(a, b))
                elif choice == 3:
                    print("Result:", mul(a, b))
                elif choice == 4:
                    print("Result:", divide(a, b))
                elif choice == 5:
                    print("Result:", modulus(a, b))
                elif choice == 6:
                    b = int(b)
                    print("Result:", power(a, b))

            elif choice == 7:
                a = float(input("Enter number: "))
                print("Result:", square_root(a))

            elif choice == 8:
                a = int(input("Enter number: "))
                print("Result:", fac(a))

            elif choice == 9:
                a = float(input("Enter exponent: "))
                print("Result:", exp(a))

            elif choice == 10:
                a = float(input("Enter number (> 0): "))
                print("Result:", custom_ln(a))

            elif choice in [11, 12, 13]:
                x = float(input("Enter angle: "))
                deg_or_rad = input("Is the angle in degrees? (yes/no): ").strip().lower()
                in_degrees = (deg_or_rad == "yes")
                if choice == 11:
                    print("sin:", sin(x, in_degrees))
                elif choice == 12:
                    print("cos:", cosi(x, in_degrees))
                elif choice == 13:
                    print("tan:", tang(x, in_degrees))

            elif choice == 14:
                a = float(input("Enter angle in radians: "))
                print("Degrees:", RadianToDegree(a))

            elif choice == 15:
                a = float(input("Enter angle in degrees: "))
                print("Radians:", DegreeToRadian(a))

            elif choice == 16:
                print("\nChoose input base:")
                print("1. Binary")
                print("2. Octal")
                print("3. Decimal")
                print("4. Hexadecimal")
                from_base = int(input("Enter input base choice (1-4): "))

                print("Choose output base:")
                print("1. Binary")
                print("2. Octal")
                print("3. Decimal")
                print("4. Hexadecimal")
                to_base = int(input("Enter output base choice (1-4): "))

                input_str = input("Enter the number: ").strip()
                result = convert_base(input_str, from_base, to_base)
                print("Converted:", result)

            else:
                print("Invalid choice!")

        except ValueError as ve:
            print("Value Error:", ve)
        except CustomError as ce:
            print("Math Error:", ce)
        except Exception as e:
            print("Unexpected Error:", e)
