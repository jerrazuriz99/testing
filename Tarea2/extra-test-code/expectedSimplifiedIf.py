def example3(x, y, z):
  a = y + z
  c = z
  return a + c > x

def example4(a, b, c, d):
  x = a % b
  y = c - a
  return not (x + y > d)

def example5(a, b, c, d, e, f):
  x = a % b
  y = c - a
  z = d - c
  return not (x + y + z > e + f)