class Config(object):
  DEBUG = False
  TESTING = False

class ProductionConfig(Config):
  ADDR = "10.0.0.109"
  PORT = 8001
  CONF = "/hy/scripts/nsca_web_config/nsca.conf"

class DevelopmentConfig(Config):
  DEBUG = True
  ADDR = "192.168.10.101"
  PORT = 8001
  CONF = "D:/WIP/nsca_web_config/nsca.conf"

class TestingConfig(Config):
  TESTING = True
  ADDR = "192.168.2.238"
  PORT = 8001
  CONF = "/root/nsca_web_config/nsca.conf"

