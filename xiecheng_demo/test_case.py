from pyse import Pyse, TestCase, TestRunner
from parameterized import parameterized
import os


class Test(TestCase):
    """Baidu serach test case"""

    @classmethod
    def setUpClass(cls):
        """ Setting browser driver, Using chrome by default."""
        cls.driver = Pyse("chrome")
        cls.timeout = 15  # You can customize timeout time


    def login(self):
        self.open("https://192.168.0.238")
        self.max_window()
        self.sleep(5)
        self.type("id=>accountName","2@2")
        self.type("id=>password","2WXeRM")
        self.sleep(2)
        self.click("xpath=>//*[@id='loginform']/fieldset/div[3]/button")
        self.sleep(5)
    #上传更新包
    def test_AssetManagement(self):
        Test.login(self)
        self.click("link_text=>资产管理")
        self.click("link_text=>终端部署")
        self.sleep(5)
        self.click("id=>btnUpdate")
        self.sleep(2)
        self.click("id=>chooseUpdatefile")
        self.sleep(5)
        os.system(r'E:\明镜.exe "E:\LongBright-V2.1.0 B30.zip"')
        self.sleep(2)
        self.click("id=>Updateadd")
        self.sleep(5)
        self.click("link_text=>确定")
        self.sleep(5)
      #  self.close()

    def test_TaskManagement(self):
       # Test.login(self)
        self.click("link_text=>任务管理")
        self.click("link_text=>补丁任务")
        self.sleep(5)
        self.click("id=>btnAdd")
        self.sleep(5)
        self.click("id=>strategySelecting")



if __name__ == '__main__':
    runner = TestRunner('./', '明镜测试', '测试环境：Chrome')
    runner.run()

'''
说明：
'./' ： 指定测试目录。
'百度测试用例' ： 指定测试项目标题。
'测试环境：Chrome' ： 指定测试环境描述。

debug() # debug模式不生成测试报告
run()   # run模式生成测试报告
'''

