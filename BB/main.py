__author__ = 'anna'

# Hints
# absolute positioning layout starts at top-left (0,0)
# implementar una interficie similar al putty
# arquitectura de proxy master node (with nodejs monitor) + dummy slave clients + stacksync server + owncloud server
# + mongodb : mongolab => get reports from the dummy slaves when this results executing simulations.


# Import the necessary modules required
import sys
import time
#from PySide.QtCore import Qt,  QDateTime, QTimer, SIGNAL
#from PySide.QtGui import QApplication, QLabel, QWidget, QIcon, QToolTip, QPushButton, QMessageBox, QDesktopWidget, \
#    QLCDNumber, QMainWindow, QStatusBar, QProgressBar, QTextEdit, QAction, QKeySequence, QHBoxLayout
from PySide.QtCore import *
from PySide.QtGui import *

class MainWindow(QWidget):
    """ Our Main Window Class
    """
    def __init__(self):
        """ Constructor Fucntion
        """
        QWidget.__init__(self)
        self.setWindowTitle("BenchBox GUI v0.0.1")
        self.setWindowIcon(QIcon('icon/face.png'))
        self.setGeometry(300, 250, 400, 300)
        #self.statusLabel = QLabel('Showing Progress')
        #self.progressBar = QProgressBar()
        #self.progressBar.setMinimum(0)
        #self.progressBar.setMaximum(100)

        self.myLayout = QVBoxLayout()
        self.myLabel = QLabel("Press 'Esc' to close this App")
        self.infoLabel = QLabel()
        self.myLabel.setAlignment(Qt.AlignCenter)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.myLayout.addWidget(self.myLabel)
        self.myLayout.addWidget(self.infoLabel)
        self.setLayout(self.myLayout)


    # Function reimplementing Key Press, Mouse Click and Resize Events
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape: self.close()

    def mouseDoubleClickEvent(self, event):
        self.close()

    def resizeEvent(self, event):
        self.infoLabel.setText("Window Resized to QSize(%d, %d)" % (event.size().width(), event.size().height()))




    def SetHLayout(self):
        """ Function to add buttons and set the layout
        """
        horizontalLayout = QHBoxLayout(self)
        hButton1 = QPushButton('Button 1', self)
        hButton2 = QPushButton('Button 2', self)
        hButton3 = QPushButton('Button 3', self)
        hButton4 = QPushButton('Button 4', self)
        horizontalLayout.addWidget(hButton1)
        horizontalLayout.addWidget(hButton2)
        horizontalLayout.addWidget(hButton3)
        horizontalLayout.addWidget(hButton4)
        self.setLayout(horizontalLayout)


    def SetVLayout(self):
        verticalLayout = QVBoxLayout(self)
        vButton1 = QPushButton('Button 1', self)
        vButton2 = QPushButton('Button 2', self)
        vButton3 = QPushButton('Button 3', self)
        vButton4 = QPushButton('Button 4', self)
        verticalLayout.addWidget(vButton1)
        verticalLayout.addWidget(vButton2)
        verticalLayout.addStretch()
        verticalLayout.addWidget(vButton3)
        verticalLayout.addWidget(vButton4)
        self.setLayout(verticalLayout)

    def SetGLayout(self):
        gridLayout = QGridLayout(self)
        gButton1 = QPushButton('Button 1 (0,0)', self)
        gButton2 = QPushButton('Button 2 (0,1)', self)
        gButton3 = QPushButton('Button 3 (1,0, 1,2)', self)
        gButton4 = QPushButton('Button 4 (2,0)', self)
        gButton5 = QPushButton('Button 5 (2,1)', self)
        gridLayout.addWidget(gButton1, 0, 0)
        gridLayout.addWidget(gButton2, 0, 1)
        gridLayout.addWidget(gButton3, 1, 0, 1, 2)
        gridLayout.addWidget(gButton4, 2, 0)
        gridLayout.addWidget(gButton5, 2, 1)
        self.setLayout(gridLayout)

    def SetFLayout(self):
        formLayout = QFormLayout(self)
        labelUsername = QLabel("Username")
        txtUsername = QLineEdit()
        labelPassword = QLabel("Password")
        txtPassword = QLineEdit()
        labelStackSync = QLabel("StackSync")
        txtStackSync = QLineEdit()
        labelOwnCoud = QLabel("OwnCloud")
        txtOwnCloud = QLineEdit()
        btnNext = QPushButton('Button Next (2,0)', self)
        btnBack = QPushButton('Button Back (2,1)', self)
        formLayout.addRow(labelUsername, txtUsername)
        formLayout.addRow(labelPassword, txtPassword)
        formLayout.addRow(labelStackSync, txtStackSync)
        formLayout.addRow(labelOwnCoud, txtOwnCloud)
        formLayout.addRow(btnBack, btnNext)
        self.setLayout(formLayout)

    def CreateStatusBar(self):
            """ Function to create Status Bar
            """
            self.myStatusBar = QStatusBar()
            self.progressBar.setValue(10)
            self.myStatusBar.addWidget(self.statusLabel, 1)
            self.myStatusBar.addWidget(self.progressBar, 2)
            self.setStatusBar(self.myStatusBar)

    def ShowProgress(self):
        """ Function to show progress
        """
        while(self.progressBar.value() < self.progressBar.maximum()):
            self.progressBar.setValue(self.progressBar.value() + 45)
            time.sleep(1) # no sleep
            self.statusLabel.setText('Ready')

    def SetupComponents(self):
        """ Setting the central widget
        """
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 10000)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.CreateActions()
        self.CreateMenus() #---------------------
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.copyAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.pasteAction)
        self.helpMenu.addAction(self.aboutAction)
        self.CreateToolBar() #-------------------
        self.mainToolBar.addAction(self.newAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.copyAction)
        self.mainToolBar.addAction(self.pasteAction)

    def newFile(self):
        self.textEdit.setText('')

    def exitFile(self):
        self.close()

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor",
                          "This example demonstrates the use "
                          "of Menu Bar")

    def CreateActions(self):
        """ Function to create actions for menus
        """
        self.newAction = QAction( QIcon('new.png'), '&New',
                              self, shortcut=QKeySequence.New,
                              statusTip="Create a New File",
                              triggered=self.newFile)
        self.exitAction = QAction( QIcon('exit.png'), 'E&xit',
                           self, shortcut="Ctrl+Q",
                           statusTip="Exit the Application",
                           triggered=self.exitFile)
        self.copyAction = QAction( QIcon('copy.png'), 'C&opy',
                           self, shortcut="Ctrl+C",
                           statusTip="Copy",
                           triggered=self.textEdit.copy)
        self.pasteAction = QAction( QIcon('paste.png'), '&Paste',
                            self, shortcut="Ctrl+V",
                            statusTip="Paste",
                            triggered=self.textEdit.paste)
        self.aboutAction = QAction( QIcon('about.png'), 'A&bout',
                            self, statusTip="Displays info about text editor",
                            triggered=self.aboutHelp)
        # Actual menu bar item creation

    def CreateMenus(self):
        """ Function to create actual menu bar
        """
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")


    def CreateToolBar(self):
        """ Function to create tool bar
        """
        self.mainToolBar = self.addToolBar('Main')


