from Models.Ascents import Ascents

from Models.Climbers import Climbers
from Models.Model import Model
from Models.Regions import Regions


# Подчинённый класс - класс в котром обрабатывается информация таблицы Climbers
class Mountains(Model):
    # приватное поле Имя Таблицы
    __nameTable = 'Mountains'
    __name = 'name'
    __height = 'height'
    __region_id = 'region_id'
    # Метод вывода всех записей из таблицы
    def get(self):
        return super().get(self.__nameTable)

    # Метод вывода записей одного поля из таблицы
    def getOneField(self, field):
        return  super().getOneField(self.__nameTable, field)

    #  Добавить запись в таблицу
    def add(self):
        name = input("Введите назавание горы: ")
        height = input("Введите высоту: ")
        region_id = input("Введите id региона: ")
        str = f"{self.__name},{self.__height},{self.__region_id}"
        super().add(self.__nameTable,str,name,height,region_id)

    def delete(self, id):
        super().delete(self.__nameTable,id)

    def update(self):
        id = input("Введите id записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("введите новое значение")
        super().update(self.__nameTable,id,field,values)

    @property
    def getMountsClimbers(self):
        return super().getMountsClimbers()

#   Создание горы, высоты, региона и страны
    @property
    def addMountainAndRegion(self):
        name = input("Введите назавание горы: ")
        height = input("Введите высоту: ")

        region = Regions()
        region.add()

        region_id = region.getLastRow['id']

        str = f"{self.__name},{self.__height},{self.__region_id}"
        super().add(self.__nameTable, str, name, height, region_id)

    def updateWithoutAscents(self):
        id = input("Введите id ГОРЫ, которую хотите изменить ")
        field = input("Введите название поля тблицы (name или height) ")
        values = input("введите новое значение ")
        ascent = Ascents()
        flag = True
        for row, list in enumerate(ascent.get()):
            if str(list['mountain_id']) != id:
                flag = False
                break
        if flag:
            super().update(self.__nameTable, id, field, values)


    def getOneRow(self,id):
        return super().getOneRow(self.__nameTable,id)


