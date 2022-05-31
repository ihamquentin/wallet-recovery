from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
#!!!
import functions as mf #this file 'functions.py' is in the same folder. it is required for this program to run
#!!!


EXTENSION_PATH =  ''  #enter the path to the binance extention .crx file here
mm_extension_id = "" #enter your binance extension id here
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(options=opt)

#driver.switch_to.window(driver.window_handles) #switch to first window
#driver.get('chrome-extension://'+mm_extension_id)

driver.get('chrome-extension://'+mm_extension_id+'/home.html#/en/setup/recover') #go to seed phrase page
time.sleep(1)
#driver.find_element(by = By.XPATH, value= '//*[@id="import-srp__srp-word-0"]') #select textbox

#ENTER SEED WORDS, current COUNT:
# stomach jelly grab dial knee olympic palm snake all deer screen feed
seed_words = ['velvet',
'finger',
'opera',
'stomach',
'shock',
'throw',
'palm',
'hurt',
'olympic',
'okay',
'tide',
'feed']
password = '12345678@A'
count = 1 #starts at 1, input 'n' to start at 'n'th permutation
#EDITABLE ^^^

keys = [i for i in range(1,13)]
seed_words = dict(zip(keys, seed_words))

s = ''
arr = [0,1,2,3,4,5,6,7,8,9,10,11]
#get starting point:
arr = mf.getPermutation(len(arr), count)

#print starting string and starting array:
print("START:",arr, [seed_words[i] for i in arr])

#loop through permuations:
t0 = time.time()
looper = True
while looper:
    #populate string:
    s = ''
    for i in arr:
        s += ' ' + seed_words[i]
    s.strip()

    #mf.copy2clipmac(s) #copy string
    #driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/form/div[1]/div/div/div/div[5]/div/textarea').send_keys(Keys.COMMAND + 'v') #paste string

    #if invalid seed phrase:
    

    #if valid seed phrase:
    #if valid seed phrase:
    try:
        #enter into wallet:
        driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/form/div[1]/div/div/div/div[5]/div/textarea').send_keys(s.strip())
        driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/form/div[1]/div/div/div/div[7]/div/input').send_keys(password) #enter pass
        driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/form/div[1]/div/div/div/div[9]/div/input').send_keys(password) #enter pass2
        
        driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/form/div[1]/div/div/div/div[12]/div[1]').click() #agree to terms
        driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/form/div[2]/button/div').click() #import wallet
        time.sleep(2)
        

        try:
            with open('Binancephrases.txt', 'a') as out:
                #once in wallet
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                #elem1 = soup.find('span', {'class':"sc-ljRboo cSrOkG"})
                #elem2 = soup.find('span', {'class':"sc-jmhFOf cLJGT"})
                ballance = soup.find('span', {'class': 'sc-fmlJLJ eyMhHH'})
                usd = float(ballance.text[:4]) #get balance usd
                if usd <= 0.005:
                    arr = mf.nextPermutation(arr)
                    looper = True
                    print(count, f'empty account:{ballance.text} ', s)
                    out.write(f'empty account {ballance.text}:, {s}/n')
                    out.flush()
                    count += 1

                    #driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div').click() #click on profile
                    #driver.find_element(by = By.XPATH, value = '//*[@id="app-content"]/div/div[3]/div[2]/button').click() #click 'lock' account
                    time.sleep(0.01)
                    driver.get('chrome-extension://'+mm_extension_id+'/home.html#/en/setup/recover')
                else:
                    looper = False
                    print("DONE",s, '$', str(usd))
                    out.write(f'DONE: {s}, $: {ballance.text} /n')
                    out.flush()
                    print(count)
        except KeyboardInterrupt:
            out.close()
    except:
        driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/form/div[1]/div/div/div/div[5]/ul/li') #check to see if invalid message pops up
        #get next perm, increment
        arr = mf.nextPermutation(arr)
        print('Attempts', count, end = '\r', flush = False)
        print('count/sec:', "{:.2f}".format(count/(time.time()- t0)), '---- count:',count, end='\r', flush=True)
        count += 1
        driver.get('chrome-extension://'+mm_extension_id+'/home.html#/en/setup/recover')


