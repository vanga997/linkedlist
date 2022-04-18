import sys
from unittest import TestCase

from PyQt5 import QtCore
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from GUI import MainWindow, PushFront, PushAfter, PushEnd, PushBefore, PushFirst, DeleteValue
from facade import Facade


class FunctionalTest(TestCase):
    def setUp(self):
        self.qapp = QApplication(sys.argv)
        name = 'test.db'
        self.facade = Facade(name)
        self.window = MainWindow(self.facade)

    def test1_push_first(self):
        btn_push_first = self.window.ui.btn_push_first
        QTest.mouseClick(btn_push_first, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushFirst):
                dialog = window
                break
        else:
            self.fail()

        dialog.lineEdit.setText("1")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test2_push_end(self):
        btn_push_end = self.window.ui.btn_push_end
        QTest.mouseClick(btn_push_end, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushEnd):
                dialog = window
                break
        else:
            self.fail()

        self.facade.push_first(1)

        dialog.lineEdit.setText("4")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("5")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("6")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test3_push_front(self):
        btn_push_front = self.window.ui.btn_push_front
        QTest.mouseClick(btn_push_front, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushFront):
                dialog = window
                break

        else:
            self.fail()

        self.facade.push_first(1)

        dialog.lineEdit.setText("10")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("20")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("40")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test4_insert_before(self):
        btn_push_before = self.window.ui.btn_push_before
        QTest.mouseClick(btn_push_before, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushBefore):
                dialog = window
                break

        else:
            self.fail()

        self.facade.push_first(1)
        self.facade.push_end(5)
        self.facade.push_end(9)

        dialog.lineEdit.setText("5")
        dialog.lineEdit_2.setText("8")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("9")
        dialog.lineEdit_2.setText("20")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test5_insert_after(self):
        btn_push_after = self.window.ui.btn_push_after
        QTest.mouseClick(btn_push_after, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, PushAfter):
                dialog = window
                break

        else:
            self.fail()

        self.facade.push_first(1)
        self.facade.push_end(5)
        self.facade.push_end(9)

        dialog.lineEdit.setText("5")
        dialog.lineEdit_2.setText("10")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

        dialog.lineEdit.setText("9")
        dialog.lineEdit_2.setText("50")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test6_del_first(self):
        self.facade.push_first(4)
        self.facade.push_end(8)

        btn_del_first = self.window.ui.btn_del_first
        QTest.mouseClick(btn_del_first, QtCore.Qt.MouseButton.LeftButton)

    def test7_del_end(self):
        self.facade.push_first(10)
        self.facade.push_end(15)
        self.facade.push_end(20)

        btn_del_end = self.window.ui.btn_del_end
        QTest.mouseClick(btn_del_end, QtCore.Qt.MouseButton.LeftButton)

    def test8_del_by_value(self):
        self.facade.push_first(10)
        self.facade.push_end(20)
        self.facade.push_front(30)

        btn_del_value = self.window.ui.btn_del_value
        QTest.mouseClick(btn_del_value, QtCore.Qt.MouseButton.LeftButton)

        for window in self.qapp.topLevelWidgets():
            if isinstance(window, DeleteValue):
                dialog = window
                break

        else:
            self.fail()

        dialog.lineEdit.setText("10")
        QTest.mouseClick(dialog.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test9_reverse(self):
        self.facade.push_first(10)
        self.facade.push_end(15)
        self.facade.push_end(20)
        self.facade.insert_before(15, 13)

        btn_reverse = self.window.ui.btn_reverse
        QTest.mouseClick(btn_reverse, QtCore.Qt.MouseButton.LeftButton)
