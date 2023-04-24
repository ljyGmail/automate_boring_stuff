# def spam():
#     bacon()


# def bacon():
#     raise Exception('This is the error message.')


# spam()

import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('data/ch11/errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to data/ch11/errorInfo.txt')
