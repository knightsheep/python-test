import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TrainTicketBot:
    def __init__(self,from_station, to_station, departure_time):
        self.from_st = from_station
        self.to_st = to_station
        self.de_time = departure_time
        self.options = Options()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-infobars')
        self.driver = webdriver.Chrome(self.options)
        self.driver.maximize_window()


    def is_element_exist(self, element):
        #判断元素是否存在
        flag = True
        try:
            self.driver.find_element(By.XPATH, element)
            return flag
        except:
            flag = False
            return flag


    #选择可购买车票信息
    def check_ticket(self):
        self.driver.get("https://kyfw.12306.cn/otn/resources/login.html")

        while not self.is_element_exist('//a[@class="txt-primary underline"]'):
            time.sleep(1)

        self.driver.find_element(By.XPATH, '//a[@class="txt-primary underline"]').click()

        try:
            # 出发地站点
            self.driver.find_element(By.XPATH, '//input[@id="fromStationText"]').click()
            self.driver.find_element(By.XPATH, '//input[@ids="fromStationText"]').send_keys(self.from_st)
            self.driver.find_element(By.XPATH, '//span[@class="ralign"]').click()
            time.sleep(0.5)

            # 目的地站点
            self.driver.find_element(By.XPATH, '//input[@id="toStationText"]').click()
            self.driver.find_element(By.XPATH, '//input[@id="toStationText"]').send_keys(self.from_st)
            self.driver.find_element(By.XPATH, '//input[@class="ralign"]').click()
            time.sleep(0.5)

            # 出发时间
            self.driver.find_element(By.XPATH, '//input[@id="train_date"]').clear()
            self.driver.find_element(By.XPATH, '//input[@id="train_date"]').send_keys(self.de_time)
            time.sleep(0.5)

            # 定位搜索
            self.driver.find_element(By.XPATH, '//a[@id="query_ticket"]').click()
            time.sleep(0.5)

            # 预定车票
            self.driver.find_element(By.XPATH, '//a[@text()="预订"]').click()
            time.sleep(0.5)


            # 选择乘车人
            self.driver.find_element(By.XPATH, '//input[@title="设置为乘车人，按空格键进行操作"]').click()
            time.sleep(0.5)
            print("选择成功")

            # 提交订单
            self.driver.find_element(By.XPATH, '//a[@text()="提交订单"]').click()
            print("提交成功")
            time.sleep(5)

            self.driver.find_element(By.ID, 'qr_submit_id').click()
            print('确认成功')

        except Exception as e:
            print('=========重试中==========')


        print("请在15min内支付订单")

        time.sleep(120)



if __name__ == '__main__':
    # 定义出发地与目的地
    from_station = "重庆北"
    to_station = "成都东"
    departure_time = "2025-10-01"


    Test = TrainTicketBot(from_station, to_station, departure_time)
    Test.check_ticket()































