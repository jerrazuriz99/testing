def example3(x, y, z):
  a = y + z
  c = z
  return True if a + c > x else False

def example4(a, b, c, d):
  x = a % b
  y = c - a
  return False if x + y > d else True

def example5(a, b, c, d, e, f):
  x = a % b
  y = c - a
  z = d - c
  return False if x + y + z > e + f else True