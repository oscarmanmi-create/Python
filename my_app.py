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
table.setColumnCount(5)
table.setHorizontalHeaderLabels(['marca','modelo','color','año','precio'])
add_button = QPushButton('Añadir vehículos')
sell_button = QPushButton('Vender vehículo seleccionado')
sell_button.setChecked(False)
money_left = QLabel('Tu dinero:')
money_number = QLabel('0€')
type_brand = None
type_model = None
type_colour = None
type_year = None
type_price = None
emerging_window = None
#4.Diseñar la aplicación
horizontal_principal = QHBoxLayout()
vertical_1 = QVBoxLayout()
vertical_2 = QVBoxLayout()
vertical_1.addWidget(table)
vertical_2.addWidget(add_button)
vertical_2.addWidget(sell_button)
vertical_2.addWidget(money_left)
vertical_2.addWidget(money_number)
horizontal_principal.addLayout(vertical_1)
horizontal_principal.addLayout(vertical_2)
window.setLayout(horizontal_principal)
#5. Funciones de la aplicación
def new_window():
    global emerging_window
    global type_brand, type_model, type_colour, type_year, type_price
    emerging_window = QDialog()
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
    save_button = QPushButton('Añadir a la lista')
    vertical_emergente = QVBoxLayout()
    vertical_emergente.addWidget(type_brand)
    vertical_emergente.addWidget(type_model)
    vertical_emergente.addWidget(type_colour)
    vertical_emergente.addWidget(type_year)
    vertical_emergente.addWidget(type_price)
    vertical_emergente.addWidget(save_button)
    save_button.clicked.connect(save)
    emerging_window.setLayout(vertical_emergente)
    emerging_window.show()
def save():
    global cars
    try:
        with open('cars_database.json','r',encoding = 'utf-8') as file:
            cars = json.load(file)
    except:
        cars = []
    new_cars = {
            'marca':type_brand.text(),
            'modelo':type_model.text(),
            'color':type_colour.text(),
            'año':type_year.text(),
            'precio':type_price.text(),
            'vendido':False
    }
    cars.append(new_cars)
    with open('cars_database.json','w',encoding = 'utf-8') as file:
        json.dump(cars, file, indent= 4, ensure_ascii = False)
    print_info(new_cars)
def print_info(new_cars):
    rows = table.rowCount()
    table.insertRow(rows)
    table.setItem(rows,0,QTableWidgetItem(type_brand.text()))
    table.setItem(rows,1,QTableWidgetItem(type_model.text()))
    table.setItem(rows,2,QTableWidgetItem(type_colour.text()))
    table.setItem(rows,3,QTableWidgetItem(type_year.text()))
    table.setItem(rows,4,QTableWidgetItem(type_price.text()))
    emerging_window.close()
    type_brand.clear()
    type_model.clear()
    type_colour.clear()
    type_year.clear()
    type_price.clear()
def load_data():
    try:
        with open('cars_database.json','r',encoding = 'utf-8')as file:
            return json.load(file)
    except:
        data = []
    for car in data:
        if 'vendido' not in data:
            car['vendido'] = False
    return data
def load_info():
    global count
    global car
    count = 0
    table.setRowCount(0)    
    for car in cars:
        if car.get('vendido',False) == False:
            rows= table.rowCount()
            table.insertRow(rows)
            table.setItem(rows,0,QTableWidgetItem(car['marca']))
            table.setItem(rows,1,QTableWidgetItem(car['modelo']))
            table.setItem(rows,2,QTableWidgetItem(car['color']))
            table.setItem(rows,3,QTableWidgetItem(car['año']))
            table.setItem(rows,4,QTableWidgetItem(car['precio']))
            count += 1
        else:
            print('Vendido')
def sell_car():
    global count
    current_row = table.currentRow()
    print(current_row)
    del cars[current_row]
    table.removeRow(current_row)
    count-=1
    print(count)
cars = load_data()
load_info()
add_button.clicked.connect(new_window)
sell_button.clicked.connect(sell_car)
window.show()
app.exec_()