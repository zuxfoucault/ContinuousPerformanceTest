# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
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

class Ui_ExperimentInfo(object):
    def setupUi(self, ExperimentInfo):
        ExperimentInfo.setObjectName(_fromUtf8("ExperimentInfo"))
        ExperimentInfo.resize(400, 309)
        self.buttonBox = QtGui.QDialogButtonBox(ExperimentInfo)
        self.buttonBox.setGeometry(QtCore.QRect(30, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(ExperimentInfo)
        self.formLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 267))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pid_label = QtGui.QLabel(self.formLayoutWidget)
        self.pid_label.setObjectName(_fromUtf8("pid_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pid_label)
        self.pid = QtGui.QLineEdit(self.formLayoutWidget)
        self.pid.setObjectName(_fromUtf8("pid"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pid)
        self.sex_label = QtGui.QLabel(self.formLayoutWidget)
        self.sex_label.setObjectName(_fromUtf8("sex_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.sex_label)
        self.sex = QtGui.QLineEdit(self.formLayoutWidget)
        self.sex.setObjectName(_fromUtf8("sex"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.sex)
        self.age_label = QtGui.QLabel(self.formLayoutWidget)
        self.age_label.setObjectName(_fromUtf8("age_label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.age_label)
        self.age = QtGui.QLineEdit(self.formLayoutWidget)
        self.age.setObjectName(_fromUtf8("age"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.age)
        self.hand_label = QtGui.QLabel(self.formLayoutWidget)
        self.hand_label.setObjectName(_fromUtf8("hand_label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.hand_label)
        self.hand = QtGui.QLineEdit(self.formLayoutWidget)
        self.hand.setObjectName(_fromUtf8("hand"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.hand)
        self.actl_label = QtGui.QLabel(self.formLayoutWidget)
        self.actl_label.setTextFormat(QtCore.Qt.PlainText)
        self.actl_label.setScaledContents(False)
        self.actl_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.actl_label.setObjectName(_fromUtf8("actl_label"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.actl_label)
        self.actl = QtGui.QLineEdit(self.formLayoutWidget)
        self.actl.setObjectName(_fromUtf8("actl"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.actl)
        self.runs_label = QtGui.QLabel(self.formLayoutWidget)
        self.runs_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.runs_label.setTextFormat(QtCore.Qt.PlainText)
        self.runs_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.runs_label.setWordWrap(True)
        self.runs_label.setObjectName(_fromUtf8("runs_label"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.runs_label)
        self.runs = QtGui.QLineEdit(self.formLayoutWidget)
        self.runs.setObjectName(_fromUtf8("runs"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.runs)
        self.sess_label = QtGui.QLabel(self.formLayoutWidget)
        self.sess_label.setObjectName(_fromUtf8("sess_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.sess_label)
        self.sess = QtGui.QLineEdit(self.formLayoutWidget)
        self.sess.setObjectName(_fromUtf8("sess"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sess)
        self.edu = QtGui.QLineEdit(self.formLayoutWidget)
        self.edu.setObjectName(_fromUtf8("edu"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.edu)
        self.edu_label = QtGui.QLabel(self.formLayoutWidget)
        self.edu_label.setObjectName(_fromUtf8("edu_label"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.edu_label)

        self.retranslateUi(ExperimentInfo)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ExperimentInfo.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ExperimentInfo.reject)
        QtCore.QMetaObject.connectSlotsByName(ExperimentInfo)

    def retranslateUi(self, ExperimentInfo):
        ExperimentInfo.setWindowTitle(_translate("ExperimentInfo", "Dialog", None))
        self.pid_label.setText(_translate("ExperimentInfo", "Participant ID", None))
        self.pid.setPlaceholderText(_translate("ExperimentInfo", "0001", None))
        self.sex_label.setText(_translate("ExperimentInfo", "Sex", None))
        self.sex.setText(_translate("ExperimentInfo", "Female", None))
        self.sex.setPlaceholderText(_translate("ExperimentInfo", "Female", None))
        self.age_label.setText(_translate("ExperimentInfo", "Age", None))
        self.age.setText(_translate("ExperimentInfo", "20", None))
        self.age.setPlaceholderText(_translate("ExperimentInfo", "20", None))
        self.hand_label.setText(_translate("ExperimentInfo", "Handedness", None))
        self.hand.setText(_translate("ExperimentInfo", "Right", None))
        self.hand.setPlaceholderText(_translate("ExperimentInfo", "Right", None))
        self.actl_label.setText(_translate("ExperimentInfo", "Activity Level\n"
"1=Low 2=Med 3=High", None))
        self.actl.setText(_translate("ExperimentInfo", "2", None))
        self.actl.setPlaceholderText(_translate("ExperimentInfo", "2", None))
        self.runs_label.setText(_translate("ExperimentInfo", "# Runs per task\n"
"(K or AK)", None))
        self.runs.setText(_translate("ExperimentInfo", "2", None))
        self.runs.setPlaceholderText(_translate("ExperimentInfo", "2", None))
        self.sess_label.setText(_translate("ExperimentInfo", "Session", None))
        self.sess.setText(_translate("ExperimentInfo", "1", None))
        self.sess.setPlaceholderText(_translate("ExperimentInfo", "1", None))
        self.edu.setText(_translate("ExperimentInfo", "14", None))
        self.edu.setPlaceholderText(_translate("ExperimentInfo", "12", None))
        self.edu_label.setText(_translate("ExperimentInfo", "# Years of Education", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ExperimentInfo = QtGui.QDialog()
    ui = Ui_ExperimentInfo()
    ui.setupUi(ExperimentInfo)
    ExperimentInfo.show()
    sys.exit(app.exec_())

