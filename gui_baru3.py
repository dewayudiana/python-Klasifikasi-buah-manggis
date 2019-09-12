# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_baru3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from keras.models import load_model
import numpy as np
from keras.preprocessing import image
import math
from glob import glob
from PIL import Image
from skimage import io, transform, morphology, exposure
from skimage.transform import rotate
from skimage.color import rgb2gray
from skimage.io import imsave
from skimage.filters import threshold_otsu
from skimage.morphology import watershed, binary_erosion, binary_closing, binary_dilation

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
import os


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 720)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.CitraAwal = QtWidgets.QLabel(Form)
        self.CitraAwal.setMinimumSize(QtCore.QSize(300, 300))
        self.CitraAwal.setMaximumSize(QtCore.QSize(300, 300))
        self.CitraAwal.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.CitraAwal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CitraAwal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.CitraAwal.setText("")
        self.CitraAwal.setScaledContents(True)
        self.CitraAwal.setObjectName("CitraAwal")
        self.verticalLayout_3.addWidget(self.CitraAwal)
        self.OpenImage = QtWidgets.QPushButton(Form)
        self.OpenImage.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.OpenImage.setObjectName("OpenImage")
        self.verticalLayout_3.addWidget(self.OpenImage)
        self.Klasifikasi = QtWidgets.QPushButton(Form)
        self.Klasifikasi.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Klasifikasi.setObjectName("Klasifikasi")
        self.verticalLayout_3.addWidget(self.Klasifikasi)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 0 )
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setMinimumSize(QtCore.QSize(100, 30))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setMinimumSize(QtCore.QSize(100, 30))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setMinimumSize(QtCore.QSize(100, 30))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(100, 30))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setMinimumSize(QtCore.QSize(100, 30))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setMinimumSize(QtCore.QSize(100, 30))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        self.CitraHasil = QtWidgets.QLabel(self.groupBox)
        self.CitraHasil.setMinimumSize(QtCore.QSize(150, 150))
        self.CitraHasil.setMaximumSize(QtCore.QSize(150, 150))
        self.CitraHasil.setText("")
        self.CitraHasil.setScaledContents(True)
        self.CitraHasil.setObjectName("CitraHasil")
        self.gridLayout.addWidget(self.CitraHasil, 3, 3, 1, 1)
        self.CitraMasking = QtWidgets.QLabel(self.groupBox)
        self.CitraMasking.setMinimumSize(QtCore.QSize(150, 150))
        self.CitraMasking.setMaximumSize(QtCore.QSize(150, 150))
        self.CitraMasking.setText("")
        self.CitraMasking.setScaledContents(True)
        self.CitraMasking.setObjectName("CitraMasking")
        self.gridLayout.addWidget(self.CitraMasking, 3, 2, 1, 1)
        self.CitraMorphologi = QtWidgets.QLabel(self.groupBox)
        self.CitraMorphologi.setMinimumSize(QtCore.QSize(150, 150))
        self.CitraMorphologi.setMaximumSize(QtCore.QSize(150, 150))
        self.CitraMorphologi.setText("")
        self.CitraMorphologi.setScaledContents(True)
        self.CitraMorphologi.setObjectName("CitraMorphologi")
        self.gridLayout.addWidget(self.CitraMorphologi, 3, 1, 1, 1)
        self.CitraBiner = QtWidgets.QLabel(self.groupBox)
        self.CitraBiner.setMinimumSize(QtCore.QSize(150, 150))
        self.CitraBiner.setMaximumSize(QtCore.QSize(150, 150))
        self.CitraBiner.setText("")
        self.CitraBiner.setScaledContents(True)
        self.CitraBiner.setObjectName("CitraBiner")
        self.gridLayout.addWidget(self.CitraBiner, 1, 3, 1, 1)
        self.CitraGrayscale = QtWidgets.QLabel(self.groupBox)
        self.CitraGrayscale.setMinimumSize(QtCore.QSize(150, 150))
        self.CitraGrayscale.setMaximumSize(QtCore.QSize(150, 150))
        self.CitraGrayscale.setText("")
        self.CitraGrayscale.setScaledContents(True)
        self.CitraGrayscale.setObjectName("CitraGrayscale")
        self.gridLayout.addWidget(self.CitraGrayscale, 1, 2, 1, 1)
        self.CitraAwal2 = QtWidgets.QLabel(self.groupBox)
        self.CitraAwal2.setMinimumSize(QtCore.QSize(150, 150))
        self.CitraAwal2.setMaximumSize(QtCore.QSize(150, 150))
        self.CitraAwal2.setText("")
        self.CitraAwal2.setScaledContents(True)
        self.CitraAwal2.setObjectName("CitraAwal2")
        self.gridLayout.addWidget(self.CitraAwal2, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LabelKeterangan = QtWidgets.QLabel(self.groupBox_2)
        self.LabelKeterangan.setMinimumSize(QtCore.QSize(321, 141))
        self.LabelKeterangan.setMaximumSize(QtCore.QSize(321, 141))
        self.LabelKeterangan.setFrameShape(QtWidgets.QFrame.Box)
        self.LabelKeterangan.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LabelKeterangan.setText("")
        self.LabelKeterangan.setScaledContents(True)
        self.LabelKeterangan.setWordWrap(True)
        self.LabelKeterangan.setObjectName("LabelKeterangan")
        self.gridLayout_2.addWidget(self.LabelKeterangan, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setMinimumSize(QtCore.QSize(100, 30))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 0, 1, 1, 1)
        self.LabelPersentase = QtWidgets.QLabel(self.groupBox_2)
        self.LabelPersentase.setMinimumSize(QtCore.QSize(141, 141))
        self.LabelPersentase.setMaximumSize(QtCore.QSize(121, 141))
        self.LabelPersentase.setFrameShape(QtWidgets.QFrame.Box)
        self.LabelPersentase.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LabelPersentase.setText("")
        self.LabelPersentase.setScaledContents(True)
        self.LabelPersentase.setWordWrap(True)
        self.LabelPersentase.setObjectName("LabelPersentase")
        self.gridLayout_2.addWidget(self.LabelPersentase, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setMinimumSize(QtCore.QSize(100, 30))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.OpenImage.clicked.connect(self.buka_file)
        self.Klasifikasi.clicked.connect(self.klasifikasi)
        self.Inisial()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "APLIKASI KLASIFIKASI BUAH MANGGIS"))
        self.OpenImage.setText(_translate("Form", "Open Image"))
        self.Klasifikasi.setText(_translate("Form", "Klasifikasi"))
        self.groupBox.setTitle(_translate("Form", "Segmentasi"))
        self.label_9.setText(_translate("Form", "Citra Awal"))
        self.label_14.setText(_translate("Form", "Proses Morphologi"))
        self.label_10.setText(_translate("Form", "Proses Grayscale"))
        self.label_13.setText(_translate("Form", "Hasil Segmentasi"))
        self.label_11.setText(_translate("Form", "Proses Binarisasi"))
        self.label_21.setText(_translate("Form", "Proses Masking"))
        self.groupBox_2.setTitle(_translate("Form", "Hasil"))
        self.label_20.setText(_translate("Form", "Keterangan"))
        self.label_15.setText(_translate("Form", "Persentase"))


    def Inisial(self):
        path_default = 'default_img.png'
        defpx = QImage(path_default)
        self.CitraAwal.setPixmap(QPixmap.fromImage(defpx))
        self.CitraAwal2.setPixmap(QPixmap.fromImage(defpx))
        self.CitraBiner.setPixmap(QPixmap.fromImage(defpx))
        self.CitraGrayscale.setPixmap(QPixmap.fromImage(defpx))
        self.CitraMasking.setPixmap(QPixmap.fromImage(defpx))
        self.CitraMorphologi.setPixmap(QPixmap.fromImage(defpx))
        self.CitraHasil.setPixmap(QPixmap.fromImage(defpx))

    def buka_file(self):
        # print('buka')
        global imagePath
        imagePath, _ = QtWidgets.QFileDialog.getOpenFileName()
        pixmap = QtGui.QPixmap(imagePath)
        pixmap = pixmap.scaledToHeight(195)
        pixmap = pixmap.scaledToWidth(225)
        self.CitraAwal.setPixmap(pixmap)

    def klasifikasi(self):
        self.progressBar.setValue(0)
        plt.figure(facecolor='w', edgecolor='k')
        plt.axis('off')
        global imagePath
        img_awal = io.imread(imagePath)
        pixmap = QtGui.QPixmap(imagePath)
        self.CitraAwal2.setPixmap(pixmap)
        self.progressBar.setValue(10)


