#1.Importar módulos
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QPushButton, QLabel, QLineEdit, QTableWidgetItem
from random import *
import json 
#2.Crear la aplicación
app = QApplication([])
window = QWidget()
window.setWindowTitle('Aplicación de gestión tienda de coches en miniatura')
window.resize(900,600)
#3.Crear Widgets
table = QTableWidget()
add_button = QPushButton('Añadir vehículos')
sell_button = QPushButton('Vender vehículo seleccionado')
type_brand = QLineEdit('')
type_brand.setPlaceholderText('Introduce la marca...')
type_model = QLineEdit('')
type_model.setPlaceholderText('Introduce el modelo...')
type_colour = QLineEdit('')
type_colour.setPlaceholderText('Introduce el color...')
type_year = QLineEdit('')
type_year.setPlaceholderText('Introduce el año...')
type_price = QLineEdit('')
type_price.setPlaceholderText('Introduce el precio de venta...')
#4.Diseñar la aplicación
horizontal_principal = QHBoxLayout()
vertical_1 = QVBoxLayout()
vertical_2 = QVBoxLayout()
vertical_1.addWidget(table)
vertical_2.addWidget(add_button)
vertical_2.addWidget(sell_button)
horizontal_principal.addLayout(vertical_1)
horizontal_principal.addLayout(vertical_2)
window.setLayout(horizontal_principal)
window.show()
app.exec_()
