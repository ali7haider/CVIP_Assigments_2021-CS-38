# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:54:31 2024

@author: Digital Zone
"""

import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QSizePolicy, QLabel, QProgressBar
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage, QIcon
from setting_ui import Ui_MainWindow  # Import the generated class
# from main import MainWindow  # Import the generated class

class SettingWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, main_window,video_info):
        super(SettingWindow, self).__init__()
        # Set up the user interface from the generated class
        self.setupUi(self)
        self.main_window = main_window


        # Set flags to remove the default title bar
        self.setWindowFlags(Qt.FramelessWindowHint)


        # Connect the closeAppBtn button to the close method
        self.closeAppBtn.clicked.connect(self.close)

        # Connect the minimizeAppBtn button to the showMinimized method
        self.minimizeAppBtn.clicked.connect(self.showMinimized)
        
        self.btnNormal.clicked.connect(self.showNormal)
        self.btnGrayScale.clicked.connect(self.showGrayScale)
        self.btnBlackWhite.clicked.connect(self.showBlackWhite)
        self.process_video_info(video_info)
    def process_video_info(self, video_info):
            
        self.lblInformation.setText(video_info)

    
    def showNormal(self):
        self.main_window.set_video_mode('normal')
        self.close()

    def showGrayScale(self):
        self.main_window.set_video_mode('grayscale')
        self.close()

    def showBlackWhite(self):
        self.main_window.set_video_mode('blackwhite')
        self.close()

