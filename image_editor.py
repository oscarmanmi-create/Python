#¡Crear aquí el editor de fotografías Editor simple!
#¡Crear aquí el editor de fotografías Editor simple!
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image
from PIL import ImageFilter
import os

class Foto():
    def __init__(self):
        self.nombre = None
        self.foto = None
        self.directorio = None
    def cargar_foto(self, nombre, directorio):
        self.directorio = directorio
        self.nombre = nombre
        ruta_imagen = os.path.join(self.directorio,self.nombre)
        self.foto = Image.open(ruta_imagen)
    def mostrar_foto(self,path):
        imagen.hide()
        pixmapimage = QPixmap(path)
        w, h = imagen.width(), imagen.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        imagen.setPixmap(pixmapimage)
        imagen.show()
    def saveImage(self):
        ruta_imagen = os.path.join(self.directorio,'modificado')
        if os.path.exists(ruta_imagen) or os.path.isdir(ruta_imagen):
            print('Ya existe la carpeta')
        else:
            os.mkdir(ruta_imagen)
        ruta_guardado = os.path.join(ruta_imagen, self.nombre)
        self.foto.save(ruta_guardado)
    def do_bw(self):
        self.foto = self.foto.convert('L')
        self.saveImage()
        ruta_imagen = os.path.join(self.directorio,'modificado')
        ruta_guardado = os.path.join(ruta_imagen, self.nombre)
        self.mostrar_foto(ruta_guardado)
    def girar_izquierda(self):
        self.foto = self.foto.transpose(Image.ROTATE_90)
        self.saveImage()
        ruta_imagen = os.path.join(self.directorio,'modificado')
        ruta_guardado = os.path.join(ruta_imagen, self.nombre)
        self.mostrar_foto(ruta_guardado)
    def girar_derecha(self):
        self.foto = self.foto.transpose(Image.ROTATE_270)
        self.saveImage()
        ruta_imagen = os.path.join(self.directorio,'modificado')
        ruta_guardado = os.path.join(ruta_imagen, self.nombre)
        self.mostrar_foto(ruta_guardado)
    def reflejo(self):
        self.foto = self.foto.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        ruta_imagen = os.path.join(self.directorio,'modificado')
        ruta_guardado = os.path.join(ruta_imagen, self.nombre)
        self.mostrar_foto(ruta_guardado)
    def nitidez(self):
        self.foto = self.foto.filter(ImageFilter.SHARPEN)
        self.saveImage()
        ruta_imagen = os.path.join(self.directorio,'modificado')
        ruta_guardado = os.path.join(ruta_imagen, self.nombre)
        self.mostrar_foto(ruta_guardado)
   
       

   




app = QApplication([])
ventana = QWidget()
ventana.show()
ventana.resize(700, 500)
ventana.setWindowTitle('Editor Simple')
 
boton_carpeta = QPushButton('Carpeta')
lista_imagenes = QListWidget()
imagen = QLabel('Imagen')
boton_izquierda = QPushButton('Izquierda')
boton_derecha = QPushButton('Derecha')
boton_reflejo = QPushButton('Reflejo')
boton_nitidez = QPushButton('Nitidez')
boton_bn = QPushButton('B/N')
 
vertical1 = QVBoxLayout()
vertical2 = QVBoxLayout()
 
vertical1.addWidget(boton_carpeta)
vertical1.addWidget(lista_imagenes)
 
linea_botones = QHBoxLayout()
linea_botones.addWidget(boton_izquierda)
linea_botones.addWidget(boton_derecha)
linea_botones.addWidget(boton_reflejo)
linea_botones.addWidget(boton_nitidez)
linea_botones.addWidget(boton_bn)
 
vertical2.addWidget(imagen)
vertical2.addLayout(linea_botones)
 
horizontal = QHBoxLayout()
horizontal.addLayout(vertical1, stretch = 20)
horizontal.addLayout(vertical2, stretch = 80)
 
ventana.setLayout(horizontal)
 
directorio = ''
 
def seleccionar_directorio():
    global directorio
    directorio = QFileDialog.getExistingDirectory()
 
def filtrar(archivos):
    imagenes = []
    for archivo in archivos:
        for extension in ['.jpg', '.png', '.jpeg', '.gif', '.tiff', '.bmp','.webp']:
            if archivo.endswith(extension):
                imagenes.append(archivo)
    return imagenes

def listar_imagenes():
    seleccionar_directorio()
    archivos = os.listdir(directorio)
    imagenes = filtrar(archivos)
    lista_imagenes.clear()
    for imagen in imagenes:
        lista_imagenes.addItem(imagen)
foto1 = Foto()
def mostrar_foto_elegida():
    try:
        if lista_imagenes.currentRow() >= 0:
            nombre = lista_imagenes.currentItem().text()
            foto1.cargar_foto(nombre, directorio)
            ruta_completa = os.path.join(foto1.directorio, foto1.nombre)
            foto1.mostrar_foto(ruta_completa)
    except:
        mensaje_error = QMessageBox()
        mensaje_error.setText('No se puede abrir este archivo')
        mensaje_error.exec_()
lista_imagenes.currentRowChanged.connect(mostrar_foto_elegida)      
boton_carpeta.clicked.connect(listar_imagenes)
boton_bn.clicked.connect(foto1.do_bw)
boton_derecha.clicked.connect(foto1.girar_derecha)
boton_izquierda.clicked.connect(foto1.girar_izquierda)
boton_reflejo.clicked.connect(foto1.reflejo)
boton_nitidez.clicked.connect(foto1.nitidez)
app.exec_()
 