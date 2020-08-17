1，
2，项目版本更新说明
 0.1：处理了XX问题
 0.2 。。。。

‘’‘
发邮件
记录log
动态处理数据
测试用例关联，后面充值，都要依赖登录
正则表达式
数据库状态
’‘’
’‘’
前程贷项目的接口实现
注册
登录
充值
提现
添加项目
审核项目
投资
获取项目
‘’‘

DDT  htmltestrunner修改版的放在接口框架的libs下

#logger
#yaml

配置文件：
1.py 非常灵活，只有Python代码适用
2.yaml文件， 通用Java，读取解析简单智能
3.ini，读取负责，旧的项目用的多

框架的分层
1、测试代码主入口，run_test.py
2、测试逻辑/用例包,test_cases，各个模块的测试用例方法
3、数据管理层，excel，csv，py文件-list，dict，yaml文件等
4、业务逻辑层，requests_handler,excel_handler通用的
# logger 访问数据库
5、配置文件（和项目是相关的，项目地址，数据库地址，logger级别）
6、测试报告（输出）

