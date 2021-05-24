import sys
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from style import stylesheet

def main():
  app = QApplication(sys.argv)
  QFontDatabase.addApplicationFont("static/Fonts/Inter/Inter.ttf")
  # app.setFont(QFont("Inter"))
  app.setStyleSheet(stylesheet)

  window = MainWindow()
  window.show()

  sys.exit(app.exec_())

if __name__ == "__main__":
  main()