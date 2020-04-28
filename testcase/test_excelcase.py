from utils.requestutil import Request
from common.excelconfig import DataConfig
from common.exceldata import Data
from config.Conf import *
import pytest
import json
from utils.logutil import my_log
from time import sleep
request = Request()
#1. 初始化信息
#1）. 初始化测试用例文件
excel_name = get_excel_file()
# print(excel_name)
#2）. 测试用例sheet名称
sheet_name = ConfigYaml().get_case_sheet()
# print(sheet_name)
#3）. 获取运行测试用例列表
data_init = Data(excel_name, sheet_name)
run_list = data_init.get_run_data()

# print(run_list)
# 前置条件

data_key = DataConfig()
# 4）. 日志
log = my_log()
# 初始化dataconfig
#2. 测试用例方法。参数化运行
#一个用例的执行

class TestExcel:
    #1. 增加Pyest
    #2. 修改方法参数
    #3. 重构函数内容
    #4. pytest.main

    @pytest.mark.parametrize("case", run_list)
    def test_run(self, case):
        global param, res
        # data_key = DataConfig()
        method = case[data_key.method]
        params = case[data_key.params]
        # headers = case[data_key.headers]
        pre_exec = case[data_key.pre_exec]
        # print(params)
        # print(headers)
        # 1. 判断headers是否存在，json转义，
        # if headers:
        #     header = json.loads(headers)
        # else:
        #     header = None
        # 1. 验证前置条件
        # if pre_exec:
        #     pre_case = data_init.get_case_pre(pre_exec)
        #     print("*" * 20, pre_case)
        #     print("前置条件 %s" % pre_case)
            # r = self.run_pre(pre_case)
            # print(r)
        sleep(0.2)
        if len(str(params).strip()) is not 0:
            param = json.loads(params)
        if str(method).lower() == "get":
            res = request.get(data=param)
        if str(method).lower() == "post":
            res = request.post(data=param)
            sleep(0.2)
        else:
            log.error("错误请求method: %s" % method)
        print(res)
        # token = res["data"]["token"]
        # uid = res["data"]["uid"]
        # sessionkey = res["data"]["session_key"]
        # print(token, uid, sessionkey)
        # if pre_exec:
        #     pass
        #     param["token"] = token
        #     param["uid"] = uid
        #     param["sessionkey"] = sessionkey
        #     print(param)
        #     r = request.post(data=param)
        #     print(r)




if __name__ == "__main__":
    pytest.main(["-s", "test_excelcace.py"])

    #1. 判断headers是否存在，json转义，
    #2. 增加headers
    #3. 增加cookies
    #4. 发送请求

    # 动态关联
    #1. 验证前置条件
    #2. 找到测试用例
    #3. 发送亲求
    # 发送获取前置条件用例，用例结果
    # 数据初始化，get/post，重构
    #4. 替换headers变量
        #1. 验证请求中是否又${}$,返回${}$的内容
    # import re
    # str1 = '{"Authorization": "JWT ${token}$","Authorization": "JWT ${uid}$","Authorization": "JWT ${session_key}$"}'
    # if "${" in str1:
    #     print(str1)

    #5. 请求发送