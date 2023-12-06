from Configuration.config import connection
# Супер класс для таблиц БД
class Model:

    # метод вывода данных из таблицы
    def get(self, table):
        with connection().cursor() as cursor:
            select_all_rows = f"SELECT * FROM {table}"
            cursor.execute(select_all_rows)
            return cursor.fetchall()
        connection().close()

    def getOneField(self,table, field):
        with connection().cursor() as cursor:
            select_one_field = f"SELECT {field} FROM {table}"
            cursor.execute(select_one_field)
            return cursor.fetchall()
        connection().close()
#     Добавить запись в таблицу
    def add(self, table, str, *values):
        with connection().cursor() as cursor:
            print(f"INSERT INTO {table} ({str}) VALUES {values}")
            query = f"INSERT INTO {table} ({str}) VALUES {values}"
            cursor.execute(query)
        connection().close()
        print(f"Новая запись в таблицу {table} добавлена")

# удаление записей
    def delete(self, table, id):
        with connection().cursor() as cursor:
            query_delete = f"DELETE FROM {table} WHERE id = {id}"
            cursor.execute(query_delete)
            connection().commit()
        connection().close()
        print("Запись удалена")

    def update(self, table, id, field, values):
        with connection().cursor() as cursor:
            # print(f"UPDATE {table} set {field} = '{values}' where id = {id}")
            query_update = f"UPDATE {table} SET {field} = '{values}' WHERE id = {id}"
            cursor.execute(query_update)
            connection().commit()
        connection().close()
        print("Запись обновлена")

#         Вывод одной записи
    def getOneRow(self,table,id):
        with connection().cursor() as cursor:
            query = f"SELECT * FROM {table} WHERE id = {id}"
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def getMountsClimbers(self):
        with connection().cursor() as cursor:
            query = ("select Climbers.name, Ascents.start_time,"
            + " (SELECT name from Mountains where id = Ascents.mountain_id) AS Mountain"
            +" from Ascents_Climbers"
            +" JOIN Ascents"
            +" ON Ascents_Climbers.ascent_id = Ascents.id"
            +" JOIN Climbers"
            +" ON Ascents_Climbers.climber_id = Climbers.id"
            + " ORDER BY Ascents.start_time")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def getLastRow(self,table):
        with connection().cursor() as cursor:
            query = f"SELECT * FROM {table} ORDER BY id DESC LIMIT 1"
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    # метод вывода имён АЛЬПИНСТОВ в учавствующих в восхождении в определённый промежуток времени
    def getClimbersDateInterval(self, first_date, lost_date):
        with connection().cursor() as cursor:
            # print(
            #         "SELECT Climbers.name, Ascents.start_time FROM Ascents_Climbers "
            #         + " JOIN Climbers ON Ascents_Climbers.climber_id = Climbers.id"
            #         + " JOIN Ascents ON Ascents_Climbers.ascent_id = Ascents.id"
            #         + f" WHERE Ascents.start_time BETWEEN '{first_date}' AND '{lost_date}'"
            # )
            query = (
                "SELECT Climbers.name, Ascents.start_time FROM Ascents_Climbers "
                + " JOIN Climbers ON Ascents_Climbers.climber_id = Climbers.id"
                + " JOIN Ascents ON Ascents_Climbers.ascent_id = Ascents.id"
                + f" WHERE Ascents.start_time BETWEEN '{first_date}' AND '{lost_date}'"
            )
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    #     Вывод количство восхождений альпистом на гору
    def numberOfAscents(self):
        print(
        "SELECT"
        + " Climbers.name, Mountains.name, COUNT(*)"
        + " AS"
        + " count"
        + " FROM"
        + " Ascents_Climbers, Climbers, Ascents, Mountains"
        + " WHERE"
        + " Ascents_Climbers.climber_id = Climbers.id"
        + " AND"
        + " Ascents_Climbers.ascent_id = Ascents.id"
        + " AND"
        + " Ascents.mountain_id = Mountains.id"
        + " GROUP"
        + " BY"
        + " Climbers.name, Mountains.name"
        )
        with connection().cursor() as cursor:
            query = (
                "SELECT"
                + " Climbers.name, Mountains.name, COUNT(*)"
                + " AS"
                + " count"
                + " FROM"
                + " Ascents_Climbers, Climbers, Ascents, Mountains"
                + " WHERE"
                + " Ascents_Climbers.climber_id = Climbers.id"
                + " AND"
                + " Ascents_Climbers.ascent_id = Ascents.id"
                + " AND"
                + " Ascents.mountain_id = Mountains.id"
                + " GROUP"
                + " BY"
                + " Climbers.name, Mountains.name"
            )
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    # Вывод количества альпинистов покоривших вершину
    def getNumberOfClimbers(self):
        print(
            "SELECT "
            + "Mountains.name, COUNT(*) "
            + "AS "
            + "countClimber "
            + "From "
            + "Mountains, Ascents, Ascents_Climbers, Climbers "
            + "WHERE "
            + "Mountains.id = Ascents.mountain_id "
            + "AND "
            + "Ascents.id = Ascents_Climbers.ascent_id "
            + "AND "
            + "Ascents_Climbers.climber_id = Climbers.id "
            + "GROUP "
            + "BY "
            + "Mountains.name "
        )
        with connection().cursor() as cursor:
            query = (
                    "SELECT "
                    + "Mountains.name, COUNT(*) "
                    + "AS "
                    + "countClimber "
                    + "From "
                    + "Mountains, Ascents, Ascents_Climbers, Climbers "
                    + "WHERE "
                    + "Mountains.id = Ascents.mountain_id "
                    + "AND "
                    + "Ascents.id = Ascents_Climbers.ascent_id "
                    + "AND "
                    + "Ascents_Climbers.climber_id = Climbers.id "
                    + "GROUP "
                    + "BY "
                    + "Mountains.name "
                    )
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

