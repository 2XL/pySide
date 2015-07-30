__author__ = 'anna'

# Hints
# absolute positioning layout starts at top-left (0,0)

# Import the necessary modules required
import sys
import time
from PySide.QtCore import Qt,  QDateTime, QTimer, SIGNAL
from PySide.QtGui import QApplication, QLabel, QWidget, QIcon, QToolTip, QPushButton, QMessageBox, QDesktopWidget, \
    QLCDNumber, QMainWindow, QStatusBar, QProgressBar, QTextEdit, QAction, QKeySequence, QHBoxLayout


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



    def SetLayout(self):
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
        mainWindow = MainWindow()
        mainWindow.SetLayout()
        #mainWindow.CreateStatusBar()
        #mainWindow.SetupComponents()
        mainWindow.show()
        #mainWindow.ShowProgress()
        myApp.exec_()
        sys.exit(0)

    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])