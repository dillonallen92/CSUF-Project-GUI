from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow

import sys 

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("First Window")
    button = QPushButton("Press Me!")
    
    self.setCentralWidget(button)


if __name__ == "__main__":
  app = QApplication([])
  window = MainWindow()
  window.show()
  app.exec()
  