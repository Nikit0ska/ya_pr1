import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import playsound

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("form/db.ui", self)
        self.con = sqlite3.connect("db/sqlite.db")
        self.pushButton.clicked.connect(self.update_result)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton_2.clicked.connect(self.save_results)
        self.pushButton_4.clicked.connect(self.download)
        self.pushButton_5.clicked.connect(self.delete_elem)
        self.pushButton_3.clicked.connect(self.listen_melody)
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.modified = {}
        self.titles = None
        self.setWindowTitle("Melodies")

    def update_result(self):
        cur = self.con.cursor()
        if self.spinBox.text() == '-1':
            result = cur.execute("SELECT id, melody_name FROM melodies").fetchall()
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            self.pushButton_4.hide()
            self.pushButton_5.hide()
            self.pushButton_5.show()
            self.pushButton_4.show()
        else:
            result = cur.execute("SELECT id, melody_name FROM melodies WHERE id=?",
                                 (item_id := self.spinBox.text(),)).fetchall()
            if result:
                self.pushButton_2.show()
                self.pushButton_3.show()
                self.pushButton_4.show()
                self.pushButton_5.show()
                self.pushButton_5.show()
                self.pushButton_4.show()
        self.tableWidget.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}


    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE melodies SET\n"
            for key in self.modified.keys():
                que += "{}='{}'\n".format(key, self.modified.get(key))
            que += "WHERE id = ?"
            cur.execute(que, (self.spinBox.text(),))
            self.con.commit()
            self.modified.clear()

    def download(self):
        conn = sqlite3.connect('db/sqlite.db')
        cur = conn.cursor()
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        for elem in ids:
            data = list(cur.execute(f'SELECT melody_name, melody_data FROM melodies WHERE id={elem}'))
            with open(f'melodies/{data[0][0]}.wav', 'wb') as op:
                op.write(data[0][1])

    def delete_elem(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        cur = self.con.cursor()
        cur.execute("DELETE FROM melodies WHERE id IN (" + ", ".join(
            '?' * len(ids)) + ")", ids)
        self.con.commit()
        self.update_result()

    def listen_melody(self):
        if self.spinBox.text() != '-1':
            cur = self.con.cursor()
            que = "SELECT melody_data FROM melodies WHERE id = ?"
            song = list(cur.execute(que, (self.spinBox.text(),)))[0][0]
            with open(f'tmp/tmpBD.wav', 'wb') as op:
                op.write(song)
            playsound.playsound('tmp/tmpBD.wav')

