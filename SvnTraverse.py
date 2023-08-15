###
    # 本脚本使用的是Edge浏览器，请自行下载对应的webdrive版本：
    # 参考链接：https://blog.csdn.net/tk1023/article/details/109078613
    # https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/
    # https://msedgewebdriverstorage.z22.web.core.windows.net/
    # 下载之后需将"msedgedriver.exe"修改为"MicrosoftWebDriver.exe"，并将该文件放入python3的安装文件夹目录下
###

import xlwt
import os 
import datetime
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def duqu():
    ## 读取
    global num_h,nm_h,tmp,tag
    sleep(1)

    for i in range(1,1000,1):
        try:  
        # 尝试查找XPath, 定位到文件/文件夹项
            element = driver.find_element(By.XPATH, value=f'//*[@id="directory-list"]/div[2]/a[{i}]')
            elementname = driver.find_element(By.XPATH, value=f'//*[@id="directory-list"]/div[2]/a[{i}]/span[2]')
        
        # 如果找到元素，则执行所需操作  

            ## 项目类型 文件夹还是文件
            a = element.get_attribute('class')
            ## 文件夹/文件名字
            b = elementname.text
           
            # sleep(1)
            print(b)
            if a == 'table-row dir':
                ## 如果是文件夹，则继续递归遍历
                # dictt.append(b)
                tmp_tmp = tmp
                if tag != 0:
                    # for ii in range(tag):
                    #     tmp = tmp + '.' + str(i)
                    tmp = tmp + '.' + str(i)
                    b = str(nm_h) + tmp + ' - ' + b
                
                worksheet.write(num_h, 0, b, style)
                num_h = num_h + 1
                element.click()
                tag = tag + 1
                duqu()
                tmp = tmp_tmp
                tag = tag - 1
            else:
                # dictt.append(b)
                b = str(nm_h) + tmp + '.' + str(i) + ' - ' + b
                worksheet.write(num_h, 0, b)
                num_h = num_h + 1

        # 如果未找到元素，则执行所需操作  
        except NoSuchElementException: 
            # tmp = ' '
            # dictt.append(tmp)
            driver.find_element(By.XPATH, value='//*[@id="repo-content"]/div/div[1]/a').click()
            if tag == 1:
                nm_h = nm_h + 1
            sleep(1)
            break
    return 1


## 设置遍历的目录字典
# dictt = []
options = webdriver.EdgeOptions()

## 取消ssl验证
options.add_experimental_option ("detach", True)
options.add_argument('ignore-certificate-errors')

## 设置是否开启浏览器预览, 默认不开启。如若开启请注释下列两行
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Edge(options=options)

# # 账号密码信息
# # 这里填写账号密码信息
username="username"
passwd="password"

## 开始访问SVN

## 这里放你的SVN地址
url_ip = "x.x.x.x/svn/XXXX/"

driver.get(rf'https://{username}:{passwd}@{url_ip}')
sleep(1)

 
print('目录')

## 进入目录
driver.find_element(By.XPATH, value='//*[@id="directory-list"]/div[2]/a').click()

## 开始读取, num_h为excel行， tag为标识缩进， nm_h为行前的大数字， l为列
num_h = 0
tag = 0
nm_h = 0
tmp = ''



style = xlwt.XFStyle()  
style.font.bold = True
workbook = xlwt.Workbook() 
worksheet = workbook.add_sheet('Sheet1')  
duqu()


today = datetime.datetime.today()
year = today.year
month = today.month
day = today.day
# 这是保存的excel文件名
file_name = f'SVN目录-{year}年{month}月{day}日.xls'
if(os.path.isfile(file_name)):
    os.remove(file_name)


worksheet.col(0).width = 256 * 125

# set_row_heights()
workbook.save(file_name)

driver.quit()
print('\n目录遍历完成')




