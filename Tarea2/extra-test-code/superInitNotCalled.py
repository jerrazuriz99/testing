class Sport:

  def __init__(self, name, players):
    self.name = name
    self.players = players

  def change_players(self, ps):
    self.players = []

class Football(Sport):
  
  def __init__(self):
    print("Juego futbol")

  def change_players(self, ps):
    self.players = []
    print("Cambio de jugadores")

class Basketball(Sport):
    
    def __init__(self):
      super(Basketball, self).__init__("basketball", [])
      print("Juego baloncesto")

class Futsal(Football):
  
  def __init__(self):
    print("Juego futsal")


