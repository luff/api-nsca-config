#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# copyright (c) 2016 luffae@gmail.com
#

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.dont_write_bytecode = True


from flask import Flask, Response, request
from collections import OrderedDict
from myconf import yaml_get, yaml_update

import simplejson as json

app = Flask(__name__)

app.config.from_object('main')
app.config.from_envvar('FLASK_CONFIG')


@app.route("/config", methods=["GET"])
def config_get():
  data = yaml_get(app.config['CFG'])

  if data:
    resp = json.dumps(data)
    code = 200
  else:
    resp = json.dumps({ 'status': 'err' })
    code = 400

  return Response(response=resp, status=code, mimetype="application/json")


@app.route("/config", methods=["POST"])
def config_post():
  data = json.loads(request.data, object_pairs_hook=OrderedDict)

  if data:
    yaml_update(data, app.config['TMP'])
    resp = json.dumps({ 'status': 'ok' })
    code = 200
  else:
    resp = json.dumps({ 'status': 'err' })
    code = 400

  return Response(response=resp, status=code, mimetype="application/json")


if __name__ == "__main__":
  app.run(
    host=app.config['ADDR'],
    port=app.config['PORT'],
    threaded=True
  )