#grayscale
        grayscale = rgb2gray(img_awal)
        #show
        plt.imshow(grayscale, cmap=plt.cm.gray)
        path_grayscale = 'preprocessing/img_grayscale.png'
        plt.savefig(path_grayscale, transparent = True, bbox_inches = 'tight', pad_inches = 0)
        img_grayscaleQ = QImage(path_grayscale)
        self.CitraGrayscale.setScaledContents(1)
        self.CitraGrayscale.setPixmap(QPixmap.fromImage(img_grayscaleQ))
#binary
        global_thresh = threshold_otsu(grayscale) #membuat threshold
        binary_global = grayscale == 1
        #show
        plt.imshow(binary_global, cmap=plt.cm.gray)
        path_binary_global = 'preprocessing/img_binary_gobal.png'
        plt.savefig(path_binary_global, transparent = True, bbox_inches = 'tight', pad_inches = 0)
        img_binary_globalQ = QImage(path_binary_global)
        self.CitraBiner.setScaledContents(1)
        self.CitraBiner.setPixmap(QPixmap.fromImage(img_binary_globalQ))

#morpologi 
        img_fix_noise = morphology.remove_small_objects(~binary_global, min_size=10000, connectivity=8)
        img_fix_hole = morphology.remove_small_holes(img_fix_noise,area_threshold=10000, connectivity=4, in_place=False, min_size=None)
        selem = np.ones((5, 5)) #kernel untuk erosi
        img_closing = morphology.opening(img_fix_hole,selem)
        #show
        plt.imshow(img_fix_noise, cmap=plt.cm.gray)
        path_morphology = 'preprocessing/img_morphology.png'
        plt.savefig(path_morphology, transparent = True, bbox_inches = 'tight', pad_inches = 0)
        img_morphologyQ = QImage(path_morphology)
        self.CitraMorphologi.setScaledContents(1)
        self.CitraMorphologi.setPixmap(QPixmap.fromImage(img_morphologyQ))

        #show
        plt.imshow(img_closing, cmap=plt.cm.gray)
        path_masking = 'preprocessing/img_masking.png'
        plt.savefig(path_masking, transparent = True, bbox_inches = 'tight', pad_inches = 0)
        img_maskingQ = QImage(path_masking)
        self.CitraMasking.setScaledContents(1)
        self.CitraMasking.setPixmap(QPixmap.fromImage(img_maskingQ))

