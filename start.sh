#!/usr/bin/env bash
#
# copyright (c) 2016 luffae@gmail.com
#

wd=$(cd $(dirname $0) && pwd)

cfg=$wd/cfg/main.conf

py=/usr/bin/python

if [[ ! -f $cfg ]]; then
  echo "config not found: $cfg"
  exit 1
fi
mkdir -p $wd/log

export FLASK_CONFIG=$cfg
nohup $py $wd/app/main.py &> $wd/log/access.log &

