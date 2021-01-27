from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QMetaObject
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QRadioButton, QGridLayout, QWidget, QTextEdit, QAction, QMainWindow, QApplication, QToolBar, \
    QStatusBar, QMenuBar, QMenu, QPushButton, QComboBox, QButtonGroup, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel

filePath = ''


def setFontSize(textEdit, fontSize, statusBar):
    textEdit.setFontPointSize(int(fontSize))
    statusBar.setText('Zmieniono wielkość czcionki na ' + fontSize)


def setFontType(textEdit, button, statusBar):
    if button.isChecked():
        text = button.text()
        textEdit.setFontFamily(text)
        statusBar.setText('Zmieniono typ czcionki na ' + text)


def setTextColor(textEdit, button, statusBar):
    if button.isChecked():
        textEdit.setTextColor(button.palette().button().color())
        statusBar.setText('Zmieniono kolor czcionki')


def handleNewFile(textEdit, statusBar):
    global filePath
    textEdit.clear()
    filePath = ''
    print('d')
    statusBar.setText('Utworzono nowy plik')


def handleOpenFile(textEdit, statusBar):
    global filePath
    file = QFileDialog.getOpenFileName(None, 'Otwórz plik tekkstowy', 'c:\\', "Text files (*.txt)")
    if file[0] != '':
        filePath = file[0]
        txt = open(filePath, 'rt').read()
        textEdit.setText(txt)
        statusBar.setText('Otworzono plik ' + filePath)


def handleSaveFile(textEdit, statusBar):
    global filePath
    if filePath != '':
        try:
            with open(filePath, 'w') as file:
                file.write(textEdit.toPlainText())
        except Exception as e:
            print(str(e))
        statusBar.setText('Zapisano plik ' + filePath)
    else:
        handleSaveFileAs(textEdit, statusBar)


def handleSaveFileAs(textEdit, statusBar):
    global filePath
    file = QFileDialog.getSaveFileName(None, 'Zapisz plik', 'c:\\', "Text files (*.txt)")
    if file[0] != '':
        filePath = file[0]
        handleSaveFile(textEdit, statusBar)


def handleCopy(textEdit, statusBarText):
    textEdit.copy()
    statusBarText.setText('Skopiowano zaznaczenie do schowka')


def handleCut(textEdit, statusBarText):
    textEdit.cut()
    statusBarText.setText('Wycięto zaznaczenie do schowka')


def handlePaste(textEdit, statusBarText):
    textEdit.paste()
    statusBarText.setText('Wklejono zaznaczenie ze schowka')


def handleUndo(textEdit, statusBarText):
    textEdit.undo()
    statusBarText.setText('Cofnięto poprzednią akcję')


def handleRedo(textEdit, statusBarText):
    textEdit.redo()
    statusBarText.setText('Przywrócono poprzednią akcję')


