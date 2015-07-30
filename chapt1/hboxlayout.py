

__author__ = 'anna'
# Import the necessary modules required
import sys
import time
from PySide.QtCore import Qt,  QDateTime, QTimer, SIGNAL
from PySide.QtGui import QApplication, QLabel, QWidget, QIcon, QToolTip, QPushButton, QMessageBox, QDesktopWidget, \
    QLCDNumber, QMainWindow, QStatusBar, QProgressBar, QTextEdit, QAction, QKeySequence, QHBoxLayout

class MainWindow(QWidget):
    """ Our Main Window class
    """
    def __init__(self):
        """ Constructor Function
        """
        QWidget.__init__(self)
        self.setWindowTitle("Horizontal Layout")
        self.setGeometry(300, 250, 400, 300)

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
