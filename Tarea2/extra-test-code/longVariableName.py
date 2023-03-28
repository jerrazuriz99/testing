class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.longnameforacar = dict()
        self.longnameforahouse = list()
        self.longnameforaperson = set()

    def newHouse(self, longnameforacar, longnameforahouse, longnameforaperson):
        self.longnameforacar = longnameforacar
        self.longnameforahouse = longnameforahouse
        self.longnameforaperson = longnameforaperson
