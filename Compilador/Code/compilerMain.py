import sys
from PyQt5.QtWidgets import QApplication
from compilerWindow import EditorWindow

app = QApplication(sys.argv)
textEditor = EditorWindow()
sys.exit(app.exec())
