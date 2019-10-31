# -*- coding: utf-8 -*-

import os
import json

worldpath = './server/world'
savepath = './savelib'

class mcsave(object):
  def __init__(self, savepath, meta = {}):
    self.path = savepath
    with open(self.path + './meta.json', 'w') as handler:
      handler.write(json.dumps(meta))
  
  def backup(self, meta = {}, writeTime = True):
    if writeTime:
      time = time.strftime('%Y-%m-%d',time.localtime()) + ' ' + time.strftime('%H:%M:%S',time.localtime())
      meta['time'] = time
    targetpath = savepath + '/' + time
    os.system('mkdir ' + targetpath)
    os.system('cp ' + worldpath + ' ' + targetpath)

  def readMeta(self):
    with open(self.path + './meta.json', 'r') as handler:
      return json.loads(handler.read())
  
  def writeMeta(self, meta):
    with open(self.path + './meta.json', 'w') as handler:
      handler.write(json.dumps(meta))