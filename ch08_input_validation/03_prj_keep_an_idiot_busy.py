import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt=prompt, yesVal='ok', noVal='sorry')
    if response == 'sorry':
        break
