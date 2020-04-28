from utils.excelutil import ExcelUtil
from common.excelconfig import DataConfig
import json
class Data:
    def __init__(self, testcase_file, sheet_name):
        # 使用excel工具类，获取结果list
        self.reader = ExcelUtil(testcase_file, sheet_name)

    def get_run_data(self):
        """
        根据是否运行列 == y 获取执行测试用例
        :return:
        """

        run_list = list()
        for line in self.reader.data():
            if line != 0:
                if str(line[DataConfig().is_run]).lower() == "yes":
                    # print(line, '\n')
                    run_list.append(line)
        # print(run_list)
        return run_list

    def get_case_list(self):
        """
        获取全部测试用例
        :return:
        """
        run_list = [line for line in self.reader.data()]
        return run_list

    def get_case_pre(self, per):
        """
        获取全部测试用例
        list判断， 执行， 获取
        :return:
        """
        run_list = self.get_case_list()
        for line in run_list:
            if per in dict(line).values():
                return line
        return None


if __name__ == "__main__":
    data = Data("../data/app.pyhongxing_case.xlsx", 0)
    print(data.get_case_pre("登录"))