from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1135, 796)
        MainWindow.setMinimumSize(QtCore.QSize(1102, 779))
        MainWindow.setStyleSheet("background-color: rgb(84, 90, 200);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.134576 rgba(63, 69, 150, 255), stop:0.708075 rgba(33, 28, 107, 255));\n"
"border-radius: 10px;")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_bar = QtWidgets.QFrame(self.dropShadowFrame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color:none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(60, 231, 195);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_3.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title)
        self.frame_btns = QtWidgets.QFrame(self.title_bar)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"border: none;\n"
"border-radius: 8px;\n"
"background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_5.addWidget(self.btn_maximize)
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"border: none;\n"
"border-radius: 8px;\n"
"background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 170, 0, 150);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_5.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setStyleSheet("QPushButton {\n"
"border: none;\n"
"border-radius: 8px;\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_5.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.title_bar)
        self.content_bar = QtWidgets.QFrame(self.dropShadowFrame)
        self.content_bar.setStyleSheet("background-color:none;")
        self.content_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content_bar)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content_bar)
        self.stackedWidget.setMaximumSize(QtCore.QSize(1041, 605))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.menu_page = QtWidgets.QWidget()
        self.menu_page.setObjectName("menu_page")
        self.frame_8 = QtWidgets.QFrame(self.menu_page)
        self.frame_8.setGeometry(QtCore.QRect(310, 80, 450, 450))
        self.frame_8.setMinimumSize(QtCore.QSize(450, 450))
        self.frame_8.setMaximumSize(QtCore.QSize(450, 450))
        self.frame_8.setStyleSheet("QFrame {\n"
"border: 5px solid rgb(60, 231, 195);\n"
"background-color: rgb(240, 233, 219);\n"
"border-radius: 125px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"border-color: rgb(105, 95, 140);\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.login_button = QtWidgets.QPushButton(self.frame_8)
        self.login_button.setGeometry(QtCore.QRect(140, 80, 181, 41))
        self.login_button.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(64, 64, 64);\n"
"                                        border-style:outlet;\n"
"                                        border-width:2px;\n"
"                                        border-radius:10px;\n"
"                                        border-color: rgb(255, 255, 255);")
        self.login_button.setObjectName("login_button")
        self.register_button = QtWidgets.QPushButton(self.frame_8)
        self.register_button.setGeometry(QtCore.QRect(140, 215, 181, 41))
        self.register_button.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(64, 64, 64);\n"
"                                        border-style:outlet;\n"
"                                        border-width:2px;\n"
"                                        border-radius:10px;\n"
"                                        border-color: rgb(255, 255, 255);")
        self.register_button.setObjectName("register_button")
        self.exit_button = QtWidgets.QPushButton(self.frame_8)
        self.exit_button.setGeometry(QtCore.QRect(140, 350, 181, 41))
        self.exit_button.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(64, 64, 64);\n"
