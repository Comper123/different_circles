from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt
from random import randint
import io


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>500</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Разные окружности</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>10</y>
      <width>161</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Новая окружность</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>500</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.InitUI()
        self.draw = False
    
    def InitUI(self):
        self.button.clicked.connect(self.draw_circle)
        
    def draw_circle(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            # генерируем размер нужного нам круга
            width = randint(20, 480)
            # Генерируем случайные координаты круга
            x, y = randint(0, 500 - width), randint(0, 500 - width)
            self.painter = QPainter(self)
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
            self.painter.setBrush(QBrush(QColor(r, g, b), Qt.SolidPattern))
            self.painter.drawEllipse(x, y, width, width)
            self.painter.end()
            self.draw = False
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec())