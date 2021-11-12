import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='NO SHIMA',
            passwd='17891881',
            database='Persons'
        )

        self.cursor = self.db.cursor(buffered=True)
        #self.cursor.execute("CREATE DATABASE IF NOT EXISTS Persons")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Person (name varchar(25), surname varchar(25), nickname varchar(25), password varchar(25), e_mail varchar(75), prediction_count smallint unsigned, personID INT AUTO_INCREMENT PRIMARY KEY)")
        self.prediction_count = int
        self.userId = int

    def add_person(self, name, surname, nickname, password, email, prediction_count):
        formula = "INSERT INTO person (name, surname, nickname, password, e_mail, prediction_count) VALUES (%s, %s, %s, %s, %s, %s)"
        person = (name, surname, nickname, password, email, prediction_count)
        self.cursor.execute(formula, person)
        self.db.commit()

    def getUsernames(self):
        self.cursor.execute("SELECT nickname FROM person")
        usernameList = []
        for username in self.cursor.fetchall():
            usernameList.append(username[0])
        return usernameList

    def getUserPass(self, username):
        self.cursor.execute(f"SELECT password FROM person WHERE nickname='{username}'")
        return self.cursor.fetchone()[0]

    def getName(self, username):
        self.cursor.execute(f"SELECT name FROM person WHERE nickname='{username}'")
        return self.cursor.fetchone()[0]

    def setUserId(self, username):
        self.cursor.execute(f"SELECT personID FROM person WHERE nickname='{username}'")
        self.userId = self.cursor.fetchone()[0]

    def getSurname(self, username):
        self.cursor.execute(f"SELECT surname FROM person WHERE nickname='{username}'")
        return self.cursor.fetchone()[0]

    def setPredictionCount(self, username):
        self.cursor.execute(f"SELECT prediction_count FROM person WHERE nickname='{username}'")
        self.prediction_count = self.cursor.fetchone()[0]

    def updatePredictionCount(self):
        formula = "UPDATE person SET prediction_count=%s WHERE personID=%s"
        self.cursor.execute(formula, (self.prediction_count, self.userId))
        self.db.commit()

    def get_emails(self):
        self.cursor.execute("SELECT e_mail FROM person")
        emailList = []
        for email in self.cursor.fetchall():
            emailList.append(email[0])
        return emailList