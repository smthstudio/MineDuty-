# -*- coding: utf-8 -*-

import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MineDuty向导")
        MainWindow.resize(768, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Minecrafter Alt")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 255, 0);\n"
                                 "font: 40pt \"Minecrafter Alt\";")
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 61, 61))
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 0, 131, 81))
        self.label_2.setStyleSheet("font: 9pt \"SimSun-ExtB\";\n"
                                    "color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 60, 101, 41))
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);\n"
                                    "font: 25 15pt \"Microsoft YaHei UI Light\";")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 100, 350, 21))  # 扩大宽度以适应文本
        self.label_5.setStyleSheet("font: 25 15pt \"等线 Light\"; color: rgb(0, 0, 255); text-decoration: underline; cursor: pointer;")
        self.label_5.setObjectName("label_5")
        self.label_5.mousePressEvent = self.open_java_url  # 绑定点击事件

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 130, 350, 21))  # 扩大宽度以适应文本
        self.label_6.setStyleSheet("font: 25 15pt \"等线 Light\"; color: rgb(0, 0, 255); text-decoration: underline; cursor: pointer;")
        self.label_6.setObjectName("label_6")
        self.label_6.mousePressEvent = self.open_hmcl_url  # 绑定点击事件

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 160, 391, 21))  
        self.label_7.setStyleSheet("font: 25 15pt \"等线 Light\"; color: rgb(0, 0, 255); text-decoration: underline; cursor: pointer;")
        self.label_7.setObjectName("label_7")
        self.label_7.mousePressEvent = self.open_pcl_launcher_url  # 绑定点击事件

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 190, 391, 21))  
        self.label_8.setStyleSheet("font: 25 15pt \"等线 Light\"; color: rgb(0, 0, 255); text-decoration: underline; cursor: pointer;")
        self.label_8.setObjectName("label_8")
        self.label_8.mousePressEvent = self.open_integrated_package_url  # 绑定点击事件

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(160, 190, 191, 21))
        self.plainTextEdit.setStyleSheet("color: rgb(255, 0, 0);")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 230, 101, 31))
        self.label_9.setStyleSheet("color: rgb(255, 0, 0);\n"
                                    "font: 25 15pt \"Microsoft YaHei UI Light\";")
        self.label_9.setObjectName("label_9")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 220, 431, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(0, 260, 241, 31))
        self.label_10.setStyleSheet("font: 15pt \"Malgun Gothic\";")
        self.label_10.setObjectName("label_10")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 290, 401, 61))
        self.textBrowser.setObjectName("textBrowser")

        self.sever_ip = QtWidgets.QPushButton(self.centralwidget)
        self.sever_ip.setGeometry(QtCore.QRect(170, 70, 181, 41))
        self.sever_ip.setStyleSheet("font: 10pt \"Bahnschrift\";\n"
                                     "color: rgb(255, 0, 0);")
        self.sever_ip.setObjectName("sever_ip")

        self.blbl = QtWidgets.QPushButton(self.centralwidget)
        self.blbl.setGeometry(QtCore.QRect(350, 70, 101, 41))
        self.blbl.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
                                "")
        self.blbl.setObjectName("blbl")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(460, 70, 301, 281))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(560, 10, 101, 51))
        self.label_11.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold\";")
        self.label_11.setObjectName("label_11")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to their functions
        self.blbl.clicked.connect(self.open_url)
        self.sever_ip.clicked.connect(self.copy_ip)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MineDuty"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/dw/屏幕截图 2024-08-01 111655.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">安装向导</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">必装项目：</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", ">>>Java17"))
        self.label_6.setText(_translate("MainWindow", ">>>HMCL启动器（推荐）提取码：5267"))
        self.label_7.setText(_translate("MainWindow", ">>>PCL启动器"))
        self.label_8.setText(_translate("MainWindow", ">>>整合包本体"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "拖入启动器内安装即可！！！"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff55ff;\">联机软件：</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", ">>>Radmin VPN"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">和群友联机必备</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">网络名称：MineDuty1.0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">密码：114514</p></body></html>"))
        self.sever_ip.setText(_translate("MainWindow", "点击复制服务器IP地址"))
        self.blbl.setText(_translate("MainWindow", "调戏腐竹"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline; color:#ff0000;\">1.移除了所有版本的</span><span style=\" font-family:\'Microsoft YaHei\',\'Arial\',\'Helvetica\',\'sans-serif\'; font-weight:600; color:#111111; background-color:#ffffff;\">Herobrine</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">2.新增了亿点bug</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">3.交互bug任然未解决</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">公告栏</span></p></body></html>"))

    def open_java_url(self, event):
        webbrowser.open("https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe")

    def open_hmcl_url(self, event):
        webbrowser.open("https://url94.ctfile.com/d/33326794-44675752-fc62fc")

    def open_pcl_launcher_url(self, event):
        webbrowser.open("https://pan.aoe.top/Tools/PCL2")

    def open_integrated_package_url(self, event):
        webbrowser.open("https://wwlf.lanzouw.com/iSUIs2agyn4f")  # 这里可以换成整合包的链接

    def open_url(self):
        webbrowser.open("https://space.bilibili.com/1702603769?spm_id_from=333.1007.0.0")  # 替换为你想要的 URL

    def copy_ip(self):
        ip_address = "cn-he-plc-2.ofalias.net:57091"  # 替换为实际的 IP 地址
        QtWidgets.QApplication.clipboard().setText(ip_address)
        QtWidgets.QMessageBox.information(None, "Info", "IP 地址已复制到剪贴板！")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())