# 来源http://www.51testing.com/html/04/n-4480904.html

import os, sys, time
from PyQt5 import QtCore, QtWidgets, QtGui

def pageShow(self, page):
    """设置窗口位置和大小,标题，图标字体等"""
    page.setGeometry(400, 400, 400, 200)
    page.setWindowTitle('Windows自动关机小工具')
    # page.setWindowIcon(QtGui.QIcon('#ddffgg'))
    QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
    page.setToolTip('这是windows关机工具')
    # 创建文本标签
    self.label = QtWidgets.QLabel(page)
    self.label.setGeometry(QtCore.QRect(60, 20, 120, 45))
    self.label.setFont(QtGui.QFont("Roman times", 10, QtGui.QFont.Bold))
    # 设置文本标签和时间栏框
    self.label2 = QtWidgets.QLabel(page)
    self.label2.setGeometry(QtCore.QRect(100, 55, 40, 51))
    self.label2.setFont(QtGui.QFont("Roman times", 10, QtGui.QFont.Bold))
    self.time = QtWidgets.QDateTimeEdit(page)
    self.time.setGeometry(QtCore.QRect(140, 70, 180, 25))
    self.time.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
    # 设置日期可使用日历插件
    self.time.setCalendarPopup(True)
