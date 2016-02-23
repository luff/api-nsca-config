#!/usr/bin/env python
# coding: utf-8
#
# copyright (c) 2016 luffae@gmail.com
#

import yaml
from collections import OrderedDict


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
  """
  usage:
  ordered_load(stream, Loader=yaml.SafeLoader)
  """
  class OrderedLoader(Loader):
    pass
  def construct_mapping(loader, node):
    loader.flatten_mapping(node)
    return object_pairs_hook(loader.construct_pairs(node))
  OrderedLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_mapping)
  return yaml.load(stream, OrderedLoader)


def ordered_dump(data, stream=None, Dumper=yaml.SafeDumper, **kwds):
  """
  usage:
  ordered_dump(data, Dumper=yaml.SafeDumper)
  """
  class OrderedDumper(Dumper):
    pass
  def _dict_representer(dumper, data):
    return dumper.represent_mapping(
      yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
      data.items())
  OrderedDumper.add_representer(OrderedDict, _dict_representer)
  return yaml.dump(data, stream, OrderedDumper, **kwds)


class NSCAConfig(object):
  def __init__(self, cfg_file):
    self.load_file(cfg_file)

  def save_file(self, cfg_file):
    with open(cfg_file, 'w') as cf:
      cf.write(
        ordered_dump(
          self.cfg,
          allow_unicode=True,
          default_flow_style=False
        )
      )

  def load_file(self, cfg_file):
    with open(cfg_file) as cf:
      self.cfg = ordered_load(cf)
      for h in self.cfg.values():
        for j in h['jobs'].values():
          j['attempts'] = 3


  def add(self, item):
    return None

  def delete(self, item):
    return None

  def get(self, fltr):
    fl = dict()
    # reconstract filter
    if 'H' in fltr and fltr['H'] != "":
      fl['H'] = fltr['H']
    if 'N' in fltr and fltr['N'] != "":
      fl['N'] = fltr['N']
    if 'A' in fltr and fltr['A'] >= 1:
      fl['A'] = fltr['A']
    if 'I' in fltr and fltr['I'] >= 1:
      fl['I'] = fltr['I']
    if 'w' in fltr and fltr['w'] >= 1:
      fl['w'] = fltr['w']
    if 'c' in fltr and fltr['c'] >= 1:
      fl['c'] = fltr['c']

    # transform cfg object into a list
    jobs = []
    for h in self.cfg.values():
      job = {}
      job['H'] = h['address']

      for j, jv in h['jobs'].iteritems():
        job['N'] = j
        job['A'] = jv['attempts']
        job['I'] = jv['params']['I']
        job['w'] = jv['params']['w']
        job['c'] = jv['params']['c']
        # fliter by fl
        if all(i in job.items() for i in fl.items()):
          jobs.append(job.copy())

    return jobs

  def update(self, item):
    # validate values
    if 'A' not in item or item['A'] < 1 or \
       'I' not in item or item['I'] < 1 or \
       'w' not in item or item['w'] < 1 or \
       'c' not in item or item['c'] < 1 or \
       'H' not in item or \
       'N' not in item:
      return None

    # find target job and set values
    for h in self.cfg.values():
      if item['H'] == h['address'] and item['N'] in h['jobs']:
        j = h['jobs'][item['N']]
        j['attempts'] = item['A']
        j['params']['I'] = item['I']
        j['params']['w'] = item['w']
        j['params']['c'] = item['c']
        return item

    return None

