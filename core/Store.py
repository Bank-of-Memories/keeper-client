class Store:
  def __init__(self):
    self.token = None
    self.accessToken = None
    self.refreshToken = None
    self.userProfile = None

    self.firstRun = True
    self.keepSignIn = False

    self.connectPopupOpen = False