from email import message
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
now = datetime.now()

url='https://www.prat.idf.il/'
url2='https://nofesh.prat.idf.il/#SearchDeals'
#put here your id 
taodat_zehot = "*********"
#put here your password
user_password = "********"

#if you put date you must need to delete remarks date in #1 place
from_date_data='26/05/22'
#if you put date you must need to delete remarks date in #2 place
to_data_data='29/05/22'
#if you put date you must need to delete remarks city in #3 place
city='דן אילת 2022'
#if you put date you must need to delete remarks type in #4 place
typeHotel='מבוקש'



#send the mail
def sendMAil(arr):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    
    sender_email = "********" #put here the mail you want that send your results -> you need to open a new one mail in google and open the security for small low security software.  
    password = "********"#put here the password of new one mail.
    receiver_email = "sagieka@gmail.com" #put here the mail that you want to recive the mails.
    
    mess = MIMEMultipart("alternative")
    message="""המלונות הפתוחים לפי התאמתך הם:\n"""
    for text in arr:
        message+="""{0}\n""".format(text)
    
    part1 = MIMEText(message, "plain")
    mess.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, mess.as_string()
        )


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url2)

IdNumber = driver.find_elements_by_id("IdNumber")
IdNumber[0].send_keys(taodat_zehot)

password = driver.find_elements_by_id("Password")
password[0].send_keys(user_password)
driver.find_element_by_xpath('//*[@id="submitLogin"]').click()

"""a 1 place:"""
# from_date=driver.find_elements_by_id("fromDateInput")   
# from_date[0].send_keys(from_date_data)
"""a 2 place:"""
# to_date=driver.find_elements_by_id("toDateInput")
# to_date[0].send_keys(to_data_data)
"""a 3 place:"""
# area=driver.find_elements_by_id("areaHoteltxt")
# area[0].send_keys(city)
"""a 4 place:"""
# type=driver.find_elements_by_id("hotelTypeSelected")
# type[0].send_keys(typeHotel)

time.sleep(2)

driver.find_element_by_xpath('//*[@id="searchButton"]').click()

time.sleep(3)
value = driver.find_elements_by_xpath('//h3[contains(@class, "name")]')
arr=[]
for i in value:
    print(i.text)
    arr.append(i.text)

if len(arr)==0:
    print('not send')
else:
    sendMAil(arr)
    print('send')

time.sleep(3)
driver.close()