import math

#function is_number checks if the numbers are valid


def is_number(input):
    try:
        input = float(input)
    except:
        if input == "pi":
            input = math.pi
        else:
            print("ERROR, first number is invalid")
            exit()
    return input

#function is_operator checks if the operator is valid


def is_operator(operator_input):
    operator_list = ["+", "-", "*", "%", "**", "//", "/", "rt"]
    if operator_input not in operator_list:
        print("ERROR, invalid operator")
        exit()
    return operator_input


num1 = is_number(input("Enter first number:"))

operator = is_operator(input("Enter operator:"))

num2 = is_number(input("Enter second number:"))


#function output provides the result
def output(num1, num2, operator):
    operators = {"+": num1 + num2, "-": num1 - num2, "*": num1 * num2, "/": num1 / num2, "**": num1 ** num2, "//": num1
                // num2, "%": num1 % num2, "rt": num1 ** (1/num2)}

    return operators[operator]


result = (output(num1, num2, operator))
div_result = result / 2
div_result = str(div_result)
str = str(result)
z = str.find(".")

if len(div_result[z+1:]) <= 1:
    result = int(result)
    print(result)
else:
    print(result)
