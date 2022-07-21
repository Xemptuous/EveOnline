class Ore(dict):
    typeID: int
    compressedID: int
    volume: float
    bonus: float
    minerals: dict
    askPrice: float
    bidPrice: float

class Mineral(dict):
    typeID: int
    bidPrice: float
    askPrice: float
