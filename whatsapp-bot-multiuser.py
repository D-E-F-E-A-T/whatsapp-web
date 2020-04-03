from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
#username 
all_names = ['mahmoud','youmnty']
msg = "This Message was sent using a Python script!"
count = int(input('Enter the count : '))
input('Enter anything after scanning QR code')

for name in all_names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_xpath("//*[@id='main'] /footer/div[1]/div[2]/div/div[2]")

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_xpath("//* [ @id='main'] /footer/div[1]/div[3]/button")
        button.click()
print("success")