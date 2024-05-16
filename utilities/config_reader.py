from configparser import ConfigParser


def read_config(section, key):
    config = ConfigParser()
    config.read("..//configuration_data/conf.ini")
    return config.get(section, key)
