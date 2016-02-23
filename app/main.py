#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# copyright (c) 2016 luffae@gmail.com
#

from flask import Flask, Response, request, render_template
from nscaconfig import NSCAConfig
import simplejson as json
import websiteconfig

app = Flask(__name__)

app.config.from_object(websiteconfig.ProductionConfig)


@app.before_first_request
def load_current_config():
  global nscacfg
  nscacfg = NSCAConfig(app.config['CONF'])


@app.route('/', methods=["GET"])
def index():
  return render_template("index.html")


@app.route("/apply", methods=["GET"])
def apply(): pass


# NOTE
# GET and DELETE method can only pass data through
# request query string args while
# PUT and POST using form/data to do the job

@app.route("/config", methods=['GET', 'POST', 'PUT', 'DELETE'])
def config_curd():
  if request.method == 'GET':
    req = json.loads(request.args['data'])
    ret = nscacfg.get(req)
    code = 200

  if request.method == 'POST':
    req = json.loads(request.form['data'])
    ret = nscacfg.add(req)
    code = 200 if ret else 404

  if request.method == 'PUT':
    req = json.loads(request.form['data'])
    ret = nscacfg.update(req)
    code = 200 if ret else 404

  if request.method == 'DELETE':
    req = json.loads(request.args['data'])
    ret = nscacfg.delete(req)
    code = 200 if ret else 404

  return Response(
           response=json.dumps(ret),
           status=code,
           mimetype="application/json"
         )


if __name__ == "__main__":
  app.run(
    host=app.config['ADDR'],
    port=app.config['PORT'],
    threaded=True
  )

