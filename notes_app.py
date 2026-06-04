from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import os
import json

app = QApplication([])
# Ventana de aplicación
ventana_notas = QWidget()
# Cambiar titulo de ventana
ventana_notas.setWindowTitle("Notas Inteligentes")
# Cambiar tamaño de la ventana
ventana_notas.resize(900, 600)
 
# Widgets de la aplicación
editorTexto = QTextEdit()
label_notas = QLabel("Lista de notas")
lista_notas = QListWidget()
 
boton_crear_nota = QPushButton("Crear Nota")
boton_eliminar_nota = QPushButton("Eliminar Nota")
boton_guardar_nota = QPushButton("Guardar Nota")
 
label_etiquetas = QLabel("Lista de Etiquetas")
lista_etiquetas = QListWidget()
 
editor_etiqueta = QLineEdit("")
editor_etiqueta.setPlaceholderText("Ingresar etiqueta...")
 
boton_anadir = QPushButton("Añadir a nota")
boton_eliminar_etiqueta = QPushButton("Eliminar etiqueta de nota")
boton_buscar = QPushButton("Buscar notas por etiqueta")
 
# Organización de widgets
horizontal_principal = QHBoxLayout()
vertical_1 = QVBoxLayout()
vertical_2 = QVBoxLayout()
 
vertical_1.addWidget(editorTexto)
 
vertical_2.addWidget(label_notas)
vertical_2.addWidget(lista_notas)
 
horizontal1 = QHBoxLayout()
horizontal1.addWidget(boton_crear_nota)
horizontal1.addWidget(boton_eliminar_nota)
 
vertical_2.addLayout(horizontal1)
vertical_2.addWidget(boton_guardar_nota)
 
vertical_2.addWidget(label_etiquetas)
vertical_2.addWidget(lista_etiquetas)
vertical_2.addWidget(editor_etiqueta)
 
horizontal2 = QHBoxLayout()
horizontal2.addWidget(boton_anadir)
horizontal2.addWidget(boton_eliminar_etiqueta)
 
vertical_2.addLayout(horizontal2)
vertical_2.addWidget(boton_buscar)
 
horizontal_principal.addLayout(vertical_1, stretch = 2)
horizontal_principal.addLayout(vertical_2, stretch = 1)
 
ventana_notas.setLayout(horizontal_principal)
 
 
ventana_notas.show()
 
 
try:
    with open("notes_data.json", "r", encoding="utf-8") as file:
        notas = json.load(file)
except:
    notas = {
        "Bienvenido":{
            "texto": "Esto es una aplicación de notas inteligentes",
            "etiquetas":["Notas","Telefono"]
        }
    }

    with open("notes_data.json", "w", encoding="utf-8") as file:
        json.dump(notas, file, sort_keys=True, ensure_ascii=False)
# Funcionalidad de la app: Funciones
def mostrar_nota():
    if lista_notas.selectedItems():
        palabraClaveClicada = lista_notas.selectedItems()[0].text()
        texto = notas[palabraClaveClicada]["texto"]
        editorTexto.setText(texto)

        etiquetas = notas[palabraClaveClicada]["etiquetas"]
        lista_etiquetas.clear()
        lista_etiquetas.addItems(etiquetas)
 
 
def crear_nota():
    nombre_nota, ok = QInputDialog.getText(ventana_notas, "Añadir nota", "Nombre de la nota")
    print(nombre_nota)
    if ok and nombre_nota != "":
        notas[nombre_nota] = {"texto":"", "etiquetas": []}
        lista_notas.addItem(nombre_nota)
        lista_etiquetas.addItems(notas[nombre_nota]["etiquetas"])
 
 
def guardar_nota():
    if lista_notas.selectedItems():
        palabraClaveClicada = lista_notas.selectedItems()[0].text()
        texto = editorTexto.toPlainText()
        notas[palabraClaveClicada]["texto"] = texto
        with open("notes_data.json", "w", encoding = "utf-8") as file:
            json.dump(notas, file, sort_keys = True, ensure_ascii = False)
    else:
        print("La nota a guardar no está seleccionada")
 
def eliminar_nota():
    if lista_notas.selectedItems():
        palabraClaveClicada = lista_notas.selectedItems()[0].text()
        del notas[palabraClaveClicada]
        lista_notas.clear()
        lista_notas.addItems(notas)
        lista_etiquetas.clear()
        editorTexto.clear()
        with open("notes_data.json", "w", encoding = 'utf-8') as file:
            json.dump(notas, file, sort_keys = True, ensure_ascii = False)
    else:
        print("La nota a eliminar no está seleccionada")  
 
 
def anadir_etiqueta():
    if lista_notas.selectedItems():
        palabraClaveClicada = lista_notas.selectedItems()[0].text()
        etiqueta = editor_etiqueta.text()
        if not etiqueta in notas[palabraClaveClicada]["etiquetas"]:
            notas[palabraClaveClicada]["etiquetas"].append(etiqueta)
            lista_etiquetas.addItem(etiqueta)
            editor_etiqueta.clear()
 
        with open("notes_data.json", "w", encoding = "utf-8") as file:
            json.dump(notas, file, sort_keys = True, ensure_ascii = False)
    else:
        print("La nota para añadir una etiqueta no está seleccionada")  
 
def eliminar_etiqueta():
    if lista_notas.selectedItems() and lista_etiquetas.selectedItems():
        palabraClaveClicada = lista_notas.selectedItems()[0].text()
        etiquetaClicada = lista_etiquetas.selectedItems()[0].text()
        notas[palabraClaveClicada]['etiquetas'].remove(etiquetaClicada)
        lista_etiquetas.clear()
        lista_etiquetas.addItems(notas[palabraClaveClicada]['etiquetas'])

        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notas, file, sort_keys=True, ensure_ascii=False)
 
def buscar_etiqueta():
    busqueda = editor_etiqueta.text()
    if boton_buscar.text() == 'Buscar notas por etiqueta' and busqueda:
        notas_filtradas = {}
        for nota in notas:
            if busqueda in notas[nota]['etiquetas']:
                notas_filtradas[nota] = notas[nota]
        lista_notas.clear()
        lista_etiquetas.clear()
        lista_notas.addItems(notas_filtradas.keys())
        boton_buscar.setText('Limpiar búsqueda')
    elif boton_buscar.text() == 'Limpiar búsqueda':
        editor_etiqueta.clear()
        lista_notas.clear()
        lista_etiquetas.clear()
        lista_notas.addItems(notas)
        boton_buscar.setText('Buscar notas por etiqueta')
 
# Manejo de eventos
lista_notas.itemClicked.connect(mostrar_nota)
boton_crear_nota.clicked.connect(crear_nota)
boton_guardar_nota.clicked.connect(guardar_nota)
boton_eliminar_nota.clicked.connect(eliminar_nota)
boton_anadir.clicked.connect(anadir_etiqueta)
boton_eliminar_etiqueta.clicked.connect(eliminar_etiqueta)
boton_buscar.clicked.connect(buscar_etiqueta)
 
 

with open("notes_data.json", "r", encoding = "utf-8") as file:
    notas = json.load(file)

lista_notas.addItems(notas)
app.exec_()
 