"                                        border-style:outlet;\n"
"                                        border-width:2px;\n"
"                                        border-radius:10px;\n"
"                                        border-color: rgb(255, 255, 255);")
        self.exit_button.setObjectName("exit_button")
        self.label_14 = QtWidgets.QLabel(self.menu_page)
        self.label_14.setGeometry(QtCore.QRect(-90, 70, 391, 551))
        self.label_14.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_14.setStyleSheet("background-image: url(:/gif/newspaper-2.png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.menu_page)
        self.label_15.setGeometry(QtCore.QRect(760, 30, 321, 551))
        self.label_15.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_15.setStyleSheet("")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/gif/newspaper.gif"))
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.menu_page)
        self.register_page = QtWidgets.QWidget()
        self.register_page.setObjectName("register_page")
        self.name_line = QtWidgets.QLineEdit(self.register_page)
        self.name_line.setGeometry(QtCore.QRect(320, 110, 181, 31))
        self.name_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"border: 2.7px solid  rgb(192, 192, 192);")
        self.name_line.setText("")
        self.name_line.setObjectName("name_line")
        self.name_line.setMaxLength(25)
        self.surname_line = QtWidgets.QLineEdit(self.register_page)
        self.surname_line.setGeometry(QtCore.QRect(620, 110, 181, 31))
        self.surname_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"border: 2.7px solid  rgb(192, 192, 192);")
        self.surname_line.setObjectName("surname_line")
        self.surname_line.setMaxLength(25)
        self.nickname_line_register = QtWidgets.QLineEdit(self.register_page)
        self.nickname_line_register.setGeometry(QtCore.QRect(120, 210, 181, 31))
        self.nickname_line_register.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"border: 2.7px solid  rgb(192, 192, 192);")
        self.nickname_line_register.setObjectName("nickname_line_register")
        self.nickname_line_register.setMaxLength(25)
        self.passw_line_register = QtWidgets.QLineEdit(self.register_page)
        self.passw_line_register.setGeometry(QtCore.QRect(120, 320, 181, 31))
        self.passw_line_register.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"border: 2.7px solid  rgb(192, 192, 192);")
        self.passw_line_register.setObjectName("passw_line_register")
        self.passw_line_register.setMaxLength(25)
        self.passw_line_register.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.mail_line = QtWidgets.QLineEdit(self.register_page)
        self.mail_line.setGeometry(QtCore.QRect(120, 440, 181, 31))
        self.mail_line.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"border: 2.7px solid  rgb(192, 192, 192);")
        self.mail_line.setObjectName("mail_line")
        self.mail_line.setMaxLength(75)
        self.register_button_2 = QtWidgets.QPushButton(self.register_page)
        self.register_button_2.setGeometry(QtCore.QRect(280, 560, 181, 41))
        self.register_button_2.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(64, 64, 64);\n"
"                                        border-style:outlet;\n"
"                                        border-width:2px;\n"
"                                        border-radius:10px;\n"
"                                        border-color: rgb(255, 255, 255);")
        self.register_button_2.setObjectName("register_button_2")
        self.back_button = QtWidgets.QPushButton(self.register_page)
        self.back_button.setGeometry(QtCore.QRect(590, 560, 181, 41))
        self.back_button.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(64, 64, 64);\n"
"                                        border-style:outlet;\n"
"                                        border-width:2px;\n"
"                                        border-radius:10px;\n"
"                                        border-color: rgb(255, 255, 255);")
        self.back_button.setObjectName("back_button")
        self.label = QtWidgets.QLabel(self.register_page)
        self.label.setGeometry(QtCore.QRect(330, 85, 47, 16))
        self.label.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.register_page)
        self.label_2.setGeometry(QtCore.QRect(625, 85, 61, 21))
        self.label_2.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.register_page)
        self.label_3.setGeometry(QtCore.QRect(125, 185, 111, 21))
        self.label_3.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.register_page)
        self.label_4.setGeometry(QtCore.QRect(125, 296, 51, 20))
        self.label_4.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.register_page)
        self.label_5.setGeometry(QtCore.QRect(125, 418, 61, 16))
        self.label_5.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.checkbox = QtWidgets.QCheckBox(self.register_page)
        self.checkbox.setGeometry(QtCore.QRect(310, 327, 131, 19))
        self.checkbox.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 255, 255);")
        self.name_warning = QtWidgets.QLabel(self.register_page)
        self.name_warning.setGeometry(QtCore.QRect(330, 143, 191, 16))
        self.name_warning.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(242, 79, 128);")
        self.surname_warning = QtWidgets.QLabel(self.register_page)
        self.surname_warning.setGeometry(QtCore.QRect(620, 143, 191, 16))
        self.surname_warning.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(242, 79, 128);")
        self.nickname_warning = QtWidgets.QLabel(self.register_page)
        self.nickname_warning.setGeometry(QtCore.QRect(70, 240, 291, 16))
        self.nickname_warning.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(242, 79, 128);")
        self.mail_warning = QtWidgets.QLabel(self.register_page)
        self.mail_warning.setGeometry(QtCore.QRect(110, 472, 191, 16))
        self.mail_warning.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(242, 79, 128);")
        self.mail_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.password_warning = QtWidgets.QLabel(self.register_page)
        self.password_warning.setGeometry(QtCore.QRect(117, 355, 191, 16))
        self.password_warning.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(242, 79, 128);")
        self.password_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.stackedWidget.addWidget(self.register_page)
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.login_page)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame = QtWidgets.QFrame(self.login_page)
        self.frame.setMinimumSize(QtCore.QSize(575, 575))
        self.frame.setMaximumSize(QtCore.QSize(575, 575))
        self.frame.setStyleSheet("border: 5px;\n"
"border-radius: 125px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nickname_line_login = QtWidgets.QLineEdit(self.frame)
        self.nickname_line_login.setGeometry(QtCore.QRect(180, 170, 211, 31))
        self.nickname_line_login.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"border: 2.7px solid  rgb(192, 192, 192);\n"
"border-radius: 10px;")
        self.nickname_line_login.setObjectName("nickname_line_login")
        self.passw_line_login = QtWidgets.QLineEdit(self.frame)
        self.passw_line_login.setGeometry(QtCore.QRect(180, 325, 211, 31))
        self.passw_line_login.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
