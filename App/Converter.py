class Converter:
    '''Az átváltandó érték'''
    __value: float
    '''Miről váltok'''
    __from_unit: str
    '''Mire váltok'''
    __to_unit: str
    '''Jelzi milyen mérétkegység csoportot kell figyelni | Távolság(Távolság) | Térfogat(Térfogat) | Súly(Tömeg) 
        A zárójelben jelzett Literálok a frontendben beégetett menüpontok.
    '''
    __pointer: str
    __Distance_data_table: dict = {"mm": 1, "cm": 10, "dm": 10**2, "m": 10**3, "km": 10**6, "miles": 1.6*10**6}
    __Volume_data_table: dict = {"ml": 1, "cl": 10, "dl": 10**2, "l": 10**3, "hl": 10**5, "m^3": 10**6}
    __Weight_data_table: dict = {"g": 1, "dkg": 10, "kg": 10**3, "t": 10*6}
    def __init__(self, value, from_unit, to_unit, pointer):
        self.__value = value
        self.__from_unit = from_unit
        self.__to_unit = to_unit
        self.__pointer = pointer
    def __Converter_logic(self, data_dict):
            decreaser = 0
            increaser = 0
            for k, v in data_dict.items():
                if k == self.__from_unit:
                    decreaser += v
                elif k == self.__to_unit:
                    increaser += v
            return self.__value * decreaser / increaser
    def Convert_unit(self):
        # Distance
        if self.__pointer == "Távolság":
            return self.__Converter_logic(self.__Distance_data_table)
        # Volume
        elif self.__pointer == "Térfogat":
            return self.__Converter_logic(self.__Volume_data_table)
        # Weight
        elif self.__pointer == "Tömeg":
            return self.__Converter_logic(self.__Weight_data_table)


#unit = Converter(1,"dl","l","V")
#unit.Convert_unit()


