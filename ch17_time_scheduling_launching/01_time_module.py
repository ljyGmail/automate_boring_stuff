# The time.time() Function
import time

print(f'time.time(): {time.time()}')

# profile code


def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(100000):
        product *= i
    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()
print(f'The result is {len(str(prod))} digits long.')
print(f'Took {endTime - startTime} seconds to calculate.')

# ctime() function
print(f'time.ctime(): {time.ctime()}')

thisMoment = time.time()
print(f'time.ctime(thisMoment): {time.ctime(thisMoment)}')

# The time.sleep() Function
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

# time.sleep(5)

# Rounding Numbers
now = time.time()
print(f'now: {now}')
print(f'round(now, 2): {round(now, 2)}')
print(f'round(now, 4): {round(now, 4)}')
print(f'round(now): {round(now)}')