"border: 2.7px solid  rgb(192, 192, 192);\n"
"border-radius: 10px;")
        self.passw_line_login.setObjectName("passw_line_login")
        self.passw_line_login.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.nickname_warning_login = QtWidgets.QLabel(self.login_page)
        self.nickname_warning_login.setGeometry(QtCore.QRect(377, 225, 291, 16))
        self.nickname_warning_login.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(242, 79, 128);")
        self.password_warning_login = QtWidgets.QLabel(self.frame)
        self.password_warning_login.setGeometry(QtCore.QRect(190, 360, 191, 16))
        self.password_warning_login.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(242, 79, 128);")
        self.password_warning_login.setAlignment(QtCore.Qt.AlignCenter)
        self.checkbox_login = QtWidgets.QCheckBox(self.login_page)
        self.checkbox_login.setGeometry(QtCore.QRect(629, 346, 131, 19))
        self.checkbox_login.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 255, 255);")
        self.back_button_2 = QtWidgets.QPushButton(self.frame)
        self.back_button_2.setGeometry(QtCore.QRect(310, 480, 181, 41))
        self.back_button_2.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(64, 64, 64);\n"
"                                        border-style:outlet;\n"
"                                        border-width:2px;\n"
"                                        border-radius:10px;\n"
"                                        border-color: rgb(255, 255, 255);")
        self.back_button_2.setObjectName("back_button_2")
        self.login_button_2 = QtWidgets.QPushButton(self.frame)
        self.login_button_2.setGeometry(QtCore.QRect(90, 480, 181, 41))
        self.login_button_2.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(64, 64, 64);\n"