#hasil Segmentasi
        img_segmented = img_awal.copy()
        img_segmented[img_closing == 0] = False
        #show
        plt.imshow(img_segmented, cmap=plt.cm.gray)
        path_CitraHasil = 'preprocessing/img_CitraHasil.png'
        plt.savefig(path_CitraHasil, transparent = True, bbox_inches = 'tight', pad_inches = 0)
        img_CitraHasilQ = QImage(path_CitraHasil)
        self.CitraHasil.setScaledContents(1)
        self.CitraHasil.setPixmap(QPixmap.fromImage(img_CitraHasilQ))

        trained_model = load_model('model_manggis_adamEpoch80br.h5')
        img = image.load_img(imagePath, target_size=(200, 200))
        test_image = image.img_to_array(img)
        test_image = np.expand_dims(test_image, axis = 0)
        result = trained_model.predict(test_image)
    
        classes = [0, 1, 2 ,3 ,4 ,5 ,6]
        listHasil = []
        hasil = ''
        for i in range(len(classes)):
            listHasil.append('Kelas ' + str(classes[i]) + ': ' + str(math.floor(result[0][i] * 100)))
        print(listHasil)
        listshow = " %\n".join(map(str, listHasil))
        listshow2 = listshow + " %" 

        for i in range(len(listHasil)):
            tempt = listHasil[i]
            listHasil[i] = tempt[-6:]
        
        print(listHasil)


        for i in range(len(listHasil)-1,0,-1):
            for x in range(i):
                if(int(listHasil[x].split(": ")[1]) < int(listHasil[x+1].split(": ")[1])):
                    temp = listHasil[x]
                    listHasil[x] = listHasil[x+1]
                    listHasil[x+1] = temp
        hasil = listHasil[0].replace(":"," : ")
        print(listHasil)     


        deskripsi = [
            "- Warna kulit buah kuning kehijauan \n- Kulit buah masih banyak mengandung getah \n- Buah belum siap dipetik",
            "- Warna kulit buah hujau kekuningan \n- Buah belum tua dan getah masih banyak \n- Isi buah masih sulit dipisahkan dari daging \n- Buah belum siap dipanen",
            "- Warna kulit buah kuning kemerahan \n Bercak merah hampir merata \n- Buah hampir tua dan getah mulai berkurang \n- isi buah masih sulit dipisahkan dari daging",
            "- Warna kulit buah merah kecoklatan \n- Kulit buah masih bergetah \n Isi buah sudah dapat dipisahkan dari daging kulit \n- Buah disarankan dapat dipetik untuk tujuan ekspor",
            "- Warna kulit buah merah keunguan \n- Kulit buah masih sedikit bergetah \n- Isi buah sudah dapat dipisahkan dari daging kulit \n- Buah dapat dikonsumsi \n- Dapat dipetik untuk tujuan ekspor",
            "- Warna kulit buah ungu kemerahan \n- Buah mulai masak dan siap dikonsumsi \n- Getah telah hilang dan isi buah mudah dilepaskan \n- Buah lebih sesuai untuk pasar domestik",
            "- Warna kulit buah ungu kehitaman \n- Buah sudah masak \n- Buah sesuai untuk kebutuhan pasar domestik dan siap saji"
        
        ]

        self.LabelPersentase.setText(listshow2)
        self.LabelKeterangan.setText(deskripsi[int(hasil.split(":")[0].replace(" ",""))])

        self.progressBar.setValue(100)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

