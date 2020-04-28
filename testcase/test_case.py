import pytest
from common.exceldata import Data
from common.excelconfig import DataConfig
from config import Conf
from utils.logutil import my_log
from utils.requestutil import Request
import json
import os
from utils.assertutil import AssertUtil
from common import base
import allure
@allure.feature()
class TestCase:
    def setup_class(self):
        global run_list, run_case
        self.data = DataConfig()
        self.asserte = AssertUtil()
        self.request = Request()
        self.log = my_log()
        case_name = Conf.get_excel_file()
        case_sheet = Conf.ConfigYaml().get_case_sheet()
        case_init = Data(case_name, case_sheet)
        run_list = case_init.get_case_list()
        run_case = case_init.get_run_data()
        data = run_list[0][self.data.params]
        res = self.request.post(data=data)
        # print(res)
        self.token = res["data"]["token"]
        self.uid = res["data"]["uid"]
        self.sessionkey = res["data"]["session_key"]

    def run_params(self, index):
        params = run_case[index][self.data.params]
        data = json.loads(params)
        data["token"] = self.token
        data["uid"] = self.uid
        data["sessionkey"] = self.sessionkey
        return data

    def test_01(self):
        data = self.run_params(1)
        res = self.request.post(data=data)
        print(res)
        self.asserte.assert_code(res["msg"], 306)

    def test_02(self):
        data = self.run_params(2)
        res = self.request.post(data=data)
        print(res)

    def test_03(self):
        data = self.run_params(3)
        res = self.request.post(data=data)
        self.asserte.assert_code(res["msg"], 0)

    def test_04(self):
        data = self.run_params(4)
        res = self.request.post(data=data)
        print(res)
        self.asserte.assert_code(res["msg"], 0)

    def test_05(self):
        params = run_case[5][self.data.params]
        data = json.loads(params)
        res = self.request.post(data)
        self.asserte.assert_code(res["msg"], 0)

    def test_06(self):
        params = run_case[6][self.data.params]
        data = json.loads(params)
        res = self.request.post(data)
        self.asserte.assert_code(res["msg"], 0)

    def test_07(self):
        params = run_case[7][self.data.params]
        data = json.loads(params)
        res = self.request.post(data)
        self.asserte.assert_code(res["msg"], 0)

    def test_08(self):
        params = run_case[8][self.data.params]
        data = json.loads(params)
        res = self.request.post(data)
        self.asserte.assert_code(res["msg"], 0)

    def test_09(self):
        params = run_case[9][self.data.params]
        data = json.loads(params)
        res = self.request.post(data)
        self.asserte.assert_code(res["msg"], 0)


if __name__ == "__main__":
    report_path = Conf.get_report_path() + os.sep + "result"
    report_html_path = Conf.get_report_path() + os.sep +"html"
    pytest.main(["-s", "test_case.py", "--alluredir", report_path])
    base.allure_report("../report/result", "../report/html")