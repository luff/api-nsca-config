#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# copyright (c) 2016 luffae@gmail.com
#

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.dont_write_bytecode = True

class Unbuffered(object):
  def __init__(self, stream):
    self.stream = stream
  def write(self, data):
    self.stream.write(data)
    self.stream.flush()
  def __getattr__(self, attr):
    return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

sys.path.insert(0, sys.path[0] + '/' + 'app')

from main import app
import websiteconfig

if __name__ == "__main__":
  app.config.from_object(websiteconfig.TestingConfig)
  app.run(
    host=app.config['ADDR'],
    port=app.config['PORT'],
    threaded=True
  )

