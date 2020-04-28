
# 定义类
class DataConfig:
# 定义属性
    # 用例ID	模块	接口名称	请求URL	前置条件	请求类型	请求参数类型
    # 请求参数	预期结果	实际结果	备注	是否运行	headers	cookies	status_code	数据库验证
    # 用例ID
    # caseid	模块	是否执行	前置条件	headers	url	method	data	预期结果方式	status_code


    case_id = "caseid"
    case_model = "模块"
    # case_name = "接口名称"
    is_run = "是否执行"
    pre_exec = "前置条件"
    headers = "headers"
    url = "url"
    # pre_exec = "前置条件"
    method = "method"
    # params_type = "请求参数类型"
    # params = "请求参数"
    params = "data"
    expect_result = "预期结果方式"
    # actual_result = "实际结果"
    # is_run = "是否运行"
    # headers = "headers"
    # cookies = "cookies"
    code = "status_code"
    # db_verify = "数据库验证"