class SampleWindow(QWidget):
    """ Our main window class
    """
    # Constructor function
    def __init__(self):
        QWidget.__init__(self)
        # width, height
        self.setWindowTitle("BencBox GUI")
        self.setGeometry(500, 500, 500, 500)

    def setIcon(self):
        """ Function to set Icon
        """
        appIcon = QIcon('icon/king.png')
        self.setWindowIcon(appIcon)

    def setButton(self):
        """ Function to add a quit button
        """
        myButton = QPushButton('Quit', self)
        myButton.move(50, 100)
        #myButton.clicked.connect(myApp.quit)
        myButton.clicked.connect(self.quitApp) # pregunta abans de sortir

    def center(self):
        """ Function to center the application
        """
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center() # find the available frame map
        qRect.moveCenter(centerPoint) # position the the frame center
        self.move(qRect.topLeft()) # put the window in  the frame center

    def setIconModes(self):
            myIcon1 = QIcon('icon/king.png')
            myLabel1 = QLabel('sample', self)
            pixmap1 = myIcon1.pixmap(50, 50, QIcon.Active, QIcon.On)
            myLabel1.setPixmap(pixmap1)
            myIcon2 = QIcon('icon/king.png')
            myLabel2 = QLabel('sample', self)
            pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
            myLabel2.setPixmap(pixmap2)
            myLabel2.move(50, 0)
            myIcon3 = QIcon('icon/king.png')
            myLabel3 = QLabel('sample', self)
            pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
            myLabel3.setPixmap(pixmap3)
            myLabel3.move(100, 0)

    def quitApp(self):
        """ Function to confirm a message from the user
        """
        userInfo = QMessageBox.question(self, 'Confirmation',"This will quit the application. Do you want to Continue?", QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            myApp.quit()
        if userInfo == QMessageBox.No:
            pass

    def setAboutButton(self):
        """ Function to set About Button
        """
        self.aboutButton = QPushButton("About", self)
        self.aboutButton.move(100, 200)
        self.aboutButton.clicked.connect(self.showAbout)

    def showAbout(self):
        """ Function to show About Box
        """
        QMessageBox.about(self.aboutButton, "About PySide", "PySide is a cross-platform tool for generating GUI Programs.")


class MyTimer(QWidget):
    """ Our Main Window class for Timer
    """
    def __init__(self):
        """ Constructor Function
        """
        QWidget.__init__(self)
        self.setWindowTitle('My Digital Clock')
        timer = QTimer(self)
        self.connect(timer, SIGNAL("timeout()"), self.updtTime)
        self.myTimeDisplay = QLCDNumber(self)
        self.myTimeDisplay.setSegmentStyle(QLCDNumber.Filled)
        self.myTimeDisplay.setDigitCount(8)
        self.myTimeDisplay.resize(500, 150)
        timer.start(1000)

    def updtTime(self):
        """ Function to update current time
        """
        currentTime = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.myTimeDisplay.display(currentTime)

class MyWidget(QWidget):
    # Constructor function
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Reimplementing Events")
        self.setGeometry(300, 250, 300, 100)
        self.myLayout = QVBoxLayout()
        self.myLabel1 = QLabel("Text 1")
        self.myLineEdit1 = QLineEdit()
        self.myLabel2 = QLabel("Text 2")
        self.myLineEdit2 = QLineEdit()
        self.myLabel3 = QLabel("Text 3")
        self.myLineEdit3 = QLineEdit()
        self.myLayout.addWidget(self.myLabel1)
        self.myLayout.addWidget(self.myLineEdit1)
        self.myLayout.addWidget(self.myLabel2)
        self.myLayout.addWidget(self.myLineEdit2)
        self.myLayout.addWidget(self.myLabel3)
        self.myLayout.addWidget(self.myLineEdit3)
        self.setLayout(self.myLayout)
        self.installEventFilter(self)

    # Function reimplementing event() function
    def event(self, event):
        if event.type()== QEvent.KeyRelease and event.key()== Qt.Key_Tab:
            self.myLineEdit3.setFocus()  # always focus this button on tab...
            return True
        return QWidget.event(self,event)

    def eventFilter(self, receiver, event):
        if(event.type() == QEvent.MouseButtonPress):
            QMessageBox.information(None,"Filtered Mouse Press Event!!",'Mouse Press Detected')
            return True
        return super(MyWidget,self).eventFilter(receiver, event)

class MyApplication(QApplication):
    def __init__(self, args):
        super(MyApplication, self).__init__(args)

    def notify(self, receiver, event):
        if (event.type() == QEvent.KeyPress):
            QMessageBox.information(None, "Received Key Release EVent", "You Pressed: "+ event.text())
        return super(MyApplication, self).notify(receiver, event)



class MyCalculator(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.amtLabel = QLabel('Loan Amount')
        self.roiLabel = QLabel('Rate of Interest')
        self.yrsLabel = QLabel('No. of Years')
        self.emiLabel = QLabel('EMI per month')
        self.emiValue = QLCDNumber()
        self.emiValue.setSegmentStyle(QLCDNumber.Flat)
        self.emiValue.setFixedSize(QSize(130,30))
        self.emiValue.setDigitCount(8)
        self.amtText = QLineEdit('10000')
        self.roiSpin = QSpinBox()
        self.roiSpin.setMinimum(1)
        self.roiSpin.setMaximum(15)
        self.yrsSpin = QSpinBox()
        self.yrsSpin.setMinimum(1)
        self.yrsSpin.setMaximum(20)
        self.roiDial = QDial()
        self.roiDial.setNotchesVisible(True)
        self.roiDial.setMaximum(15)
        self.roiDial.setMinimum(1)
        self.roiDial.setValue(1)
        self.yrsSlide = QSlider(Qt.Horizontal)
        self.yrsSlide.setMaximum(20)
        self.yrsSlide.setMinimum(1)
        self.calculateButton = QPushButton('Calculate EMI')
        self.myGridLayout = QGridLayout()
        self.myGridLayout.addWidget(self.amtLabel, 0, 0)
        self.myGridLayout.addWidget(self.roiLabel, 1, 0)
        self.myGridLayout.addWidget(self.yrsLabel, 2, 0)
        self.myGridLayout.addWidget(self.amtText, 0, 1)
        self.myGridLayout.addWidget(self.roiSpin, 1, 1)
        self.myGridLayout.addWidget(self.yrsSpin, 2, 1)
        self.myGridLayout.addWidget(self.roiDial, 1, 2)
        self.myGridLayout.addWidget(self.yrsSlide, 2, 2)
        self.myGridLayout.addWidget(self.calculateButton, 3, 1)
        self.setLayout(self.myGridLayout)

        # inserting/binding connectors to the widget

        self.setWindowTitle("A simple EMI calculator")
        self.roiDial.valueChanged.connect(self.roiSpin.setValue)
        self.connect(self.roiSpin, SIGNAL("valueChanged(int)"), self.roiDial.setValue)

        self.yrsSlide.valueChanged.connect(self.yrsSpin.setValue)
        self.connect(self.yrsSpin, SIGNAL("valueChanged(int)"), self.yrsSlide, SLOT("setValue(int)"))

        self.connect(self.calculateButton, SIGNAL("clicked()"), self.showEMI)

        #
    def showEMI(self):
        loanAmount = float(self.amtText.text())
        rateInterest = float( float (self.roiSpin.value() / 12) / 100)
        noMonths = int(self.yrsSpin.value() * 12)
        emi = (loanAmount * rateInterest) * ( ( ( (1 + rateInterest) ** noMonths ) / ( ( (1 + rateInterest) ** noMonths ) - 1) ))
        self.emiValue.display(emi)
        self.myGridLayout.addWidget(self.emiLabel, 4, 0)
        self.myGridLayout.addWidget(self.emiValue, 4, 2)







if __name__ == '__main__':
    # Create the main application
    try:
        myApp = QApplication(sys.argv)
        """
        myWindow = SampleWindow()
        myWindow.setIcon()
        myWindow.setIconModes()
        myWindow.setButton()
        myWindow.setAboutButton()
        myWindow.center()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)
        """
        """
        myWindow = MyTimer()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)
        """
        #mainWindow = MainWindow()
        #mainWindow.SetFLayout()
        #mainWindow.CreateStatusBar()
        #mainWindow.SetupComponents()
        #mainWindow.show()
        #mainWindow.ShowProgress()
        myWidget = MyCalculator()
        myWidget.showEMI()
        myApp.exec_()
        sys.exit(0)

    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])