import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from datetime import datetime
import mysql.connector

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomeScreen.ui", self)
        self.pushButton.clicked.connect(self.nextPage)


    def nextPage(self):
        try:
            nextPage = Home()
            widget.addWidget(nextPage)
            widget.setCurrentIndex(widget.currentIndex()+1)
        except Exception as e:
            print(f"TIDAK BISA KE HALAMAN HOME: {e}")

class Home(QDialog):
    def __init__(self):
        super(Home, self).__init__()
        loadUi("home.ui", self)
        self.loaddata()
        self.tampilkanData()
        self.tableWidget.clicked.connect(self.pilihItem)
        self.pushButton_kembali.clicked.connect(self.kembali)
        self.pushButton_tambahData.clicked.connect(self.tambahData)
        self.pushButton_perbaruiData.clicked.connect(self.perbaruiData)
        self.pushButton_hapusData.clicked.connect(self.hapusData)
        self.mataKuliah = 0

    def loaddata(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            db="tubespbo",
            # use_pure=True #Tambahkan ini jika menggunakan MySQL langsung di localhost (tanpa XAMPP)
        )
        cursor = con.cursor()
        sql = "SELECT * FROM listtugas ORDER BY Deadline ASC"
        cursor.execute(sql)
        self.results = cursor.fetchall()

    def tampilkanData(self):
        self.tableWidget.setHorizontalHeaderLabels(["Mata Kuliah", "Judul Tugas", "Deadline", "Keterangan"])
        self.tableWidget.setColumnWidth(0, 280)
        self.tableWidget.setColumnWidth(1, 330)
        self.tableWidget.setColumnWidth(2, 220)
        self.tableWidget.setColumnWidth(3, 400)

        self.tableWidget.setRowCount(len(self.results))
        tablerow = 0
        for data in self.results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(data[1]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(data[2]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(data[3])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(data[4]))
            tablerow+=1

    def pilihItem(self):
        baris = self.tableWidget.currentRow()
        self.mataKuliah = self.tableWidget.item(baris, 0).text()
        self.judulTugas = self.tableWidget.item(baris, 1).text()
        self.deadline = self.tableWidget.item(baris, 2).text()
        self.keterangan = self.tableWidget.item(baris, 3).text()

    def kembali(self):
        try:
            Kembali = WelcomeScreen()
            widget.addWidget(Kembali)
            widget.setCurrentIndex(widget.currentIndex()+1)
        except:
            print("TIDAK BISA KEMBALI KE WELCOME SCREEN")

    def tambahData(self):
        try:
            tambahData = TambahData()
            widget.addWidget(tambahData)
            widget.setCurrentIndex(widget.currentIndex()+1)
        except:
            print("TIDAK BISA KE HALAMAN TAMBAH DATA")

    def perbaruiData(self):
        try:
            if (type(self.mataKuliah) == str):
                    perbaruiData = PerbaruiData(self.mataKuliah, self.judulTugas, self.deadline, self.keterangan)
                    widget.addWidget(perbaruiData)
                    widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                self.informationError()
        except:
            print("TIDAK BISA KE HALAMAN PERBARUI DATA")

    def hapusData(self):
        try:
            if (type(self.mataKuliah) == str):
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    db="tubespbo"
                )
                cursor = con.cursor()

                sql = ("DELETE FROM listtugas WHERE Mata_kuliah=%s AND Judul_tugas=%s AND Deadline=%s AND Keterangan=%s")
                value = self.mataKuliah, self.judulTugas, self.deadline, self.keterangan

                cursor.execute(sql, value)
                con.commit()

                self.informationHapus()
                self.loaddata()
                self.tampilkanData()
            else:
                self.informationError()
        except Exception as e:
            return e

    def informationError(self):
        info = QMessageBox()
        info.setIcon(QMessageBox.Critical)
        info.setWindowTitle("Informasi")
        info.setText("PILIH DATA TERLEBIH DAHULU")
        info.exec_()

    def informationHapus(self):
        info = QMessageBox()
        info.setIcon(QMessageBox.Warning)
        info.setWindowTitle("Informasi")
        info.setText("DATA BERHASIL DI HAPUS")
        info.exec_()

