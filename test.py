from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import winsound
import time
import ctypes
import sys

saturdays = ["7", "21", "28"]
sundays = ["1", "15", "22", "29"]
driver = webdriver.Chrome('./chromedriver')

driver.get("https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S220414202040183665&code=T500&dCode=T502&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EB%82%9C%EC%A7%80&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&sch_reqst_value=")
# driver.get("https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S220414192158211658&code=T500&dCode=T502&sch_order=1&sch_choose_list=&sch_type=&sch_text=&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&sch_reqst_value=")


driver.find_element(by=By.CLASS_NAME, value="pop_x").click()

counter = 0

while True:

    element = driver.find_element(by=By.XPATH, value='//*[@id="calendar"]/table/tbody')

    tds = element.find_elements(by=By.TAG_NAME, value="td")
    for td in tds:
        nm = td.get_attribute("class")
        if nm == "able":
            winsound.Beep(2500, 1000)
            date = td.find_element(by=By.TAG_NAME, value="span").text
            if date in saturdays:
                ctypes.windll.user32.MessageBoxW(0, "Saturday :" + date, "alert", 1)
                driver.close()
            if date in sundays:
                ctypes.windll.user32.MessageBoxW(0, "Sunday :" + date, "alert", 1)
                driver.close()
    if counter==10 :
        print("-")
        counter = 0
    else :
        print(".")
        counter+=1
    
    driver.refresh()
    time.sleep(10)
    driver.find_element(by=By.CLASS_NAME, value="pop_x").click()
