from Models.Model import Model


# Подчинённый класс - класс в котром обрабатывается информация таблицы Climbers
class Ascents(Model):
    # приватное поле Имя Таблицы
    __nameTable = 'Ascents'
    __name = 'name'
    __start_time = 'start_time'
    __finish_time = 'finish_time'
    __mountain_id = 'mountain_id'
    # Метод вывода всех записей из таблицы
    def get(self):
        return super().get(self.__nameTable)

    # Метод вывода записей одного поля из таблицы
    def getOneField(self, field):
        return  super().getOneField(self.__nameTable, field)

    #  Добавить запись в таблицу
    def add(self):
        name = input("Введите название восхождения: ")
        start_time = input("Введите начало восхождения: ")
        finish_time = input("Введите окончание восхождения: ")
        mount_id = input("Введите id горы: ")
        str = f"{self.__name},{self.__start_time}, {self.__finish_time}, {self.__mountain_id}"
        super().add(self.__nameTable,str,name,start_time, finish_time, int(mount_id))

    def delete(self, id):
        super().delete(self.__nameTable,id)

    def update(self):
        id = input("Введите id записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("введите новое занчение")
        super().update(self.__nameTable,id,field,values)

    def getOneRow(self,id):
        return super().getOneRow(self.__nameTable,id)

    def getLastRow(self):
        return super().getLastRow(self.__nameTable)[0]
