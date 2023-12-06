from Models.Model import Model


# Подчинённый класс - класс в котром обрабатывается информация таблицы Climbers
class Regions(Model):
    # приватное поле Имя Таблицы
    __nameTable = 'Regons'
    __country = 'country'
    __region = 'region'

    # Метод вывода всех записей из таблицы
    def get(self):
        return super().get(self.__nameTable)

    # Метод вывода записей одного поля из таблицы
    def getOneField(self, field):
        return  super().getOneField(self.__nameTable, field)

    #  Добавить запись в таблицу
    def add(self):
        country = input("Введите назавание страны: ")
        region = input("Введите название региона: ")
        str = f"{self.__country},{self.__region}"
        super().add(self.__nameTable,str,country,region)

    def delete(self, id):
        super().delete(self.__nameTable,id)

    def update(self):
        id = input("Введите id записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("введите новое занчение")
        super().update(self.__nameTable,id,field,values)
    def getOneRow(self,id):
        if super().getOneRow(self.__nameTable,id) != ():
            return super().getOneRow(self.__nameTable,id)[0]

    @property
    def getLastRow(self):
        return super().getLastRow(self.__nameTable)[0]