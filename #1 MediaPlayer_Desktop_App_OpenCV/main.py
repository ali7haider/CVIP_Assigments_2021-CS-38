import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QSizePolicy
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage
from main_ui import Ui_MainWindow  # Import the generated class

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from the generated class
        self.setupUi(self)

        # Set flags to remove the default title bar
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Connect the maximizeRestoreAppBtn button to the maximize_window method
        self.maximizeRestoreAppBtn.clicked.connect(self.maximize_window)

        # Connect the closeAppBtn button to the close method
        self.closeAppBtn.clicked.connect(self.close)

        # Connect the minimizeAppBtn button to the showMinimized method
        self.minimizeAppBtn.clicked.connect(self.showMinimized)

        # Connect the btnBrowse button to open file dialog
        self.btnBrowse.clicked.connect(self.open_file_dialog)
    
        self.videoLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.videoLabel.setAlignment(Qt.AlignCenter)




        # Initialize video player variables
        self.video_file_path = None
        self.cap = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mov *.mkv *.wmv)", options=options)
        if file_name:
            self.video_file_path = file_name
            self.txtBrowsePath.setText(file_name)
            self.play_video()

    def play_video(self):
        if self.video_file_path is not None:
            self.cap = cv2.VideoCapture(self.video_file_path)
            if not self.cap.isOpened():
                print("Error: Unable to open video file")
                return

            # Start the timer to update the frame
            self.timer.start(33)  # Update frame every ~33 milliseconds (about 30 frames per second)

    def update_frame(self):
        if self.cap is None or not self.cap.isOpened():
            return
    
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame to QPixmap
            pixmap = self.convert_cv_to_pixmap(frame)
            
            # Scale the QPixmap to fit the QLabel while maintaining aspect ratio
            scaled_pixmap = pixmap.scaled(self.videoLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            
            # Set the scaled QPixmap to the QLabel
            self.videoLabel.setPixmap(scaled_pixmap)



    def convert_cv_to_pixmap(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        q_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(q_img)

    def maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
