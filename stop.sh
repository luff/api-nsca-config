#!/usr/bin/env bash
#
# copyright (c) 2016 luffae@gmail.com
#

wd=$(cd $(dirname $0) && pwd)

pkill -f $wd/app/main.py