"                                        border-style:outlet;\n"
"                                        border-width:2px;\n"
"                                        border-radius:10px;\n"
"                                        border-color: rgb(255, 255, 255);")
        self.login_button_2.setObjectName("login_button_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(180, 300, 51, 20))
        self.label_6.setStyleSheet("QLabel {\n"
"font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(180, 140, 111, 21))
        self.label_7.setStyleSheet("QLabel {\n"
"font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.frame)
        self.stackedWidget.addWidget(self.login_page)
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.home_page)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.home_page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, -1, 481, 561))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 221, 201))
        self.label_9.setStyleSheet("background-image: url(:/image/user.jfif);\n"
"background-color: none")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(260, 60, 47, 13))
        self.label_11.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setGeometry(QtCore.QRect(260, 125, 51, 21))
        self.label_12.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setGeometry(QtCore.QRect(260, 190, 111, 20))
        self.label_13.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.name_home = QtWidgets.QLabel(self.frame_6)
        self.name_home.setGeometry(QtCore.QRect(292, 55, 151, 21))
        self.name_home.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(253, 195, 96);")
        self.name_home.setObjectName("name_home")
        self.surname_home = QtWidgets.QLabel(self.frame_6)
        self.surname_home.setGeometry(QtCore.QRect(315, 125, 151, 21))
        self.surname_home.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(253, 195, 96);")
        self.surname_home.setObjectName("surname_home")
        self.prediction_number = QtWidgets.QLabel(self.frame_6)
        self.prediction_number.setGeometry(QtCore.QRect(370, 190, 81, 21))
        self.prediction_number.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(253, 195, 96);")
        self.prediction_number.setObjectName("prediction_number")
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 481, 31))
        self.label_8.setStyleSheet("font: 16pt \"MS Reference Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.news_text = QtWidgets.QTextEdit(self.frame_4)
        self.news_text.setGeometry(QtCore.QRect(10, 10, 461, 241))
        self.news_text.setStyleSheet("border: 2.7px solid rgb(192, 192, 192);\n"
"border-radius: 8px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.news_text.setObjectName("news_text")
        self.verticalLayout_4.addWidget(self.frame_4)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(530, 290, 501, 20))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(500, 10, 20, 571))
        self.label_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(529, 9, 481, 281))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_7)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_2.addWidget(self.page)
        self.sport = QtWidgets.QWidget()
        self.sport.setObjectName("sport")
        self.image_label = QtWidgets.QLabel(self.sport)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 463, 263))
        self.image_label.setStyleSheet("background-image: url(:/sport/rsz_sport.png);")
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.stackedWidget_2.addWidget(self.sport)
        self.crime = QtWidgets.QWidget()
        self.crime.setObjectName("crime")
        self.image_label_2 = QtWidgets.QLabel(self.crime)
        self.image_label_2.setGeometry(QtCore.QRect(0, 0, 463, 263))
        self.image_label_2.setStyleSheet("background-image: url(:/crime/rsz_crime-removebg-preview.png);")
        self.image_label_2.setText("")
        self.image_label_2.setObjectName("image_label_2")
        self.stackedWidget_2.addWidget(self.crime)
        self.tech_science = QtWidgets.QWidget()
        self.tech_science.setObjectName("tech_science")
        self.image_label_3 = QtWidgets.QLabel(self.tech_science)
        self.image_label_3.setGeometry(QtCore.QRect(0, 0, 463, 263))
        self.image_label_3.setStyleSheet("background-image: url(:/tech/rsz_tech_science__2_-removebg-preview.png);")
        self.image_label_3.setText("")
        self.image_label_3.setObjectName("image_label_3")
        self.stackedWidget_2.addWidget(self.tech_science)
        self.entertainment = QtWidgets.QWidget()
        self.entertainment.setObjectName("entertainment")
        self.image_label_4 = QtWidgets.QLabel(self.entertainment)
        self.image_label_4.setGeometry(QtCore.QRect(0, 0, 463, 263))
        self.image_label_4.setStyleSheet("background-image: url(:/entertainment/rsz_entertainment.png);")
        self.image_label_4.setText("")
        self.image_label_4.setObjectName("image_label_4")
        self.stackedWidget_2.addWidget(self.entertainment)
        self.business = QtWidgets.QWidget()
        self.business.setObjectName("business")
        self.image_label_5 = QtWidgets.QLabel(self.business)
        self.image_label_5.setGeometry(QtCore.QRect(0, 0, 463, 263))
        self.image_label_5.setStyleSheet("background-image: url(:/business/rsz_1business.png);")
        self.image_label_5.setText("")
        self.image_label_5.setObjectName("image_label_5")
        self.stackedWidget_2.addWidget(self.business)
        self.medical = QtWidgets.QWidget()
        self.medical.setObjectName("medical")
        self.image_label_6 = QtWidgets.QLabel(self.medical)
        self.image_label_6.setGeometry(QtCore.QRect(0, 0, 463, 263))
        self.image_label_6.setStyleSheet("background-image: url(:/medical/rsz_medical-removebg-preview.png);")
        self.image_label_6.setText("")
        self.image_label_6.setObjectName("image_label_6")
        self.stackedWidget_2.addWidget(self.medical)
        self.politics = QtWidgets.QWidget()
        self.politics.setObjectName("politics")
        self.image_label_7 = QtWidgets.QLabel(self.politics)
        self.image_label_7.setGeometry(QtCore.QRect(0, 0, 463, 263))
        self.image_label_7.setAutoFillBackground(False)
        self.image_label_7.setStyleSheet("background-image: url(:/politics/rsz_politics-removebg-preview.png);")
        self.image_label_7.setText("")
        self.image_label_7.setScaledContents(True)
        self.image_label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label_7.setObjectName("image_label_7")
        self.stackedWidget_2.addWidget(self.politics)
        self.horizontalLayout_8.addWidget(self.stackedWidget_2)
        self.exit_button_2 = QtWidgets.QPushButton(self.frame_2)
        self.exit_button_2.setGeometry(QtCore.QRect(820, 530, 181, 41))
        self.exit_button_2.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(64, 64, 64);\n"
