ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)

assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
print(ages)

# assert ages[0] <= ages[-1], 'Assert that first first age is <= the last age.'

# Using an Assertion in a Traffic Light Simulation
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

    # assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)


switchLights(market_2nd)
