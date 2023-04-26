import census2010

print(
    f"census2010.allData['AK']['Anchorage']: {census2010.allData['AK']['Anchorage']}")

anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print(f'The 2020 population of Anchorage was {anchoragePop}')
