from Models.Ascents import Ascents
from Models.Climbers import Climbers
from Models.Model import Model
from Models.Mountains import Mountains


class AscentsClimbers(Model):
    __nameTable = 'Ascents_Climbers'
    __climber_id = 'climber_id'
    __ascent_id = 'ascent_id'
    def addAscentsClimber(self):
        ascent = Ascents()
        ascent.add()
        climber = Climbers()
        climber.add()
        str = f"{self.__ascent_id}, {self.__climber_id}"
        ascentId = ascent.getLastRow()
        climberId = climber.getLastRow()
        super().add(self.__nameTable,str, ascentId['id'], climberId['id'])

    def getOneRow(self,id):
        return super().getOneRow(self.__nameTable,id)

    def get(self):
        return super().get(self.__nameTable)

    def getClimbersNumberOfAscents(self):
        climber = Climbers()
        ascent = Ascents()
        mountain = Mountains()
        # список
        listMountain = list()
        for row, column in enumerate(self.get()):
            row+=1
            climberOn = climber.getOneRow(column['climber_id'])[0]
            ascentOn = ascent.getOneRow(column['ascent_id'])[0]
            mountainOn = mountain.getOneRow(ascentOn['mountain_id'])[0]
            # print(f"{row}) Восхождение: {mountainOn['name']}, Альпинист: {climberOn['name']}")
            listMountain.append(f"{climberOn['name']} - {mountainOn['name']}")
        for element in listMountain:
            print(element)

        print("------------------------------")
        # множество
        setMountain = set(listMountain)
        for element in setMountain:
            count = listMountain.count(element)
            print(f"{element} - {count}")

    def getCountOfClimbers2(self):
        ascent = Ascents()
        mountain = Mountains()

        # Список Гор которые покорили АЛЬПИНИСТЫ
        listMount = list()
        for row, column in enumerate(self.get()):
            row+=1
            ascentOn = ascent.getOneRow(column['ascent_id'])[0]
            mountainOn = mountain.getOneRow(ascentOn['mountain_id'])[0]
            print(f"{row}) Гора: {mountainOn['name']} - {column['climber_id']}")
            listMount.append(mountainOn['name'])
        print(listMount)

        # Множество
        for element in set(listMount):
            count = listMount.count(element)
            print(f"{element}: {count}")