def handleSelectAll(textEdit, statusBarText):
    textEdit.selectAll()
    statusBarText.setText('Zaznaczono cały tekst')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.png"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.statusbar = QStatusBar(MainWindow)
        self.statusBarText = QLabel()
        self.statusBarText.setAlignment(QtCore.Qt.AlignRight)
        self.statusbar.addWidget(self.statusBarText, 1)
        MainWindow.setStatusBar(self.statusbar)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(190, 0, 611, 501))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 171, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_3 = QRadioButton(self.gridLayoutWidget)
        self.radioButton = QRadioButton(self.gridLayoutWidget)
        self.radioButton_2 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setChecked(True)
        self.radioButtonGroup = QButtonGroup()
        self.radioButtonGroup.addButton(self.radioButton)
        self.radioButtonGroup.addButton(self.radioButton_2)
        self.radioButtonGroup.addButton(self.radioButton_3)
        self.radioButton.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.radioButton, statusBar=self.statusBarText: setFontType(
                textEdit, button, statusBar))
        self.radioButton_2.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.radioButton_2, statusBar=self.statusBarText: setFontType(
                textEdit, button, statusBar))
        self.radioButton_3.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.radioButton_3, statusBar=self.statusBarText: setFontType(
                textEdit, button, statusBar))
        self.gridLayout.addWidget(self.radioButton_2, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.radioButton_3, 1, 0, 1, 1)
        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.fontSizeList = ['8', '9', '10', '11', '12', '14', '16', '18', '20', '22', '24', '26', '28', '36', '48',
                             '72']
        self.comboBox.addItems(self.fontSizeList)
        self.comboBox.setCurrentIndex(4)
        self.comboBox.currentTextChanged.connect(
            lambda fontSize, textEdit=self.textEdit, statusBar=self.statusBarText: setFontSize(textEdit, fontSize,
                                                                                               statusBar))
        self.textEdit.setFont(QFont('Times New Roman', 12))
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QRect(9, 200, 171, 135))
        self.gridLayoutWidget_2.setFixedWidth(171)
        self.gridLayoutWidget_2.setFixedHeight(135)
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButtonGroup = QButtonGroup()
        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(255, 241, 60);\n"
                                        "}")
        self.pushButton_3.setText("")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_3, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_3)
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_16 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_16.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(107, 144, 186);\n"
                                         "}")
        self.pushButton_16.setText("")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_16, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_16)
        self.gridLayout_2.addWidget(self.pushButton_16, 3, 3, 1, 1)
        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "}")
        self.pushButton_2.setText("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_2, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_2)
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_6 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(126, 126, 126);\n"
                                        "}")
        self.pushButton_6.setText("")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_6, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_6)
        self.gridLayout_2.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_10 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(188, 121, 90);\n"
                                         "}")
        self.pushButton_10.setText("")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_10, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_10)
        self.gridLayout_2.addWidget(self.pushButton_10, 1, 2, 1, 1)
        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-color: black;\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton)
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_7 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(0, 175, 82);\n"
                                        "}")
        self.pushButton_7.setText("")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_7, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_7)
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.pushButton_11 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(0, 160, 228);\n"
                                         "}")
        self.pushButton_11.setText("")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_11, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_11)
        self.gridLayout_2.addWidget(self.pushButton_11, 2, 2, 1, 1)
        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(239, 227, 177);\n"
                                        "}")
        self.pushButton_4.setText("")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_4, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_4)
        self.gridLayout_2.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_12 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_12.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(143, 215, 232);\n"
                                         "}")
        self.pushButton_12.setText("")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_12, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_12)
        self.gridLayout_2.addWidget(self.pushButton_12, 3, 2, 1, 1)
        self.pushButton_14 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_14.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(255, 172, 199);\n"
                                         "}")
        self.pushButton_14.setText("")
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_14, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_14)
        self.gridLayout_2.addWidget(self.pushButton_14, 1, 3, 1, 1)
        self.pushButton_15 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_15.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(63, 72, 198);\n"
                                         "}")
        self.pushButton_15.setText("")
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_15, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_15)
        self.gridLayout_2.addWidget(self.pushButton_15, 2, 3, 1, 1)
        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(193, 193, 193);\n"
                                        "}")
        self.pushButton_5.setText("")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_5, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_5)
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_9 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(140, 9, 31);\n"
                                        "}")
        self.pushButton_9.setText("")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_9, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_9)
        self.gridLayout_2.addWidget(self.pushButton_9, 0, 2, 1, 1)
        self.pushButton_8 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(174, 229, 61);\n"
                                        "}")
        self.pushButton_8.setText("")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_8, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_8)
        self.gridLayout_2.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.pushButton_17 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_17.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(255, 126, 58);\n"
                                         "}")
        self.pushButton_17.setText("")
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_17, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_17)
        self.gridLayout_2.addWidget(self.pushButton_17, 0, 4, 1, 1)
        self.pushButton_18 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_18.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(255, 200, 56);\n"
                                         "}")
        self.pushButton_18.setText("")
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_18, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_18)
        self.gridLayout_2.addWidget(self.pushButton_18, 1, 4, 1, 1)
        self.pushButton_19 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_19.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(166, 74, 160);\n"
                                         "}")
        self.pushButton_19.setText("")
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_19, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_19)
        self.gridLayout_2.addWidget(self.pushButton_19, 2, 4, 1, 1)
        self.pushButton_20 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_20.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(199, 189, 228);\n"
                                         "}")
        self.pushButton_20.setText("")
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_20, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_20)
        self.gridLayout_2.addWidget(self.pushButton_20, 3, 4, 1, 1)
        self.pushButton_13 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_13.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(246, 36, 49);\n"
                                         "}")
        self.pushButton_13.setText("")
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.toggled.connect(
            lambda e, textEdit=self.textEdit, button=self.pushButton_13, statusBar=self.statusBarText: setTextColor(
                textEdit, button, statusBar))
        self.pushButtonGroup.addButton(self.pushButton_13)
        self.gridLayout_2.addWidget(self.pushButton_13, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuPlik = QMenu(self.menubar)
        self.menuEdycj = QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNowy = QAction(MainWindow)
        self.actionNowy.triggered.connect(lambda: handleNewFile(self.textEdit, self.statusBarText))
        self.actionOtworz = QAction(MainWindow)
        self.actionOtworz.triggered.connect(lambda: handleOpenFile(self.textEdit, self.statusBarText))
        self.actionZapisz = QAction(MainWindow)
        self.actionZapisz.triggered.connect(lambda: handleSaveFile(self.textEdit, self.statusBarText))
        self.actionZapisz_jako = QAction(MainWindow)
        self.actionZapisz_jako.triggered.connect(lambda: handleSaveFileAs(self.textEdit, self.statusBarText))
        self.actionZakoncz = QAction(MainWindow)
        self.actionZakoncz.triggered.connect(lambda: sys.exit())
        self.actionWytnij = QAction(MainWindow)
        self.actionWytnij.triggered.connect(lambda: handleCut(self.textEdit, self.statusBarText))
        self.actionKopiuj = QAction(MainWindow)
        self.actionKopiuj.triggered.connect(lambda: handleCopy(self.textEdit, self.statusBarText))
        self.actionWklej = QAction(MainWindow)
        self.actionWklej.triggered.connect(lambda: handlePaste(self.textEdit, self.statusBarText))
        self.actionZazancz_wszystko = QAction(MainWindow)
        self.actionZazancz_wszystko.triggered.connect(lambda: handleSelectAll(self.textEdit, self.statusBarText))
        self.actionNew_File = QAction(MainWindow)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("file.png"), QIcon.Normal, QIcon.Off)
        self.actionNew_File.setIcon(icon1)
        self.actionNew_File.triggered.connect(lambda: handleNewFile(self.textEdit, self.statusBarText))
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.triggered.connect(lambda: handleOpenFile(self.textEdit, self.statusBarText))
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("browse.png"), QIcon.Normal, QIcon.Off)
        self.actionOpen_File.setIcon(icon2)
        self.actionSave_File = QAction(MainWindow)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("save.png"), QIcon.Normal, QIcon.Off)
        self.actionSave_File.setIcon(icon3)
        self.actionSave_File.triggered.connect(lambda: handleSaveFile(self.textEdit, self.statusBarText))
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.triggered.connect(lambda: handleUndo(self.textEdit, self.statusBarText))
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("undo.png"), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon4)
        self.actionRedo = QAction(MainWindow)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap("redo.png"), QIcon.Normal, QIcon.Off)
        self.actionRedo.setIcon(icon5)
        self.actionRedo.triggered.connect(lambda: handleRedo(self.textEdit, self.statusBarText))
        self.actionCut = QAction(MainWindow)
        icon6 = QIcon()
        icon6.addPixmap(QPixmap("cut.png"), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon6)
        self.actionCut.triggered.connect(lambda: handleCut(self.textEdit, self.statusBarText))
        self.actionCopy = QAction(MainWindow)
        icon7 = QIcon()
        icon7.addPixmap(QPixmap("copy.png"), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon7)
        self.actionCopy.triggered.connect(lambda: handleCopy(self.textEdit, self.statusBarText))
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.triggered.connect(lambda: handlePaste(self.textEdit, self.statusBarText))
        icon8 = QIcon()
        icon8.addPixmap(QPixmap("paste.png"), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon8)
        self.menuPlik.addAction(self.actionNowy)
        self.menuPlik.addAction(self.actionOtworz)
        self.menuPlik.addAction(self.actionZapisz)
        self.menuPlik.addAction(self.actionZapisz_jako)
        self.menuPlik.addAction(self.actionZakoncz)
        self.menuEdycj.addAction(self.actionWytnij)
        self.menuEdycj.addAction(self.actionKopiuj)
        self.menuEdycj.addAction(self.actionWklej)
        self.menuEdycj.addAction(self.actionZazancz_wszystko)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuEdycj.menuAction())
        self.toolBar.addAction(self.actionNew_File)
        self.toolBar.addAction(self.actionOpen_File)
        self.toolBar.addAction(self.actionSave_File)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)

        self.leftPaneWidget = QWidget()
        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.comboBox)
        self.vBox.addWidget(self.radioButton)
        self.vBox.addWidget(self.radioButton_2)
        self.vBox.addWidget(self.radioButton_3)
        self.vBox.addWidget(self.gridLayoutWidget_2)
        self.leftPaneWidget.setLayout(self.vBox)
        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.leftPaneWidget)
        self.hBox.addWidget(self.textEdit)
        self.centralwidget.setLayout(self.hBox)
        self.setObjectTitles(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def setObjectTitles(self, MainWindow):
        MainWindow.setWindowTitle("Notatnik")
        self.radioButton_3.setText("Courier New")
        self.radioButton.setText("Arial")
        self.radioButton_2.setText("Times New Roman")
        self.menuPlik.setTitle("Plik")
        self.menuEdycj.setTitle("Edycja")
        self.toolBar.setWindowTitle("toolBar")
        self.actionNowy.setText("Nowy")
        self.actionNowy.setShortcut("Ctrl+N")
        self.actionOtworz.setText("Otwórz")
        self.actionOtworz.setShortcut("Ctrl+O")
        self.actionZapisz.setText("Zapisz")
        self.actionZapisz.setShortcut("Ctrl+S")
        self.actionZapisz_jako.setText("Zapisz jako")
        self.actionZapisz_jako.setShortcut("Ctrl+Shift+S")
        self.actionZakoncz.setText("Zakończ")
        self.actionWytnij.setText("Wytnij")
        self.actionWytnij.setShortcut("Ctrl+X")
        self.actionKopiuj.setText("Kopiuj")
        self.actionKopiuj.setShortcut("Ctrl+C")
        self.actionWklej.setText("Wklej")
        self.actionWklej.setShortcut("Ctrl+V")
        self.actionZazancz_wszystko.setText("Zaznacz wszystko")
        self.actionZazancz_wszystko.setShortcut("Ctrl+A")
        self.actionNew_File.setText("New File")
        self.actionNew_File.setToolTip("New File")
        self.actionNew_File.setShortcut("Ctrl+N")
        self.actionOpen_File.setText("Open File")
        self.actionOpen_File.setToolTip("Open File")
        self.actionOpen_File.setShortcut("Ctrl+O")
        self.actionSave_File.setText("Save File")
        self.actionSave_File.setToolTip("Save File")
        self.actionSave_File.setShortcut("Ctrl+S")
        self.actionUndo.setText("Undo")
        self.actionUndo.setToolTip("Undo Action")
        self.actionUndo.setShortcut("Ctrl+Z")
        self.actionRedo.setText("Redo")
        self.actionRedo.setToolTip("Redo Action")
        self.actionRedo.setShortcut("Ctrl+Shift+Z")
        self.actionCut.setText("Cut")
        self.actionCut.setToolTip("Cut Selection")
        self.actionCut.setShortcut("Ctrl+X")
        self.actionCopy.setText("Copy")
        self.actionCopy.setToolTip("Copy Selection")
        self.actionCopy.setShortcut("Ctrl+C")
        self.actionPaste.setText("Paste")
        self.actionPaste.setToolTip("Paste Text")
        self.actionPaste.setShortcut("Ctrl+V")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
