import os
from utils.yamlutil import YamlReader

current = os.path.abspath(__file__)     # 获取当前路径
base_dir = os.path.dirname(os.path.dirname(current))     # 获取上一级路径
# 定义config路径
_config_path = base_dir + os.sep + "config"

# 定义yml路径
_config_file = _config_path + os.sep + "conf.yml"

# 定义logs文件路径
_log_path = base_dir + os.sep + "logs"

# db_conf.yml路径
_bd_config_file = _config_path + os.sep + "db_conf.yml"

# excel_path
_excel_path = base_dir + os.sep + "data"
# print(_excel_path)
# excel_file
_excel_file = _excel_path + os.sep + "app.pyhongxing_case.xlsx"
# print(_excel_file)

# 报告地址
_report_path = base_dir + os.sep + "report"

def get_config_path():
    return _config_file

def get_log_path():
    return _log_path

def get_db_config_file():
    return _bd_config_file

def get_excel_file():
    return _excel_file

def get_report_path():
    return _report_path

class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_path()).data()
        self.bd_config = YamlReader(get_db_config_file()).data()
    def get_conf_url(self):
        url = self.config["base"]["test"]["url"]
        return url

    def get_accountinfo(self, index):
        value = self.config["accountsinfo"][index]
        return value

    def get_conf_log(self):
        return self.config["base"]["log_level"]

    def get_conf_log_extension(self):
        return self.config["base"]["log_extension"]

    def get_db_conf_info(self, db_alias):
        """
        获取数据库相关信息
        :param db_alias:
        :return:
        """
        return self.bd_config[db_alias]
    def get_case_sheet(self):
        return self.config["base"]["test"]["case_sheet"]



if __name__ == "__main__":
    user = ConfigYaml()
    print(user.get_case_sheet())
    print(user.get_conf_url())
#     print(user.get_accountinfo("pmaccount"))
#     print(user.get_conf_log())
#     print(user.get_conf_log_extension())
#     print(user.get_db_conf_info("db_1"))
