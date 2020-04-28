from utils.mysqlutil import Mysql
from config.Conf import ConfigYaml
from utils.logutil import my_log
from utils.assertutil import AssertUtil
import json
import re
import subprocess
p_data = '\${.*?}\$'
log = my_log()

#1, 定义init_db
#2,初始化信息，通过配置
#3，初始化mysql对象
def init_db(db_alias):
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    passwrod = db_info["db_passwrod"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])
    conn = Mysql(host, user, passwrod, db_name, charset, port)
    print(conn)
    return conn

def assert_db(db_name, result, db_verify):
    assert_util = AssertUtil()
    sql = init_db(db_name)
    db_res = sql.fetchone(db_verify)
    # log.debug("数据库查询结果：{}".format(str(db_res)))
    # 3、数据库的结果与接口返回的结果验证
    # 获取数据库结果的key
    verify_list = list(dict(db_res).keys())
    # 根据key获取数据库结果，接口结果
    for line in verify_list:
        res_line = result[line]
        res_db_line = dict(db_res)[line]
        assert_util.assert_body(res_line, res_db_line)

def json_parse(data):
    return json.loads(data) if data else data

def res_find(data, pattern_data=p_data):
    """查询"""
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res

def res_sub(data, replace, pattern_data=p_data):
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
        return re.sub(pattern_data, replace, data)
    return re_res

def params_find(headers, cookies):
    """验证请求中是否有${}$需要结果关联"""
    if "${" in headers:
        headers = res_find(headers)
    if "${" in cookies:
        cookies = res_find(cookies)
    return headers, cookies

def allure_report(report_path, report_html):
    allure_cmd = "allure generate %s -o %s --clean" % (report_path, report_html)
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        log.error("执行用例失败，请检查配置环境")
        raise
