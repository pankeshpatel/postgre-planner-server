from calculations import add


def test_add():
  print("Testing add function()....")
  sum = add(10, 20)
  assert sum == 30
  
  
