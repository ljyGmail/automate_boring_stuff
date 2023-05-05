import pyinputplus as pyip

# print('Please enter a number:')
# response = pyip.inputNum()

# print(f'response: {response}')

# response = input('Enter a number: ')
# print(f'type(response): {type(response)}')  # ==> <class 'str'>


# response = pyip.inputInt(prompt='Enter a number: ')
# print(f'type(response): {type(response)}')  # ==> <class 'int'>

# help(pyip.inputChoice)

# The min, max, greaterThan, and lessThan Keyword Arguments
# response = pyip.inputNum('Enter num: ', min=4)
# print(f'response: {response}')

# response = pyip.inputNum('Enter num greater than 4: ', greaterThan=4)
# print(f'response: {response}')

# response = pyip.inputNum('Enter num less than 6: ', lessThan=6)
# print(f'response: {response}')

# response = pyip.inputNum('> (min: 4, less than 6): ', min=4, lessThan=6)
# print(f'response: {response}')

# The blank Keyword Argument
# response = pyip.inputNum('Enter num: ')
# print(f'response: {response}')

# response = pyip.inputNum('Enter num (blank allowed): ', blank=True)
# print(f'response: {response}')

# The limit, timeout, and default Keyword Arguments
# try:
#     response = pyip.inputNum('Enter a number: ', limit=2)
# except Exception as e:
#     print(type(e))
#     print('You have only 2 chances to enter a number. Bye!')

# try:
#     response = pyip.inputNum(prompt='Enter a number: ', timeout=3)
# except Exception as e:
#     print(type(e))
#     print('You have only 3 seconds to enter.')

# response = pyip.inputNum(prompt='Enter a number: ', limit=2, default='N/A')
# print(f'response: {response}')

# The allowRegexes and blockRegexes Keyword Arguments
# response = pyip.inputNum(prompt='Enter a number: ', allowRegexes=[
#                          r'(I|V|X|L|C|D|M)+', r'zero'])
# print(f'response: {response}, type(response): {type(response)}')

# response = pyip.inputNum(prompt='Enter a number: ', allowRegexes=[
#                          r'(i|v|x|l|c|d|m)+', r'zero'])
# print(f'response: {response}, type(response): {type(response)}')

# response = pyip.inputNum(prompt='Enter a number: ', blockRegexes=[r'[02468]$'])
# print(f'response: {response}')

# when allowRegexes and blockRegexes are both specified, the allow list overrides the block list
# response = pyip.inputStr(prompt='Enter a string: ',
#                          allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
# print(f'response: {response}')

# Passing a Custom Validation Function to inputCustom()
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception(
            f'The digits must add up to 10, not {sum(numbersList)}')
    return int(numbers)  # Return an int form of numbers.


response = pyip.inputCustom(
    addsUpToTen, prompt='Enter a number that add up to 10: ')
print(f'response: {response}')
