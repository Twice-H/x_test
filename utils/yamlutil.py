import os
import yaml
# from config.Conf import *
import datetime
class YamlReader:
    # 初始化判断有没有yaml文件
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None

    def data(self):
        if not self._data:
            with open(self.yamlf, "r", encoding="utf-8")as f:
                self._data = yaml.safe_load(f)
        return self._data

    def data_all(self):
        if not self._data_all:
            with open(self.yamlf, "r", encoding="utf-8")as f:
                self._data_all = yaml.safe_load(f)
        return self._data_all
