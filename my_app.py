from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QPushButton, QLabel, QLineEdit, QTableWidgetItem
from random import *
import json 
def cargar_datos():
    with open('cars_database.json','r',encoding= 'utf-8') as archivo:
        datos = json.load(archivo)
    return datos
def cambio_ventana():
    ventana_emergente1.show()
    ventana_emergente2.hide()
cantidad = randint(3,9)
datos = cargar_datos()
def coche_aleatorio(datos,cantidad):
    cargar_datos()
    coches = []
    for i in range(cantidad):
        modelo = choice(list(datos.keys()))
        carroceria = choice(list(datos[modelo].keys()))
        version = choice(list(datos[modelo][carroceria]["versiones"].keys()))
        color = choice(datos[modelo][carroceria]["colores"])
        precio = datos[modelo][carroceria]["versiones"][version]["precio"]

        coches.append((modelo, carroceria, version, color, precio))

    return coches
def agregar_coche(tabla, modelo, carroceria, version, color, precio):
    fila = tabla.rowCount()
    tabla.insertRow(fila)
    tabla.setItem(fila, 0, QTableWidgetItem(modelo))
    tabla.setItem(fila, 1, QTableWidgetItem(carroceria))
    tabla.setItem(fila, 2, QTableWidgetItem(version))
    tabla.setItem(fila, 3, QTableWidgetItem(color))
    tabla.setItem(fila, 4, QTableWidgetItem(str(precio)))
def comprobar_inventario(tabla, modelo, carroceria, version, color):
    for fila in range(tabla.rowCount()):
        item_modelo = tabla.item(fila, 0)
        item_carroceria = tabla.item(fila, 1)
        item_version = tabla.item(fila, 2)

        # Comprobamos que los QTableWidgetItem no sean None
        if item_modelo and item_carroceria and item_version:
            if (item_modelo.text() == modelo and
                item_carroceria.text() == carroceria and
                item_version.text() == version):
                return True
    return False
    
def requests():
    global dias

    # Generar 3 coches aleatorios
    solicitudes = coche_aleatorio(datos, 3)

    # Solicitud 1
    modelo, carroceria, version, color, precio = solicitudes[0]
    texto_ventana1_2.setText(modelo + " " + carroceria + " " + version)
    if comprobar_inventario(tabla, modelo, carroceria, version):
        texto_ventana1_2.setStyleSheet("text-decoration: underline;")
    else:
        texto_ventana1_2.setStyleSheet("")

    # Solicitud 2
    modelo, carroceria, version, color, precio = solicitudes[1]
    texto_ventana1_3.setText(modelo + " " + carroceria + " " + version)
    if comprobar_inventario(tabla, modelo, carroceria, version):
        texto_ventana1_3.setStyleSheet("text-decoration: underline;")
    else:
        texto_ventana1_3.setStyleSheet("")

    # Solicitud 3
    modelo, carroceria, version, color, precio = solicitudes[2]
    texto_ventana1_4.setText(modelo + " " + carroceria + " " + version)
    if comprobar_inventario(tabla, modelo, carroceria, version):
        texto_ventana1_4.setStyleSheet("text-decoration: underline;")
    else:
        texto_ventana1_4.setStyleSheet("")

    # Actualizar día
    dias += 1
    texto_ventana1_1.setText("Día: " + str(dias))
        
# --- Aplicación ---
app = QApplication([])

# --- Ventana principal ---
ventana = QWidget()
ventana.setWindowTitle("Simulador de concesionario de coches")
ventana.resize(400,400)

# Widgets
tabla = QTableWidget()
tabla.setColumnCount(5)
tabla.setHorizontalHeaderLabels([
    'Marca','Modelo','Versión','Color','Precio'
])
boton_clientes = QPushButton("Solicitudes de clientes")
boton_guardar = QPushButton('Guardar datos')
boton_coches = QPushButton("Pedir vehículos")
boton_dia = QPushButton("Siguiente día")
boton_interes = QPushButton("Interés del cliente")
boton_pago = QPushButton("Método de pago")


