import sqlite3


class UsersDataBase:
    def __init__(self):
        self.conn = sqlite3.connect('timer.sqlite')
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS Users (
                            userID INTEGER PRIMARY KEY AUTOINCREMENT,
                            userName VARCHAR(50) UNIQUE)
                        """)

    def insert_user(self, userName):
        self.cur.execute("INSERT INTO Users (userName) VALUES (?)", [userName])
        self.conn.commit()

    def get_user_id(self, userName):
        result = self.cur.execute(
            "SELECT userID FROM Users WHERE userName = (?)", [userName])
        return list(result)[0][0]

    def list_user(self):
        results = self.cur.execute("SELECT * FROM Users")
        return results


class TimerDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(
            'timer.sqlite', timeout=5)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
                        CREATE TABLE IF NOT EXISTS TimerRecord (
                        points INTEGER,
                        time_spent INTEGER,
                        level INTEGER,
                        personID INTEGER,
                        dateAdded TEXT,
                        CONSTRAINT FK_TimerUser FOREIGN KEY (personID)
                        REFERENCES Users(userID))
                        """)

    def insert_record(self, personID, dateAdded, points, time_spent, level):
        print(personID, dateAdded, points, time_spent, level)
        self.cur.execute("INSERT INTO TimerRecord (personID, dateAdded, points, time_spent, level) VALUES (?,?,?,?,?)",
                         [personID, dateAdded, points, int(time_spent), level])
        self.conn.commit()

    def get_users_stats(self, personID):
        results = self.cur.execute(
            "SELECT * FROM TimerRecord WHERE personID = (?)", [personID])
        dataList = []
        for a in list(zip(*results)):
            dataList.append(a)

        return dataList[0], dataList[1], dataList[-1]

    def get_users_points_till_now(self, personID):
        results = self.cur.execute(
            "SELECT points FROM TimerRecord WHERE personID = (?)", [personID])

        points = []
        for point in results:
            points.append(point[0])

        return sum(points)

    def get_users_level(self, personID):
        try:
            results = self.cur.execute(
                "SELECT level FROM TimerRecord WHERE personID = (?) ORDER BY level DESC limit 1", [personID])

            return list(results)[0][0]
        except:
            return 0




def main():
    database1 = TimerDatabase()
    database1.create_table()


if __name__ == '__main__':
    main()
