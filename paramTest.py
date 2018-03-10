import pytest
"""at first we should write a test with assert"""

def dictionaryAssertion(keys, values):
  try:
    if type(keys)!=list and type(values)!=list:
      raise TypeError("is not a list")
  except TypeError as err:
    print("Input argument {} and {} {}".format(keys,values, err))
  else:
    dictionary = dict.fromkeys(keys, None)
    dictionary.update(zip(keys, values))
    print(dictionary)
    return dictionary
    

keysList = [1,2,3,4]
valuesList = ['1','2','3']
expectedDict = {1: '1', 2: '2', 3: '3', 4: None}

"""parametrizing test"""
@pytest.mark.parametrize("keys,values,expected", [
    (keysList, valuesList, expectedDict),
    (keysList, valuesList, None),
    (keysList, 0, {1:0})])

def testDictionaryAssertion(keys, values, expected):
  assert dictionaryAssertion(keys,values) == expected