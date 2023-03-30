def example3(x, y, z):
  a = y + z
  c = z
  return a + c

def example4(a, b, c, d):
  x = a % b
  y = c - a
  return x + y

class Sport:
  def __init__(self, name, players):
    self.name = name
    self.players = players

  def change_players(self, ps):
    self.players = []

class Football(Sport):
  def __init__(self, name, players, teams):
    super().__init__(name, players)
    self.teams = teams

  def change_teams(self, ts):
    self.teams = []