"                                        border-style:outlet;\n"
"                                        border-width:2px;\n"
"                                        border-radius:10px;\n"
"                                        border-color: rgb(255, 255, 255);")
        self.exit_button_2.setObjectName("exit_button_2")
        self.predict_button = QtWidgets.QPushButton(self.frame_2)
        self.predict_button.setGeometry(QtCore.QRect(590, 530, 181, 41))
        self.predict_button.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(64, 64, 64);\n"
"                                        border-style:outlet;\n"
"                                        border-width:2px;\n"
"                                        border-radius:10px;\n"
"                                        border-color: rgb(255, 255, 255);")
        self.predict_button.setObjectName("predict_button")
        self.clear_button = QtWidgets.QPushButton(self.frame_2)
        self.clear_button.setGeometry(QtCore.QRect(175, 555, 140, 30))
        self.clear_button.setStyleSheet("font: 75 14pt \\\"MS Shell Dlg 2\\\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(64, 64, 64);\n"
"                                        border-style:outlet;\n"
"                                        border-width:2px;\n"
"                                        border-radius:10px;\n"
"                                        border-color: rgb(255, 255, 255);")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setGeometry(QtCore.QRect(566, 320, 421, 21))
        self.label_19.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(253, 195, 96);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.forecast_label = QtWidgets.QLabel(self.frame_2)
        self.forecast_label.setGeometry(QtCore.QRect(550, 370, 451, 131))
        self.forecast_label.setStyleSheet("background-color: rgb(192, 192, 192);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(158, 74, 255);")
        self.forecast_label.setAlignment(QtCore.Qt.AlignCenter)
        self.forecast_label.setObjectName("forecast_label")
        self.horizontalLayout_7.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.home_page)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.content_bar)
        self.credits_bar = QtWidgets.QFrame(self.dropShadowFrame)
        self.credits_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.credits_bar.setStyleSheet("background-color:none;")
        self.credits_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_bar.setObjectName("credits_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_label_credits = QtWidgets.QFrame(self.credits_bar)
        self.frame_label_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_credits.setObjectName("frame_label_credits")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_label_credits)
        self.horizontalLayout_3.setContentsMargins(15, 0, 0, 5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_credits = QtWidgets.QLabel(self.frame_label_credits)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(15)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(128, 102, 168);")
        self.label_credits.setObjectName("label_credits")
        self.horizontalLayout_3.addWidget(self.label_credits)
        self.horizontalLayout_2.addWidget(self.frame_label_credits)
        self.frame_grip = QtWidgets.QFrame(self.credits_bar)
        self.frame_grip.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setStyleSheet("padding:5px;")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_2.addWidget(self.frame_grip)
        self.verticalLayout_2.addWidget(self.credits_bar)
        self.verticalLayout.addWidget(self.dropShadowFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1135, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "News Category Predictor"))
        self.label_title.setText(_translate("MainWindow", "News Category Prediction"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Exit"))
        self.login_button.setText(_translate("MainWindow", "Giriş Yap"))
        self.register_button.setText(_translate("MainWindow", "Kayıt Ol"))
        self.exit_button.setText(_translate("MainWindow", "Çıkış"))
        self.register_button_2.setText(_translate("MainWindow", "Kayıt Ol"))
        self.back_button.setText(_translate("MainWindow", "Geri"))
        self.label.setText(_translate("MainWindow", "Ad"))
        self.label_2.setText(_translate("MainWindow", "Soyad"))
        self.label_3.setText(_translate("MainWindow", "Kullanıcı Adı"))
        self.label_4.setText(_translate("MainWindow", "Şifre"))
        self.label_5.setText(_translate("MainWindow", "E-mail"))
        self.back_button_2.setText(_translate("MainWindow", "Geri"))
        self.login_button_2.setText(_translate("MainWindow", "Giriş Yap"))
        self.label_6.setText(_translate("MainWindow", "Şifre"))
        self.label_7.setText(_translate("MainWindow", "Kullanıcı Adı"))
        self.label_11.setText(_translate("MainWindow", "Ad:"))
        self.label_12.setText(_translate("MainWindow", "Soyad:"))
        self.label_13.setText(_translate("MainWindow", "Tahmin Sayısı:"))
        self.name_home.setText(_translate("MainWindow", ""))
        self.surname_home.setText(_translate("MainWindow", ""))
        self.checkbox.setText("Şifreyi Göster.")
        self.checkbox_login.setText("Şifreyi Göster.")
        self.name_warning.setText("Ad sadece a-Z karakterler içermeli.")
        self.surname_warning.setText("Soyad sadece a-Z karakterler içermeli.")
        self.nickname_warning.setText("Kullanıcı adları harf (a-z), rakam (0-9) ve nokta (.) içerebilir.")
        self.mail_warning.setText("""Geçersiz e-mail adresi!""")
        self.nickname_warning_login.setText("Kullanıcı adları harf (a-z), rakam (0-9) ve nokta (.) içerebilir.")
        self.password_warning.setText("""Şifre " ' = karakterlerini içeremez.""")
        self.password_warning_login.setText("""Şifre " ' = karakterlerini içeremez.""")
        self.password_warning.setHidden(True)
        self.password_warning_login.setHidden(True)
        self.name_warning.setHidden(True)
        self.surname_warning.setHidden(True)
        self.nickname_warning.setHidden(True)
        self.mail_warning.setHidden(True)
        self.nickname_warning_login.setHidden(True)
        self.register_button_2.setEnabled(False)
        self.register_button_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                            "color:rgb(255, 255, 255);\n"
                                            "background-color: rgb(224, 224, 224);\n"
                                            "border-style:outlet;\n"
                                            "border-width:2px;\n"
                                            "border-radius:10px;\n"
                                            "border-color: rgb(0, 0, 0);")
        self.register_button_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.login_button_2.setEnabled(False)
        self.login_button_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                            "color:rgb(255, 255, 255);\n"
                                            "background-color: rgb(224, 224, 224);\n"
                                            "border-style:outlet;\n"
                                            "border-width:2px;\n"
                                            "border-radius:10px;\n"
                                            "border-color: rgb(0, 0, 0);")
        self.login_button_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.predict_button.setEnabled(False)
        self.predict_button.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(224, 224, 224);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(0, 0, 0);")
        self.predict_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.clear_button.setText("Temizle")
        self.clear_button.setEnabled(False)
        self.clear_button.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                                    "color:rgb(255, 255, 255);\n"
                                                    "background-color: rgb(224, 224, 224);\n"
                                                    "border-style:outlet;\n"
                                                    "border-width:2px;\n"
                                                    "border-radius:10px;\n"
                                                    "border-color: rgb(0, 0, 0);")
        self.clear_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prediction_number.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", "Bir haber metni veya haber başlığı giriniz"))
        self.news_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.exit_button_2.setText(_translate("MainWindow", "Çıkış"))
        self.predict_button.setText(_translate("MainWindow", "Tahmin Yap"))
        self.label_19.setText(_translate("MainWindow", "Tahmin Sonucu:"))
        self.forecast_label.setText(_translate("MainWindow", ""))
        self.label_credits.setText(_translate("MainWindow", "By: Emirhan Ese"))
import resource_rc
