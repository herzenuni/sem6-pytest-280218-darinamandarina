"""testing with assert"""

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
dictionaryAssertion(keysList,valuesList)
dictionaryAssertion(('this','is', 'tuple'),9)
#dictionaryAssertion()
