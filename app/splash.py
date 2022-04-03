
import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer

app= QApplication(sys.argv)
lbl= QLabel('<font color=Green size=12><b>Hola es un splash</b></font>')
lbl.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
lbl.show()
QTimer.singleShot(10000,app.quit)
sys.exit(app.exec())

# val= user()
