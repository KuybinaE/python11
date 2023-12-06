from Models.Model import Model


# Подчинённый класс - класс в котром обрабатывается информация таблицы Climbers
class Climbers(Model):
    # приватное поле Имя Таблицы
    __nameTable = 'Climbers'
    __name = 'name'
    __address = 'address'
    # Метод вывода всех записей из таблицы
    def get(self):
        return super().get(self.__nameTable)

    # Метод вывода записей одного поля из таблицы
    def getOneField(self, field):
        return  super().getOneField(self.__nameTable, field)

    #  Добавить запись в таблицу
    def add(self):
        name = input("Введите имя: ")
        address = input("Введите адрес: ")
        str = f"{self.__name},{self.__address}"
        super().add(self.__nameTable,str,name,address)

    def delete(self, id):
        super().delete(self.__nameTable,id)

    def update(self):
        id = input("Введите id записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("введите новое занчение")
        super().update(self.__nameTable,id,field,values)

    #  метод вывода имён АЛЬПИНСТОВ в учавствующих в восхождении в определённый промежуток времени
    def getClimbersDateInterval(self, first_date, lost_date):
        return super().getClimbersDateInterval(first_date, lost_date)

    def getLastRow(self):
        return super().getLastRow(self.__nameTable)[0]

    def getOneRow(self,id):
        return super().getOneRow(self.__nameTable,id)