import json
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
from core.Component import Component
from constants import OTP_CHECK_URL

class RoundEdit(QLineEdit):
  def __init__(self, parent = None):
    super(RoundEdit, self).__init__(parent)
    self.setObjectName("code-otp-item")
    self.setAttribute(Qt.WA_MacShowFocusRect, 0)
    self.validator = QIntValidator()

    self.neighbor = None

    self.textChanged.connect(self.goToNext)

    self.setValidator(self.validator)

  def setNeighbor(self, n):
    self.neighbor = n

  def goToNext(self):
    if self.neighbor and len(self.text()) > 0:
      self.neighbor.setFocusPolicy(Qt.TabFocus)
      self.neighbor.setFocus()
    else:
      return False

class OtpComponent(Component):
  def __init__(self, parent = None):
    super(OtpComponent, self).__init__(parent)

    self.pageLayout = QVBoxLayout()
    self.pageLayout.setSpacing(0)
    self.pageLayout.setContentsMargins(0, 0, 0, 0)
    self.pageLayout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

    self.formLayout = QHBoxLayout()


    self.intValidator = QIntValidator()

    self.title = QLabel("Enter a confirmation code we sent\nto your email address")
    self.title.setAlignment(Qt.AlignHCenter)

    self.num1 = RoundEdit()
    self.num2 = RoundEdit()
    self.num3 = RoundEdit()
    self.num4 = RoundEdit()

    self.num1.setNeighbor(self.num2)
    self.num2.setNeighbor(self.num3)
    self.num3.setNeighbor(self.num4)

    self.submitButton = QPushButton("Submit")
    self.submitButton.setMaximumWidth(100)
    self.submitButton.clicked.connect(self.tryCheck)

    self.pageLayout.addWidget(self.title)
    self.formLayout.addWidget(self.num1)
    self.formLayout.addWidget(self.num2)
    self.formLayout.addWidget(self.num3)
    self.formLayout.addWidget(self.num4)
    self.pageLayout.addWidget(self.submitButton)

    self.pageLayout.insertLayout(1, self.formLayout)
    self.setLayout(self.pageLayout)

  def resetFirst(self):
    if len(self.num1.text()) > 0:
      self.num2.setFocusPolicy(Qt.TabFocus)
      self.num2.setFocus()

  def resetSecond(self):
    if len(self.num2.text()) > 0:
      self.num3.setFocusPolicy(Qt.TabFocus)
      self.num3.setFocus()

  def resedThird(self):
    if len(self.num3.text()) > 0:
      self.num4.setFocusPolicy(Qt.TabFocus)
      self.num4.setFocus()

  def resetFourth(self):
    if len(self.num4.text()) > 0:
      return False


  def tryCheck(self):
    userInput = self.num1.text() + self.num2.text() + self.num3.text() + self.num4.text()
    print(userInput)
    data = {
      "token": self._parent.store.token,
      "code": userInput
    }

    out = requests.post(OTP_CHECK_URL, json=data).json()

    if out["result"] == True:
      self._parent.store.accessToken = out["data"]["access_token"]
      self._parent.store.refreshToken = out["data"]["refresh_token"]
      self._parent.store.userProfile = out["data"]["user"]


      if self._parent.store.keepSignIn:
        with open(".profile", "w+") as f:
          f.write(json.dumps(out["data"]))

      self._parent.updateCentralWidgetIndex(1)
      self._parent.switchPage()
    else:
      self._parent.showAlertMessage(out["error"]["msg"])