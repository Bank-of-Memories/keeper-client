import os
import urllib
import psutil
import time
import subprocess
import ipfshttpclient
from utils import getOSName

OPTION = "daemon"

class IpfsController:
  def __init__(self, parent = None):
    self._parent = parent
    try:
      # self.client = ipfshttpclient.connect()
      self.connectIpfsGateWay()
    except:
      self.client = None
      # self._parent.showAlertMessage("Ipfs daemon is not running!\n\nStarting ipfs node...")
      self.runDaemon()


  def setStorageSize(self, size):
    next_size = str(size)
    self.client.config.set("Datastore.StorageMax", next_size + "GB")

  def getStorageSize(self):
    return self.client.config.get()["Datastore"]["StorageMax"]

  def runDaemon(self):
    if not os.path.isdir(".tmp"):
      subprocess.run(["scripts/init.sh"], shell=True)

    try:
      self.daemon_proc = subprocess.Popen([self.getIPFSExecutablePath(), OPTION], text=True)

      time.sleep(1)
      self.connectIpfsGateWay()
      # self.client = ipfshttpclient.connect()
    except:
      pass

  def connectIpfsGateWay(self):
    self.client = ipfshttpclient.connect()
    self.client.bootstrap.add("/ip4/167.86.71.92/tcp/4005/ipfs/12D3KooWHw78xTEE99hbRghAAM68jGdeHsexg3rkFQ2aT8Evijcw")

  def restartIpfs(self):
    for proc in psutil.process_iter():
      if proc.name() == "ipfs.exe":
        proc.kill()
      if proc.name() == "ipfs":
        proc.kill()

    self.daemon_proc = subprocess.Popen([self.getIPFSExecutablePath(), OPTION], text=True)

  @staticmethod
  def getIPFSAddress(url):
    addr = urllib.parse.urlsplit(url)
    return '/'.join(['/dns', addr.hostname, 'tcp', str(addr.port), addr.scheme])

  @staticmethod
  def getIPFSExecutablePath():
    return os.path.join('.tmp', 'go-ipfs', 'ipfs')

  @staticmethod
  def getIPFSOutputFilePath(file):
    if not os.path.isdir(os.path.join('.tmp')):
      os.mkdir(os.path.join('.tmp'))
    return os.path.join('.tmp', file)
