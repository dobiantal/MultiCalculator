class Converter:
    value: float
    def __init__(self, value):
        self.value = value
    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, v: float):
        if v > 0:
            self.value = v
        else:
            raise ValueError("The convertation value must be higher then 0")
    #Distance


    #Volume