#HALAMAN TAMBAH DATA
class TambahData(QDialog):
    def __init__ (self):
        super(TambahData, self).__init__()
        loadUi("tambahData.ui", self)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.pushButton_kembali.clicked.connect(self.kembaliHome)
        self.pushButton_hapus.clicked.connect(self.hapus)
        self.pushButton_simpan.clicked.connect(lambda : [self.tambahData(), self.informationTambah(), self.kembaliHome()])

    def kembaliHome(self):
        try:
            KembaliHome = Home()
            widget.addWidget(KembaliHome)
            widget.setCurrentIndex(widget.currentIndex()+1)
        except:
            print("TIDAK BISA KE KEMBALI KE HOME")

    def hapus(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.lineEdit_3.clear()

    def tambahData(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                db="tubespbo"
            )
            cursor = con.cursor()

            mataKuliah = self.lineEdit.text()
            judulTugas = self.lineEdit_2.text()
            deadline = self.dateEdit.date().toString("yyyy/MM/dd")
            keterangan = self.lineEdit_3.text()

            sql = "INSERT INTO listtugas (Mata_kuliah, Judul_tugas, Deadline, Keterangan) VALUES (%s, %s, %s, %s)"
            value = (mataKuliah, judulTugas, deadline, keterangan)

            data = cursor.execute(sql, value)
            con.commit()
        except Exception as e:
            return e

    def informationTambah(self):
        info = QMessageBox()
        info.setIcon(QMessageBox.Information)
        info.setWindowTitle("Informasi")
        info.setText("DATA BERHASIL DI TAMBAHKAN")
        info.exec_()

#HALAMAN UPDATE DATA
class PerbaruiData(QDialog):
    def __init__ (self, mataKuliah, judulTugas, deadline, keterangan):
        super(PerbaruiData, self).__init__()
        loadUi("perbaruiData.ui", self)
        self.pushButton_kembali.clicked.connect(self.kembaliHome)
        self.pushButton_hapus.clicked.connect(self.hapus)
        self.pushButton_simpan.clicked.connect(lambda : [self.perbaruiData(), self.informationPerbarui(), self.kembaliHome()])

        self.mataKuliah = mataKuliah
        self.judulTugas = judulTugas
        self.deadline = datetime.strptime(deadline,'%Y-%m-%d')
        self.deadlineString = "{}/{}/{}".format(self.deadline.year, self.deadline.month, self.deadline.day)
        self.keterangan = keterangan

        self.lineEdit.setText(self.mataKuliah)
        self.lineEdit_2.setText(self.judulTugas)
        self.dateEdit.setDateTime(self.deadline)
        self.lineEdit_3.setText(self.keterangan)

    def kembaliHome(self):
        try:
            KembaliHome = Home()
            widget.addWidget(KembaliHome)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except:
            print("TIDAK BISA KE KEMBALI KE HOME")

    def hapus(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.lineEdit_3.clear()

    def perbaruiData(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                db="tubespbo"
            )
            cursor = con.cursor()

            mataKuliah = self.lineEdit.text()
            judulTugas = self.lineEdit_2.text()
            deadline = self.dateEdit.date().toString("yyyy/MM/dd")
            keterangan = self.lineEdit_3.text()

            sql = ("UPDATE listtugas SET Mata_kuliah=%s, Judul_tugas=%s, Deadline=%s, Keterangan=%s WHERE Mata_kuliah=%s AND Judul_tugas=%s AND Deadline=%s AND Keterangan=%s")
            value = (mataKuliah, judulTugas, deadline, keterangan, self.mataKuliah, self.judulTugas, self.deadlineString, self.keterangan)

            cursor.execute(sql, value)
            con.commit()
        except Exception as e:
            return e

    def informationPerbarui(self):
        info = QMessageBox()
        info.setIcon(QMessageBox.Information)
        info.setWindowTitle("Informasi")
        info.setText("DATA BERHASIL DI PERBARUI")
        info.exec_()

app = QApplication(sys.argv)
mainwindow = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.setWindowIcon(QtGui.QIcon("logoAplikasi.png"))
widget.addWidget(mainwindow)
widget.setFixedWidth(1080)
widget.setFixedHeight(720)
widget.show()
sys.exit(app.exec_())