from hypothesis import given
from hypothesis.strategies import dictionaries


def dictionary(keys, values):
  try:
    if type(keys) != list and type(values) != list:
      raise TypeError("is not a list")
  except TypeError as err:
    print("Input argument {} and {} {}".format(keys, values, err))
  else:
    diction = dict.fromkeys(keys, None)
    diction.update(zip(keys, values))
    print(diction)
    return diction


@given(dictionaries([1, 2, 3, 4], ['1', '2', '3']))
def test_dictionary(dicts):
    assert dictionary([1, 2, 3, 4], ['1', '2', '3']) == dicts

