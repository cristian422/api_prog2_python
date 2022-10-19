from model.kidDTO import KidByPositionDTO
from model.kid import Kid
from model.list_se import ListSE

class ListSEService:
    def __init__(self):
        self.list= ListSE()
        #mosquera = Kid("123456","Jeronimo Mosquera",4,"M")
        sara = Kid({"identification": "434343", "name": "Sara", "age": 5, "gender": "F"})
        self.list.add(sara)
        mosquera = Kid({"identification":"123456","name":"Jeronimo Mosquera","age":4,"gender":"M"})
        self.list.add(mosquera)
        murillo = Kid({"identification":"654321","name":"Jeronimo Murillo","age":5,"gender":"M"})
        self.list.add(murillo)


    def add_kid(self,data):
        #Aca irian las validaciones del dict
        if "age" in data:
            if data['age'] > 0:
                self.list.add(Kid(data))
                return "Kid adicionado exitosamente"
            else:
                return "La edad debe ser positiva"
        else:
            return "Atributo age no encontrado"


    def add_by_position(self,kidByPositionDTO:KidByPositionDTO):
        if kidByPositionDTO.position > 0 and kidByPositionDTO.position <= (self.list.size +1):
            self.list.add_by_position(kidByPositionDTO.position,kidByPositionDTO.kid)
            return "Adicionado exitosamente"
        else:
            return "Posición no permitida"

    def mix_by_gender(self):
        self.list.mix_by_gender()
        return "Se ha ejecutado la mezcla"

    def invert(self):
        self.list.invert()
        return "listo"

    def mix_by_gender(self):
        self.list.mix_by_gender()
        return "listo"
    def firs_and_last(self):
        self.list.firs_and_last()
        return "listo"
    def count(self):
        self.list.count()
        return "listo"
    def male_female(self):
        self.list.male_female()
        return "listo"
    def delet_position(self,i:int):
        self.list.delet_position(i)
        return "listo"
    def less_7_years(self):
        self.list.less_7_years()
        return "listo"
    def delet_3years_kids(self):
        self.list.delet_3years_kids()
        return "listo"
