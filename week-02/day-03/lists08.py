# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

def calculator(operator, op_1, op_2):
    if operator == '+':
        result = op_1, op_2
    elif operator == '-':
        result = op_1, op_2
    elif operator == '*':
        result = op_1 * op_2
    elif operator == '/':
        if op_2 != 0:
            result = op_1 / op_2
        else:
            result = "No division by 0"
    elif operator == '%':
        if op_2 != 0:
            result = op_1 % op_2
        else:
            result = "No division by 0"
    print('The result is: ' + result)

inp_1 = input('Please type in what kind of operation you want to do (e.g. + - * / %): ')
inp_2 = input('What is the first number? ')
inp_3 = input('What is the second number? ')

calculator(inp_1, inp_2, inp_3)

# not working yet, because it doesn't add numbers together, but places them next to each other