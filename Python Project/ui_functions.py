from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QCursor
from PyQt5.QtWidgets import QCheckBox, QGraphicsDropShadowEffect, QLineEdit, QMessageBox, QSizeGrip
from PyQt5.QtWidgets import QMainWindow
from main import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from database import Database
# Importing our model from model.py
from model import Model

GLOBAL_STATE = 0


class UIFunctions(QMainWindow):

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()

            GLOBAL_STATE = 1

            self.ui.dropShadowFrame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.134576 rgba(63, 69, 150, 255), stop:0.708075 rgba(33, 28, 107, 255));\n"
                                                  "border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")

        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.size().width(), self.size().height())
            self.ui.dropShadowFrame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.134576 rgba(63, 69, 150, 255), stop:0.708075 rgba(33, 28, 107, 255));\n"
                                                  "border-radius: 10px;")
            self.ui.btn_maximize.setToolTip("Maximize")

    def uiDefinitions(self):
        self.database = Database()
        self.model = Model()
        self.model.initialize_model()
        self.player = QMediaPlayer()
        self.sound = str

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(
            lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: UIFunctions.exitPopUp(self))

        self.ui.login_button_2.clicked.connect(lambda: UIFunctions.login(self))
        self.ui.register_button.clicked.connect(
            lambda: UIFunctions.pageRegister(self))
        self.ui.register_button_2.clicked.connect(
            lambda: UIFunctions.addToDatabase(self))
        self.ui.back_button.clicked.connect(lambda: UIFunctions.backward(self))
        self.ui.back_button_2.clicked.connect(
            lambda: UIFunctions.backward(self))
        self.ui.login_button.clicked.connect(
            lambda: UIFunctions.pageLogin(self))
        self.ui.predict_button.clicked.connect(lambda: UIFunctions.predict(self))
        self.ui.predict_button.clicked.connect(lambda: UIFunctions.play(self, self.sound))
        self.ui.clear_button.clicked.connect(lambda: UIFunctions.clearTextEdit(self))

        self.ui.nickname_line_login.textChanged.connect(lambda: UIFunctions.onTexting6(self))
        self.ui.passw_line_login.textChanged.connect(lambda: UIFunctions.onTexting7(self))
        self.ui.news_text.textChanged.connect(lambda: UIFunctions.onTexting8(self))
        self.ui.name_line.textChanged.connect(
            lambda: UIFunctions.onTexting4(self))
        self.ui.surname_line.textChanged.connect(
            lambda: UIFunctions.onTexting2(self))
        self.ui.passw_line_register.textChanged.connect(
            lambda: UIFunctions.onTexting5(self))
        self.ui.nickname_line_register.textChanged.connect(
            lambda: UIFunctions.onTexting3(self))
        self.ui.checkbox.stateChanged.connect(lambda: UIFunctions.check(self, self.ui.checkbox, self.ui.passw_line_register))
        self.ui.checkbox_login.stateChanged.connect(lambda: UIFunctions.check(self, self.ui.checkbox_login, self.ui.passw_line_login))
        self.ui.mail_line.textChanged.connect(
            lambda: UIFunctions.onTexting(self))
        
        self.ui.exit_button.clicked.connect(lambda: UIFunctions.exitPopUp(self))
        self.ui.exit_button_2.clicked.connect(lambda: UIFunctions.exitPopUp(self))

        # ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet(
            "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

    def check(self, checkbox:QCheckBox, line:QLineEdit):
        if checkbox.isChecked():
            line.setEchoMode(QLineEdit.EchoMode.Normal)

        else:
            line.setEchoMode(
                QLineEdit.EchoMode.Password)

    def onTexting(self):
        mails = ["@hotmail.com", "@gmail.com", "@outlook.com", "@yahoo.com"]
        if len(self.ui.mail_line.text()) == 0:
            self.ui.mail_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                            "border: 2.7px solid  rgb(255, 0, 0);")
            self.ui.mail_warning.setHidden(True)

        else:
            if "'" in self.ui.mail_line.text() or '"' in self.ui.mail_line.text() or '=' in self.ui.mail_line.text() or all(i not in self.ui.mail_line.text() for i in mails) or not (self.ui.mail_line.text().endswith(".com")):
                self.ui.mail_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                "border: 2.7px solid  rgb(255, 0, 0);")
                self.ui.mail_warning.setHidden(False)

            else:
                self.ui.mail_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                "border: 2.7px solid  rgb(192, 192, 192);")
                self.ui.mail_warning.setHidden(True)

        UIFunctions.register_button_state(self)

    def onTexting2(self):
        invalidCharacters = """@_,.'()?/%^! $½#+£><"-*[]="""

        if len(self.ui.surname_line.text()) == 0:
            self.ui.surname_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                               "border: 2.7px solid  rgb(255, 0, 0);")
            self.ui.surname_warning.setHidden(True)

        else:
            check = any([i in self.ui.surname_line.text()
                         for i in invalidCharacters])

            if check:
                self.ui.surname_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                   "border: 2.7px solid  rgb(255, 0, 0);")
                self.ui.surname_warning.setHidden(False)

            else:
                self.ui.surname_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                   "border: 2.7px solid  rgb(192, 192, 192);")
                self.ui.surname_warning.setHidden(True)

        UIFunctions.register_button_state(self)

    def onTexting3(self):
        invalidCharacters = """@_,'()?/%^! $½#+£><"-*[]="""

        if len(self.ui.nickname_line_register.text()) == 0:
            self.ui.nickname_line_register.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                         "border: 2.7px solid  rgb(255, 0, 0);")
            self.ui.nickname_warning.setHidden(True)

        else:
            check = any([i in self.ui.nickname_line_register.text()
                         for i in invalidCharacters])

            if check:
                self.ui.nickname_line_register.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                             "border: 2.7px solid  rgb(255, 0, 0);")
                self.ui.nickname_warning.setHidden(False)

            else:
                self.ui.nickname_line_register.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                             "border: 2.7px solid  rgb(192, 192, 192);")
                self.ui.nickname_warning.setHidden(True)

        UIFunctions.register_button_state(self)

    def onTexting4(self):
        invalidCharacters = """@_,.'()?/%^! $½#+£><"-*[]="""

        if len(self.ui.name_line.text()) == 0:
            self.ui.name_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                            "border: 2.7px solid  rgb(255, 0, 0);")
            self.ui.name_warning.setHidden(True)

        else:
            check = any([i in self.ui.name_line.text()
                         for i in invalidCharacters])

            if check:
                self.ui.name_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                "border: 2.7px solid  rgb(255, 0, 0);")
                self.ui.name_warning.setHidden(False)

            else:
                self.ui.name_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                "border: 2.7px solid  rgb(192, 192, 192);")
                self.ui.name_warning.setHidden(True)

        UIFunctions.register_button_state(self)

    def onTexting5(self):
        if len(self.ui.passw_line_register.text()) == 0:
            self.ui.passw_line_register.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                      "border: 2.7px solid  rgb(255, 0, 0);")
            self.ui.password_warning.setHidden(True)

        elif "'" in self.ui.passw_line_register.text() or '"' in self.ui.passw_line_register.text() or "=" in self.ui.passw_line_register.text():
            self.ui.passw_line_register.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                      "border: 2.7px solid  rgb(255, 0, 0);")
            self.ui.password_warning.setHidden(False)

        else:
            self.ui.passw_line_register.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                      "border: 2.7px solid  rgb(192, 192, 192);")
            self.ui.password_warning.setHidden(True)

        UIFunctions.register_button_state(self)

    def onTexting6(self):
        invalidCharacters = """@_,'()?/%^! $½#+£><"-*[]="""

        if len(self.ui.nickname_line_login.text()) == 0:
            self.ui.nickname_line_login.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                         "border: 2.7px solid  rgb(255, 0, 0);\n"
                                                         "border-radius: 10px;")
            self.ui.nickname_warning_login.setHidden(True)

        else:
            check = any([i in self.ui.nickname_line_login.text()
                         for i in invalidCharacters])

            if check:
                self.ui.nickname_line_login.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                         "border: 2.7px solid  rgb(255, 0, 0);\n"
                                                         "border-radius: 10px;")
                self.ui.nickname_warning_login.setHidden(False)

            else:
                self.ui.nickname_line_login.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                         "border: 2.7px solid  rgb(192, 192, 192);\n"
                                                         "border-radius: 10px;")
                self.ui.nickname_warning_login.setHidden(True)

        UIFunctions.login_button_state(self)

    def onTexting7(self):
        if len(self.ui.passw_line_login.text()) == 0:
            self.ui.passw_line_login.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                      "border: 2.7px solid  rgb(255, 0, 0);\n"
                                                      "border-radius: 10px;")
            self.ui.password_warning_login.setHidden(True)

        elif "'" in self.ui.passw_line_login.text() or '"' in self.ui.passw_line_login.text() or "=" in self.ui.passw_line_login.text():
            self.ui.passw_line_login.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                      "border: 2.7px solid  rgb(255, 0, 0);\n"
                                                      "border-radius: 10px;")
            self.ui.password_warning_login.setHidden(False)

        else:
            self.ui.passw_line_login.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                      "border: 2.7px solid  rgb(192, 192, 192);\n"
                                                      "border-radius: 10px;")
            self.ui.password_warning_login.setHidden(True)

        UIFunctions.login_button_state(self)

    def onTexting8(self):
        if len(self.ui.news_text.toPlainText()) == 0 or self.ui.news_text.toPlainText().isspace():
            self.ui.news_text.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                      "border: 2.7px solid  rgb(255, 0, 0);\n"
                                                      "border-radius: 10px;")

            self.ui.predict_button.setEnabled(False)
            self.ui.predict_button.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(224, 224, 224);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(0, 0, 0);")
            self.ui.predict_button.setCursor(QCursor(QtCore.Qt.ArrowCursor))

        else:
            self.ui.news_text.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                      "border: 2.7px solid  rgb(192, 192, 192);\n"
                                                      "border-radius: 10px;")

            self.ui.predict_button.setEnabled(True)
            self.ui.predict_button.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(64, 64, 64);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(255, 255, 255);")
            self.ui.predict_button.setCursor(
                QCursor(QtCore.Qt.PointingHandCursor))

        UIFunctions.clear_button_state(self)

    def clear_button_state(self):
        if len(self.ui.news_text.toPlainText()) != 0:
            self.ui.clear_button.setEnabled(True)
            self.ui.clear_button.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(64, 64, 64);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(255, 255, 255);")
            self.ui.clear_button.setCursor(
                QCursor(QtCore.Qt.PointingHandCursor))

        else:
            self.ui.clear_button.setEnabled(False)
            self.ui.clear_button.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(224, 224, 224);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(0, 0, 0);")
            self.ui.clear_button.setCursor(QCursor(QtCore.Qt.ArrowCursor))
    
    def login_button_state(self):
        if self.ui.nickname_warning_login.isVisible() or len(self.ui.nickname_line_login.text()) == 0 or len(self.ui.passw_line_login.text()) == 0 or self.ui.password_warning_login.isVisible():
            self.ui.login_button_2.setEnabled(False)
            self.ui.login_button_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(224, 224, 224);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(0, 0, 0);")
            self.ui.login_button_2.setCursor(QCursor(QtCore.Qt.ArrowCursor))

        else:
            self.ui.login_button_2.setEnabled(True)
            self.ui.login_button_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(64, 64, 64);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(255, 255, 255);")
            self.ui.login_button_2.setCursor(
                QCursor(QtCore.Qt.PointingHandCursor))

    def login(self):
        usernames = self.database.getUsernames()
        username = self.ui.nickname_line_login.text()
        password = self.ui.passw_line_login.text()

        if username in usernames:
            userPass = self.database.getUserPass(username)
            if userPass == password:
                UIFunctions.logged_in_success(self)
                UIFunctions.home(self, username)
                UIFunctions.pageHome(self)

            else:
                UIFunctions.error(self, "Username or password is incorrect.")

        else:
            UIFunctions.error(self, "There is not any registered account with these informations.")

    def pageRegister(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def pageLogin(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def pageHome(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def home(self, username:str):
        name = self.database.getName(username)
        surname = self.database.getSurname(username)
        self.database.setPredictionCount(username)
        self.database.setUserId(username)

        self.ui.name_home.setText(name)
        self.ui.surname_home.setText(surname)
        self.ui.prediction_number.setText(str(self.database.prediction_count))

    def logged_in_success(self):
        CHECKMARK = "icons/checkmark.png"
        msg = QMessageBox()
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setWindowIcon(QtGui.QIcon(
            CHECKMARK))
        msg.setWindowTitle("Successfully logged in!")
        msg.setText("You're being redirected to the home page.")
        msg.exec_()

    def register_button_state(self):
        labels = [self.ui.name_warning, self.ui.surname_warning,
                  self.ui.nickname_warning, self.ui.mail_warning, self.ui.password_warning]

        if any([i.isVisible() for i in labels]) or len(self.ui.mail_line.text()) == 0 or len(self.ui.nickname_line_register.text()) == 0 or len(self.ui.passw_line_register.text()) == 0 or len(self.ui.name_line.text()) == 0 or len(self.ui.surname_line.text()) == 0:
            self.ui.register_button_2.setEnabled(False)
            self.ui.register_button_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(224, 224, 224);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(0, 0, 0);")
            self.ui.register_button_2.setCursor(QCursor(QtCore.Qt.ArrowCursor))

        else:
            self.ui.register_button_2.setEnabled(True)
            self.ui.register_button_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(64, 64, 64);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(255, 255, 255);")
            self.ui.register_button_2.setCursor(
                QCursor(QtCore.Qt.PointingHandCursor))

    def addToDatabase(self):
        name = self.ui.name_line.text()
        surname = self.ui.surname_line.text()
        nickname = self.ui.nickname_line_register.text()
        password = self.ui.passw_line_register.text()
        e_mail = self.ui.mail_line.text()
        username = self.database.getUsernames()
        user_email = self.database.get_emails()
        check_username = 0
        check_email = 0
            
        if nickname in username:
            check_username = 1

        if e_mail in user_email:
            check_email = 1

        if check_email == 0 and check_username == 0:
            try:
                self.database.add_person(
                    name, surname, nickname, password, e_mail, 0)
                UIFunctions.registered_successfully(self)
                UIFunctions.clear_register_page(self)

            except Exception as e:
                UIFunctions.error(self, "Unfortunately, registration failed.")


        else:
            if check_email == 1 and check_username == 0:
                UIFunctions.error(self, "This e-mail has been used by someone else.")

            elif check_email == 0 and check_username == 1:
                UIFunctions.error(self, "This username has been used by someone else.")

            else:
                UIFunctions.error(self, "There is an account which has been created with these informations.")

    def registered_successfully(self):
        CHECKMARK = "icons/checkmark.png"
        msg = QMessageBox()
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setWindowIcon(QtGui.QIcon(
            CHECKMARK))
        msg.setWindowTitle("Successfully registered!")
        msg.setText("Your account has been created successfully.")
        msg.exec_()

    def clearTextEdit(self):
        self.ui.forecast_label.setText("")
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.news_text.setPlainText("")

    def error(self, message):
        CROSSICON = "icons/crossmark.png"
        msg = QMessageBox()
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setWindowIcon(QtGui.QIcon(
            CROSSICON))
        msg.setWindowTitle("An error occurred !")
        msg.setText(message)
        msg.exec_()

    def exitPopUp(self):
        choice = QMessageBox.question(self, "Exit", "Are you sure you want to quit ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes,)

        if choice == QMessageBox.Yes:
            UIFunctions.exit_program(self)

    def exit_program(self):
        try:
            self.database.updatePredictionCount()
        except Exception as e:
            pass
        
        finally:
            self.close()

    def play(self, sound):
        url = QtCore.QUrl.fromLocalFile(sound)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()


    def predict(self):
        news_text = self.ui.news_text.toPlainText()
        news_text = news_text.strip()
        category = self.model.forecast(news_text)
        widgetIndex = int

        if category == 'b':
            category = "Business"
            self.sound = "sounds/business.mp3"
            widgetIndex = 5

        elif category == 'c':
            category = "Crime"
            self.sound = "sounds/crime.mp3"
            widgetIndex = 2

        elif category == 'e':
            category = "Entertainment"
            self.sound = "sounds/entertainment.mp3"
            widgetIndex = 4

        elif category == 's':
            category = "Sport"
            self.sound = "sounds/sport.mp3"
            widgetIndex = 1

        elif category == 'p':
            category = "Politics"
            self.sound = "sounds/politics.mp3"
            widgetIndex = 7

        elif category == 'm':
            category = "Health"
            self.sound = "sounds/health.mp3"
            widgetIndex = 6

        elif category == 't':
            category = "Tech and Science"
            self.sound = "sounds/tech_science.mp3"
            widgetIndex = 3

        self.ui.forecast_label.setText(category)
        self.ui.stackedWidget_2.setCurrentIndex(widgetIndex)
        self.database.prediction_count += 1
        self.ui.prediction_number.setText(str(self.database.prediction_count))

    def clear_register_page(self):
        self.ui.name_line.clear()
        self.ui.surname_line.clear()
        self.ui.nickname_line_register.clear()
        self.ui.passw_line_register.clear()
        self.ui.mail_line.clear()
        self.ui.checkbox.setChecked(False)
        self.ui.name_warning.setHidden(True)
        self.ui.surname_warning.setHidden(True)
        self.ui.mail_warning.setHidden(True)
        self.ui.nickname_warning.setHidden(True)
        self.ui.name_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                        "border: 2.7px solid  rgb(192, 192, 192);")
        self.ui.surname_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                           "border: 2.7px solid  rgb(192, 192, 192);")
        self.ui.nickname_line_register.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                     "border: 2.7px solid  rgb(192, 192, 192);")
        self.ui.passw_line_register.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                                  "border: 2.7px solid  rgb(192, 192, 192);")
        self.ui.mail_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                        "border: 2.7px solid  rgb(192, 192, 192);")

    def clear_login_page(self):
        self.ui.nickname_line_login.clear()
        self.ui.passw_line_login.clear()
        self.ui.checkbox_login.setChecked(False)
        self.ui.nickname_warning_login.setHidden(True)
        self.ui.nickname_line_login.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                        "border: 2.7px solid  rgb(192, 192, 192);\n"
                                        "border-radius: 10px;")
        self.ui.passw_line_login.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                           "border: 2.7px solid  rgb(192, 192, 192);\n"
                                           "border-radius: 10px;")
    def backward(self):
        if self.ui.stackedWidget.currentIndex() == 1:
            self.ui.stackedWidget.setCurrentIndex(0)
            UIFunctions.clear_register_page(self)

        elif self.ui.stackedWidget.currentIndex() == 2:
            self.ui.stackedWidget.setCurrentIndex(0)
            UIFunctions.clear_login_page(self)

    def returnStatus():
        return GLOBAL_STATE