texto1 = QLabel("Concesionario OM Motor")
texto2 = QLabel("Capital inicial:500000")
texto3 = QLabel("Capital actual:500000")
texto4 = QLabel("Tiempo")
texto5 = QLabel("0 semanas 0 días 1 mes")

num_coche = QLineEdit()
num_coche.setPlaceholderText("Introduce el número del coche a comprar")

# --- Layouts ventana principal ---
linea_principal = QHBoxLayout()
vertical1 = QVBoxLayout()
vertical2 = QVBoxLayout()
vertical3 = QVBoxLayout()

vertical1.addWidget(tabla)

vertical2.addWidget(texto1)
vertical2.addWidget(texto2)
vertical2.addWidget(texto3)
vertical2.addWidget(texto4)
vertical2.addWidget(texto5)

vertical3.addWidget(boton_clientes)
vertical3.addWidget(boton_guardar)
vertical3.addWidget(boton_coches)

linea_principal.addLayout(vertical1)
linea_principal.addLayout(vertical2)
linea_principal.addLayout(vertical3)

ventana.setLayout(linea_principal)

# --- Ventana emergente 1 ---
ventana_emergente1 = QDialog()
ventana_emergente1.setWindowTitle("Solicitudes de clientes")
ventana_emergente1.resize(400,400)
layout_emergente1 = QVBoxLayout()

texto_ventana1_1 = QLabel("Día: 1")
texto_ventana1_2 = QLabel("Solicitud 1:")
texto_ventana1_3 = QLabel("Solicitud 2:")
texto_ventana1_4 = QLabel("Solicitud 3:")
texto_ventana1_5 = QLabel("Interés del cliente: interesado")
texto_ventana1_6 = QLabel("Método de pago: contado")

layout_emergente1.addWidget(texto_ventana1_1)
layout_emergente1.addWidget(texto_ventana1_2)
layout_emergente1.addWidget(texto_ventana1_3)
layout_emergente1.addWidget(texto_ventana1_4)
layout_emergente1.addWidget(texto_ventana1_5)
layout_emergente1.addWidget(texto_ventana1_6)

# Botones en la ventana emergente
horizontal_emergente1 = QHBoxLayout()
horizontal_emergente1.addWidget(boton_dia)
horizontal_emergente1.addWidget(boton_interes)
horizontal_emergente1.addWidget(boton_pago)


principal_ventana1 = QVBoxLayout()
principal_ventana1.addLayout(layout_emergente1)
principal_ventana1.addLayout(horizontal_emergente1)

ventana_emergente1.setLayout(principal_ventana1)

# --- Ventana emergente 2 (financiamiento) ---
ventana_emergente2 = QDialog()
ventana_emergente2.setWindowTitle("Financiamiento")
ventana_emergente2.resize(400,400)
layout_emergente2 = QVBoxLayout()

texto_ventana2_1 = QLabel("Ingresos:")
texto_ventana2_2 = QLabel("Morosidad: no")
texto_ventana2_3 = QLabel("Meses a pagar:")
num_coche = QLineEdit('')
num_coche.setPlaceholderText('Ingresa el número del vehículo que quiere el cliente')
boton_confirmar = QPushButton('Confirmar pago')
layout_emergente2.addWidget(texto_ventana2_1)
layout_emergente2.addWidget(texto_ventana2_2)
layout_emergente2.addWidget(texto_ventana2_3)
layout_emergente2.addWidget(num_coche)
layout_emergente2.addWidget(boton_confirmar)
ventana_emergente2.setLayout(layout_emergente2)

# --- Funciones de los botones ---

boton_clientes.clicked.connect(cambio_ventana)
# --- Mostrar ventana principal ---
ventana.show()
app.exec_()

