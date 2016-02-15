#!/usr/bin/env python
# coding: utf-8
#
# copyright (c) 2016 luffae@gmail.com
#

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.dont_write_bytecode = True


from myyaml import ordered_load, ordered_dump

def yaml_to_nagios_cfg(cfg_file):
  service_definition = 'generic-passive-service'

  buffer = ''

  with open(cfg_file) as cf:
    config = ordered_load(cf)

  for h, hv in config.iteritems():
    buffer += (
      "\n"
      "{0:/<64}\n".format('# ') +
      "# Configuration for " + h + "\n"
      "{0:/<64}\n".format('# ') + "\n"
    )

    buffer += (
      "define host {\n" +
      "    %-24s%s\n" % ('use', hv['template']) +
      "    %-24s%s\n" % ('host_name', hv['alias']) +
      "    %-24s%s\n" % ('alias', h) +
      "    %-24s%s\n" % ('address', hv['address']) +
      "}\n\n"
    )

    for j, jv in hv['jobs'].iteritems():
      fresh_second = jv['params']['I'] * 60 + 300
      buffer += (
        "define service {\n"
        "    %-24s%s\n" % ('use', service_definition) +
        "    %-24s%s\n" % ('host_name', hv['alias']) +
        "    %-24s%s\n" % ('service_description', j) +
        "    %-24s%d\n" % ('freshness_threshold', fresh_second) +
        "}\n\n"
      )

  return buffer


def yaml_update(cfg, cfg_file):
  with open(cfg_file, 'w') as cf:
    cf.write(
      ordered_dump(
        cfg,
        allow_unicode=True,
        default_flow_style=False
      )
    )


def yaml_get(cfg_file):
  with open(cfg_file) as cf:
    config = ordered_load(cf)

  return config

