#!/usr/bin/python3
import calculator_1

if __name__ == "__main__":
    # Define variables a and b
    a = 10
    b = 5

    # Perform calculations using functions from calculator_1
    addition_result = calculator_1.add(a, b)
    subtraction_result = calculator_1.sub(a, b)
    multiplication_result = calculator_1.mul(a, b)
    division_result = calculator_1.div(a, b)

    # Print the results with the desired format
    print(f"{a} + {b} = {addition_result}")
    print(f"{a} - {b} = {subtraction_result}")
    print(f"{a} * {b} = {multiplication_result}")
    print(f"{a} / {b} = {division_result}")
