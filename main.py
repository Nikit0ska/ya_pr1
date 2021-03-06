import shutil

import save
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import threading
import playsound
import wave
import pyaudio
import sqlite3
import db

is_recording = False

def record():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    filename = "tmp/tmp.wav"

    p = pyaudio.PyAudio()


    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []

    while True:
        global is_recording
        if not is_recording:
            break
        data = stream.read(chunk)
        frames.append(data)



    stream.stop_stream()
    stream.close()

    p.terminate()


    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()



class Ui_PianoForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_PianoForm, self).__init__()
    def setupUi(self):
        self.setObjectName("PianoForm")
        self.resize(662, 486)
        self.setMinimumSize(QtCore.QSize(621, 486))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.f4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.f4_2.setGeometry(QtCore.QRect(450, 130, 21, 91))
        self.f4_2.setStyleSheet("border: 2px solid #858585;\n"
"\n"
"    background-color:black ;\n"
"")
        self.f4_2.setText("")
        self.f4_2.setObjectName("f4_2")
        self.d3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.d3_2.setGeometry(QtCore.QRect(90, 130, 21, 91))
        self.d3_2.setStyleSheet("border: 2px solid #858585;\n"
"\n"
"    background-color:black ;\n"
"")
        self.d3_2.setText("")
        self.d3_2.setObjectName("d3_2")
        self.a4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.a4_2.setGeometry(QtCore.QRect(250, 130, 21, 91))
        self.a4_2.setStyleSheet("border: 2px solid #858585;\n"
"\n"
"    background-color:black ;\n"
"")
        self.a4_2.setText("")
        self.a4_2.setObjectName("a4_2")
        self.d4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.d4_2.setGeometry(QtCore.QRect(370, 130, 21, 91))
        self.d4_2.setStyleSheet("border: 2px solid #858585;\n"
"\n"
"    background-color:black ;\n"
"")
        self.d4_2.setText("")
        self.d4_2.setObjectName("d4_2")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(250, 20, 101, 71))
        self.stop.setObjectName("stop")
        self.f3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.f3_2.setGeometry(QtCore.QRect(170, 130, 21, 91))
        self.f3_2.setStyleSheet("border: 2px solid #858585;\n"
"\n"
"    background-color:black ;\n"
"")
        self.f3_2.setText("")
        self.f3_2.setObjectName("f3_2")
        self.d4 = QtWidgets.QPushButton(self.centralwidget)
        self.d4.setGeometry(QtCore.QRect(340, 130, 41, 151))
        self.d4.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.d4.setText("")
        self.d4.setObjectName("d4")
        self.e3 = QtWidgets.QPushButton(self.centralwidget)
        self.e3.setGeometry(QtCore.QRect(100, 130, 41, 151))
        self.e3.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.e3.setText("")
        self.e3.setObjectName("e3")
        self.a5_2 = QtWidgets.QPushButton(self.centralwidget)
        self.a5_2.setGeometry(QtCore.QRect(530, 130, 21, 91))
        self.a5_2.setStyleSheet("border: 2px solid #858585;\n"
"\n"
"    background-color:black ;\n"
"")
        self.a5_2.setText("")
        self.a5_2.setObjectName("a5_2")
        self.c4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.c4_2.setGeometry(QtCore.QRect(330, 130, 21, 91))
        self.c4_2.setStyleSheet("border: 2px solid #858585;\n"
"\n"
"    background-color:black ;\n"
"")
        self.c4_2.setText("")
        self.c4_2.setObjectName("c4_2")
        self.c4 = QtWidgets.QPushButton(self.centralwidget)
        self.c4.setGeometry(QtCore.QRect(300, 130, 41, 151))
        self.c4.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.c4.setText("")
        self.c4.setObjectName("c4")
        self.e4 = QtWidgets.QPushButton(self.centralwidget)
        self.e4.setGeometry(QtCore.QRect(380, 130, 41, 151))
        self.e4.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.e4.setText("")
        self.e4.setObjectName("e4")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(540, 130, 41, 151))
        self.b5.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.listen = QtWidgets.QPushButton(self.centralwidget)
        self.listen.setGeometry(QtCore.QRect(480, 20, 101, 71))
        self.listen.setObjectName("listen")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(260, 130, 41, 151))
        self.b4.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.a4 = QtWidgets.QPushButton(self.centralwidget)
        self.a4.setGeometry(QtCore.QRect(220, 130, 41, 151))
        self.a4.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.a4.setText("")
        self.a4.setObjectName("a4")
        self.g4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.g4_2.setGeometry(QtCore.QRect(490, 130, 21, 91))
        self.g4_2.setStyleSheet("border: 2px solid #858585;\n"
"\n"
"    background-color:black ;\n"
"")
        self.g4_2.setText("")
        self.g4_2.setObjectName("g4_2")
        self.f3 = QtWidgets.QPushButton(self.centralwidget)
        self.f3.setGeometry(QtCore.QRect(140, 130, 41, 151))
        self.f3.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.f3.setText("")
        self.f3.setObjectName("f3")
        self.c3 = QtWidgets.QPushButton(self.centralwidget)
        self.c3.setGeometry(QtCore.QRect(20, 130, 41, 151))
        self.c3.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.c3.setText("")
        self.c3.setObjectName("c3")
        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setGeometry(QtCore.QRect(250, 20, 101, 71))
        self.record.setObjectName("record")
        self.g4 = QtWidgets.QPushButton(self.centralwidget)
        self.g4.setGeometry(QtCore.QRect(460, 130, 41, 151))
        self.g4.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.g4.setText("")
        self.g4.setObjectName("g4")
        self.g3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.g3_2.setGeometry(QtCore.QRect(210, 130, 21, 91))
        self.g3_2.setStyleSheet("border: 2px solid #858585;\n"
"\n"
"    background-color:black ;\n"
"")
        self.g3_2.setText("")
        self.g3_2.setObjectName("g3_2")
        self.c3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.c3_2.setGeometry(QtCore.QRect(50, 130, 20, 91))
        self.c3_2.setStyleSheet("border: 2px solid #858585;\n"
"\n"
"    background-color:black ;\n"
"")
        self.c3_2.setText("")
        self.c3_2.setObjectName("c3_2")
        self.a5 = QtWidgets.QPushButton(self.centralwidget)
        self.a5.setGeometry(QtCore.QRect(500, 130, 41, 151))
        self.a5.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.a5.setText("")
        self.a5.setObjectName("a5")
        self.f4 = QtWidgets.QPushButton(self.centralwidget)
        self.f4.setGeometry(QtCore.QRect(420, 130, 41, 151))
        self.f4.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.f4.setText("")
        self.f4.setObjectName("f4")
        self.g3 = QtWidgets.QPushButton(self.centralwidget)
        self.g3.setGeometry(QtCore.QRect(180, 130, 41, 151))
        self.g3.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.g3.setText("")
        self.g3.setObjectName("g3")
        self.d3 = QtWidgets.QPushButton(self.centralwidget)
        self.d3.setGeometry(QtCore.QRect(60, 130, 41, 151))
        self.d3.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.d3.setText("")
        self.d3.setObjectName("d3")
        self.c5 = QtWidgets.QPushButton(self.centralwidget)
        self.c5.setGeometry(QtCore.QRect(580, 130, 41, 151))
        self.c5.setStyleSheet("border: 2px solid #8f8f91;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"")
        self.c5.setText("")
        self.c5.setObjectName("c5")
        self.save_pc = QtWidgets.QPushButton(self.centralwidget)
        self.save_pc.setGeometry(QtCore.QRect(30, 20, 101, 71))
        self.save_pc.setObjectName("save_pc")
        self.save_db = QtWidgets.QPushButton(self.centralwidget)
        self.save_db.setGeometry(QtCore.QRect(10, 340, 301, 71))
        self.save_db.setObjectName("save_db")
        self.open_list = QtWidgets.QPushButton(self.centralwidget)
        self.open_list.setGeometry(QtCore.QRect(330, 340, 301, 71))
        self.open_list.setObjectName("open_list")
        self.stop.raise_()
        self.record.raise_()
        self.b5.raise_()
        self.a5.raise_()
        self.g4.raise_()
        self.f4.raise_()
        self.e4.raise_()
        self.d4.raise_()
        self.c4.raise_()
        self.b4.raise_()
        self.a4.raise_()
        self.g3.raise_()
        self.f3.raise_()
        self.e3.raise_()
        self.c3.raise_()
        self.d3.raise_()
        self.f4_2.raise_()
        self.d3_2.raise_()
        self.a4_2.raise_()
        self.d4_2.raise_()
        self.f3_2.raise_()
        self.a5_2.raise_()
        self.c4_2.raise_()
        self.listen.raise_()
        self.g4_2.raise_()
        self.g3_2.raise_()
        self.c3_2.raise_()
        self.c5.raise_()
        self.save_pc.raise_()
        self.save_db.raise_()
        self.open_list.raise_()
        self.setCentralWidget(self.centralwidget)

        self.a4.clicked.connect(lambda: self.kb_pressed('a4'))
        self.a4_2.clicked.connect(lambda: self.kb_pressed('a4_2'))
        self.a5.clicked.connect(lambda: self.kb_pressed('a5'))
        self.a5_2.clicked.connect(lambda: self.kb_pressed('a5_2'))
        self.c3.clicked.connect(lambda: self.kb_pressed('c3'))
        self.c3_2.clicked.connect(lambda: self.kb_pressed('c3_2'))
        self.c4.clicked.connect(lambda: self.kb_pressed('c4'))
        self.c4_2.clicked.connect(lambda: self.kb_pressed('c4_2'))
        self.d3.clicked.connect(lambda: self.kb_pressed('d3'))
        self.d3_2.clicked.connect(lambda: self.kb_pressed('d3_2'))
        self.d4.clicked.connect(lambda: self.kb_pressed('d4'))
        self.d4_2.clicked.connect(lambda: self.kb_pressed('d4_2'))
        self.e3.clicked.connect(lambda: self.kb_pressed('e3'))
        self.e4.clicked.connect(lambda: self.kb_pressed('e4'))
        self.f3.clicked.connect(lambda: self.kb_pressed('f3'))
        self.f3_2.clicked.connect(lambda: self.kb_pressed('f3_2'))
        self.f4.clicked.connect(lambda: self.kb_pressed('f4'))
        self.f4_2.clicked.connect(lambda: self.kb_pressed('f4_2'))
        self.g3.clicked.connect(lambda: self.kb_pressed('g3'))
        self.g3_2.clicked.connect(lambda: self.kb_pressed('g3_2'))
        self.g4.clicked.connect(lambda: self.kb_pressed('g4'))
        self.g4_2.clicked.connect(lambda: self.kb_pressed('g4_2'))
        self.b4.clicked.connect(lambda: self.kb_pressed('b4'))
        self.b5.clicked.connect(lambda: self.kb_pressed('b5'))
        self.c5.clicked.connect(lambda: self.kb_pressed('c5'))
        self.stop.hide()
        self.record.clicked.connect(self.recording)
        self.stop.clicked.connect(self.stop_recording)
        self.listen.clicked.connect(self.listen_last)
        self.save_pc.clicked.connect(self.save_wav)
        self.save_db.clicked.connect(self.save_sql)
        self.open_list.clicked.connect(self.open_db_list)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, PianoForm):
        _translate = QtCore.QCoreApplication.translate
        PianoForm.setWindowTitle(_translate("PianoForm", "MainWindow"))
        self.stop.setText(_translate("PianoForm", "Стоп"))
        self.listen.setText(_translate("PianoForm", "Прослушать"))
        self.record.setText(_translate("PianoForm", "Запись"))
        self.save_pc.setText(_translate("PianoForm", "Сохранить "))
        self.save_db.setText(_translate("PianoForm", "Сохранить в базу данных"))
        self.open_list.setText(_translate("PianoForm", "Открыть список мелодий"))

    def kb_pressed(self, btn_name):
        if len(btn_name) > 2:
            playsound.playsound(f'src/sound2/{btn_name[0]}-{btn_name[1]}.mp3')
        else:

            playsound.playsound(f'src/sound2/{btn_name}.mp3')

    def recording(self):
        self.rec_thread = threading.Thread(target=record, daemon=True)
        global is_recording
        is_recording = True
        self.rec_thread.start()
        self.stop.show()
        self.record.hide()
        self.save_db.hide()
        self.save_pc.hide()
        self.open_list.hide()
        self.listen.hide()

    def stop_recording(self):
        global is_recording
        is_recording = False
        self.rec_thread.join()
        self.stop.hide()
        self.record.show()
        self.listen.show()
        self.save_db.show()
        self.save_pc.show()
        self.open_list.show()

    def save_wav(self):
        global Dialog
        Dialog = QtWidgets.QDialog()
        ui = save.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.setWindowTitle('Save')

        def save_melody():
            name = ui.plainTextEdit.toPlainText()
            shutil.copy(r'tmp/tmp.wav', fr'melodies/{name}.wav')
            Dialog.hide()

        ui.pushButton.clicked.connect(save_melody)
        ui.pushButton_2.clicked.connect(lambda: Dialog.hide())

    def save_sql(self):
        global Dialog
        Dialog = QtWidgets.QDialog()
        ui = save.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.setWindowTitle('Save')

        def save_db():
            name = ui.plainTextEdit.toPlainText()

            with open('tmp/tmp.wav', 'rb') as op:
                data = op.read()
            conn = sqlite3.connect('db/sqlite.db')
            cur = conn.cursor()
            cur.execute(f'INSERT INTO melodies(melody_name, melody_data) VALUES(?,?)', (name, data))
            conn.commit()
            Dialog.hide()
            conn.close()

        ui.pushButton.clicked.connect(save_db)
        ui.pushButton_2.clicked.connect(lambda: Dialog.hide())

    def listen_last(self):
        self.record.hide()
        self.listen.hide()
        self.save_db.hide()
        self.save_pc.hide()
        self.open_list.hide()
        playsound.playsound('tmp/tmp.wav')
        self.record.show()
        self.listen.show()
        self.save_db.show()
        self.save_pc.show()
        self.open_list.show()

    def open_db_list(self):
        global MyWidget
        MyWidget = db.MyWidget()
        MyWidget.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.kb_pressed('c3')
        if event.key() == QtCore.Qt.Key_W:
            self.kb_pressed('d3')
        if event.key() == QtCore.Qt.Key_E:
            self.kb_pressed('e3')
        if event.key() == QtCore.Qt.Key_R:
            self.kb_pressed('f3')
        if event.key() == QtCore.Qt.Key_T:
            self.kb_pressed('g3')
        if event.key() == QtCore.Qt.Key_Y:
            self.kb_pressed('a4')
        if event.key() == QtCore.Qt.Key_U:
            self.kb_pressed('b4')
        if event.key() == QtCore.Qt.Key_I:
            self.kb_pressed('c4')
        if event.key() == QtCore.Qt.Key_O:
            self.kb_pressed('d4')
        if event.key() == QtCore.Qt.Key_P:
            self.kb_pressed('e4')
        if event.key() == QtCore.Qt.Key_Z:
            self.kb_pressed('f4')
        if event.key() == QtCore.Qt.Key_X:
            self.kb_pressed('g4')
        if event.key() == QtCore.Qt.Key_C:
            self.kb_pressed('a5')
        if event.key() == QtCore.Qt.Key_V:
            self.kb_pressed('b5')
        if event.key() == QtCore.Qt.Key_B:
            self.kb_pressed('c5')
        if event.key() == QtCore.Qt.Key_1:
            self.kb_pressed('c3_2')
        if event.key() == QtCore.Qt.Key_2:
            self.kb_pressed('d3_2')
        if event.key() == QtCore.Qt.Key_3:
            self.kb_pressed('f3_2')
        if event.key() == QtCore.Qt.Key_4:
            self.kb_pressed('g3_2')
        if event.key() == QtCore.Qt.Key_5:
            self.kb_pressed('a4_2')
        if event.key() == QtCore.Qt.Key_6:
            self.kb_pressed('c4_2')
        if event.key() == QtCore.Qt.Key_7:
            self.kb_pressed('d4_2')
        if event.key() == QtCore.Qt.Key_8:
            self.kb_pressed('f4_2')
        if event.key() == QtCore.Qt.Key_9:
            self.kb_pressed('g4_2')
        if event.key() == QtCore.Qt.Key_0:
            self.kb_pressed('a5_2')
        event.accept()




if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_PianoForm()
    ui.setupUi()
    ui.show()
    ui.setWindowTitle('Super piano!!')
    ui.c3.setText('Q')
    ui.d3.setText('W')
    ui.e3.setText('E')
    ui.f3.setText('R')
    ui.g3.setText('T')
    ui.a4.setText('Y')
    ui.b4.setText('U')
    ui.c4.setText('I')
    ui.d4.setText('O')
    ui.e4.setText('P')
    ui.f4.setText('Z')
    ui.g4.setText('X')
    ui.a5.setText('C')
    ui.b5.setText('V')
    ui.c5.setText('B')
    sys.exit(app.exec_())

