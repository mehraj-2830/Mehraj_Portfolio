from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QIcon
from logging import exception


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CALCULATOR")
        self.resize(300, 270)
        self.text_box_1 = QLineEdit()
        self.text_box_2 = QLineEdit()
        self.text_box_1.setReadOnly(True)
        self.text_box_2.setReadOnly(True)
        font = QFont("Arial", 14)
        self.text_box_1.setFont(font)
        self.text_box_2.setFont(font)
        self.text_box_1.setAlignment(Qt.AlignRight)

        # Button Grid
        self.grid = QGridLayout()
        buttons = ["7", "8", "9", "/",
                   "4", "5", "6", "*",
                   "1", "2", "3", "-",
                   "0", ".", "=", "+"]

        button_row = 0
        button_col = 0

        for button_text in buttons:
            self.button = QPushButton(button_text)
            self.grid.addWidget(self.button, button_row, button_col)
            self.button.clicked.connect(self.Calc_function)
            button_col += 1
            if button_col > 3:
                button_row += 1
                button_col = 0

        # Extra Buttons
        self.clear = QPushButton("Clear")
        self.delete = QPushButton("Delete")
        self.Answer = QPushButton("Ans")

        self.clear.setObjectName("clearButton")
        self.delete.setObjectName("deleteButton")
        self.Answer.setObjectName("ansButton")

        self.clear.clicked.connect(self.Calc_function)
        self.delete.clicked.connect(self.Calc_function)
        self.Answer.clicked.connect(self.Calc_function)

        # Master Layout
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box_1)
        master_layout.addWidget(self.text_box_2)
        master_layout.addLayout(self.grid)

        # Extra Button Row
        Extra_button_row = QHBoxLayout()
        Extra_button_row.addWidget(self.clear)
        Extra_button_row.addWidget(self.delete)
        Extra_button_row.addWidget(self.Answer)

        master_layout.addLayout(Extra_button_row)
        self.setLayout(master_layout)





    def Calc_function(self): 
        text = self.sender().text()  
        current_text = self.text_box_1.text() 

        if text == "=":
            try:
                all_text = self.text_box_1.text()  
                result = eval(str(all_text))
                self.text_box_2.setText(str(result)) 
                self.text_box_1.clear() 

            except Exception as e:
                self.text_box_2.setText(str(e))  

        elif text == "Delete":
            self.text_box_1.setText(current_text[:-1])  
        elif text == "Clear":
            self.text_box_1.clear()  #
        elif text == "Ans":
            text_on_textBox_2 = self.text_box_2.text()  
            self.text_box_1.setText(current_text + text_on_textBox_2)  
        else:
            self.text_box_1.setText(current_text + text)  
            self.text_box_1.update()  


app = QApplication([])
image_path = "416cvwskOKL._UF894,1000_QL80_.jpg"
app.setStyleSheet("background-image: image_path")
main_window = Calculator()
main_window.setWindowIcon(QtGui.QIcon("475497.png"))
main_window.setStyleSheet("""
        QWidget {
            background:transparent;
            color: #fff;
            font: 30px Cosmic Sans MS;
        }

        QLineEdit {
            background: rgba(255, 255, 255, 0.2);  /* Lighter transparency */
            border: 1px solid rgba(255, 255, 255, 0.3); /* Lighter border */
            border-radius: 5px;
            padding: 5px;
            color: #fff;
        }

        QPushButton {
            background: rgba(255, 255, 255, 0.1);  /* Lighter transparency */
            border: 1px solid rgba(255, 255, 255, 0.2); /* Lighter border */
            border-radius: 5px;
            padding: 10px;
            color: #fff;
        }

        QPushButton:hover {
            background: rgba(255, 255, 255, 0.2);  /* Slightly more opaque on hover */
        }

        QPushButton:pressed {
            background: rgba(255, 255, 255, 0.3);  /* Even more opaque on press */
        }

        QPushButton#clearButton, QPushButton#deleteButton, QPushButton#ansButton {
            background: rgba(200, 50, 50, 0.2); /* Example color for special buttons */
        }

        QMainWindow {
            background: transparent;
            border-radius: 10px; /* Keep border radius if desired */
        }
    """)


main_window.show()
app.exec_()

