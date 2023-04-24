# Using the logging Module
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')

#  Logging to a File
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
#                     format='%(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Start')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    logging.debug('End of factorial(%s)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')

# Don't Debug with the print() Function

# Logging Levels
# debug
# info
# warning
# error
# critical
logging.debug('Some debugging details')

logging.info('The logging module is working.')

logging.warning('An error message is about to be logged.')

logging.error('Ann error has occurred.')

logging.critical('The program is unable to recover!')

# Disabling Logging
logging.critical('Critical error! Critical error!')
# logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
