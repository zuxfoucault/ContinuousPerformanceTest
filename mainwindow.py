# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QDialog, QtGui.QMainWindow):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.exp_info = {}
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 332)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 257))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pid_label = QtGui.QLabel(self.formLayoutWidget)
        self.pid_label.setObjectName(_fromUtf8("pid_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pid_label)
        self.pid = QtGui.QLineEdit(self.formLayoutWidget)
        self.pid.setObjectName(_fromUtf8("pid"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pid)
        self.sex_label = QtGui.QLabel(self.formLayoutWidget)
        self.sex_label.setObjectName(_fromUtf8("sex_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.sex_label)
        self.sex = QtGui.QLineEdit(self.formLayoutWidget)
        self.sex.setObjectName(_fromUtf8("sex"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sex)
        self.hand_label = QtGui.QLabel(self.formLayoutWidget)
        self.hand_label.setObjectName(_fromUtf8("hand_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.hand_label)
        self.pid_label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.pid_label_4.setObjectName(_fromUtf8("pid_label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.pid_label_4)
        self.pid_label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.pid_label_5.setObjectName(_fromUtf8("pid_label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.pid_label_5)
        self.pid_label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.pid_label_6.setObjectName(_fromUtf8("pid_label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.pid_label_6)
        self.pid_label_7 = QtGui.QLabel(self.formLayoutWidget)
        self.pid_label_7.setObjectName(_fromUtf8("pid_label_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.pid_label_7)
        self.hand = QtGui.QLineEdit(self.formLayoutWidget)
        self.hand.setObjectName(_fromUtf8("hand"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.hand)
        self.sess = QtGui.QLineEdit(self.formLayoutWidget)
        self.sess.setObjectName(_fromUtf8("sess"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.sess)
        self.age = QtGui.QLineEdit(self.formLayoutWidget)
        self.age.setObjectName(_fromUtf8("age"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.age)
        self.edu = QtGui.QLineEdit(self.formLayoutWidget)
        self.edu.setObjectName(_fromUtf8("edu"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.edu)
        self.actl = QtGui.QLineEdit(self.formLayoutWidget)
        self.actl.setObjectName(_fromUtf8("actl"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.actl)
        self.pid_label_8 = QtGui.QLabel(self.formLayoutWidget)
        self.pid_label_8.setWordWrap(True)
        self.pid_label_8.setObjectName(_fromUtf8("pid_label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.pid_label_8)
        self.runs = QtGui.QLineEdit(self.formLayoutWidget)
        self.runs.setObjectName(_fromUtf8("runs"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.runs)
        self.startButton = QtGui.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(0, 250, 401, 31))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def start(self):
        self.exp_info = {u'Sex': self.sex.text(),
                         u'Handedness': self.hand.text(),
                         u'Participant': self.pid.text(),
                         u'Session': self.sess.text(),
                         u'Age': self.age.text(),
                         u'Years of completed education': self.edu.text(),
                         u'Activity Level': self.actl.text(),
                         u'# of runs per experiment': self.runs.text()}
        self.accept()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pid_label.setText(_translate("MainWindow", "Participant ID", None))
        self.pid.setText(_translate("MainWindow", "0001", None))
        self.sex_label.setText(_translate("MainWindow", "Sex", None))
        self.sex.setText(_translate("MainWindow", "femaile", None))
        self.hand_label.setText(_translate("MainWindow", "Handedness", None))
        self.pid_label_4.setText(_translate("MainWindow", "Session #", None))
        self.pid_label_5.setText(_translate("MainWindow", "Age", None))
        self.pid_label_6.setText(_translate("MainWindow", "Years of education", None))
        self.pid_label_7.setText(_translate("MainWindow", "Activity Level", None))
        self.hand.setText(_translate("MainWindow", "right", None))
        self.sess.setText(_translate("MainWindow", "1", None))
        self.age.setText(_translate("MainWindow", "20", None))
        self.edu.setText(_translate("MainWindow", "12", None))
        self.actl.setText(_translate("MainWindow", "2", None))
        self.pid_label_8.setText(_translate("MainWindow", "# of Runs", None))
        self.runs.setText(_translate("MainWindow", "2", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
