# SearchNofeshKeva
#-----------------------------------------------------------------------------------#


# install python 3.X 
# install with pip: selenium, MIMEMultipart,MIMEText.


# you need to look of remarks:

put here your id : #taodat_zehot = "*********"

put here your password:#user_password = "********"

if you put date you must need to delete remarks date in #1 place: #from_date_data='26/05/22'

if you put date you must need to delete remarks date in #2 place:#to_data_data='29/05/22'

if you put date you must need to delete remarks city in #3 place:#city='דן אילת 2022'

if you put date you must need to delete remarks type in #4 place:#typeHotel='מבוקש'

sender_email = "********"put here the mail you want that send your results -> you need to open a new one mail in google and open the security for small low security software.

password = "********" #put here the password of new one mail.

receiver_email = "sagieka@gmail.com" #put here the mail that you want to recive the mails.

"""a 1 place:"""
#from_date=driver.find_elements_by_id("fromDateInput")   
#from_date[0].send_keys(from_date_data)

"""a 2 place:"""
#to_date=driver.find_elements_by_id("toDateInput")
#to_date[0].send_keys(to_data_data)

"""a 3 place:"""
#area=driver.find_elements_by_id("areaHoteltxt")
#area[0].send_keys(city)

"""a 4 place:"""
#type=driver.find_elements_by_id("hotelTypeSelected")
#type[0].send_keys(typeHotel)

write in terminal : python find-order.py

and run it! good luck!
