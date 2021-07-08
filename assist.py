# ---------------------------------------------------------------------------------------- KSX ---------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------- CREATED BY KUNAL SEN ------------------------------------------------------------------------------------------

#importing all modules:-
import speech_recognition as sr
import pyttsx3  
import os 
import datetime
import wikipedia 
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyautogui
import math
from playsound import playsound
import requests
from PIL import Image, ImageGrab
import string
import random
import cv2
import serial
import cmath
from bs4 import BeautifulSoup

# s = time.time()
#initial of the KSX voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')



def speakf(audio):
    engine.setProperty("rate",127)
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
def speakm(audio):
    engine.setProperty("rate",175)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


#wishing by time


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speakm("Good Morning!")

    elif hour>=12 and hour<18:
        speakm("Good Afternoon!")   

    else:
        speakm("Good Evening!")  

    speakm("I am ksx Sir. Please tell me how may I help you")  
    com()


#taking the commands:-



def takeCommand1():
    #It takes microphone input from the user and returns string output

    t = sr.Recognizer()
    with sr.Microphone() as source1:
        speakm('I am listening speak')
        print("Listening...")
        t.pause_threshold = 1.5
        audio = t.listen(source1)

    try:
        print("Recognizing...")    
        query1 = t.recognize_google(audio, language='en-in')
        print(f"You said: {query1}")
        return query1

    except Exception as e:
        # print(e)    
        speakm("Sorry could not recognize what you said")
        print("Sorry could not recognize what you said")  
        return ''
  


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speakf('speak sir')
        print("Listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query

    except Exception as e:
        # print(e)    
        speakm("Sorry could not recognize what you said")
        print("Sorry could not recognize what you said")  
        return ''
        
    


#-------------------------------------------------------------------------------- Main Body --------------------------------------------------------------------------------------------------





def com():
    s = time.time()
    while True:

    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:

                speakm('Searching Wikipedia...')
                print('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speakm("According to Wikipedia")
                print(results)
                speakm(results)
            except Exception as wiki:
                # print(wiki)
                speakm('error') 
                print('error')   
        # elif 'search files' in query or 'search file' in query:
        #     def src():

        #         speakm('say the name of the file')
        #         srch = takeCommand().lower()
                
        #         pyautogui.click(12,1057)
        #         pyautogui.typewrite('this pc')
        #         time.sleep(1)
        #         pyautogui.click(77,538)
        #         time.sleep(1)
        #         # pyautogui.moveTo(1764,155)
        #         pyautogui.click(1764,155)
        #         pyautogui.typewrite(srch)
        #     src()    
                 
        elif 'weather' in query or 'forcast' in query or 'weather forcast' in query:
            def banku():
                city = 'Bankura'

                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=0dfd0858683905639ed72d2af8ffebff'.format(city)
                res = requests.get(url)

                data = res.json()

                tempmax = data['main']['temp_max']
                tempmin = data['main']['temp_min']
                humidity = data['main']['humidity']
                tempmax = tempmax - 273
                tempmin = tempmin - 273
                t = round(tempmax)
                t1 = round(tempmin)
                wind = data['wind']['speed']
                print('He said : \n')
                
                if t == t1:
                    speakm(f'The average temparature is {t} degree celcius')
                    print(f'The average temparature is {t} degree celcius')

                else:
                    speakm(f'The temparature is {t1} degree celcius to {t}degree celcius')
                    print(f'The temparature is {t1} degree celcius to {t}degree celcius')
                speakm(f'The wind speed is {wind}meter per second')
                speakm(f'The humidity level is {humidity}')
                print(f'The wind speed is {wind}m/s')
                print(f'The humidity level is {humidity}')    
            try:
                banku()
            except Exception as bn:
                # print(bn)
                print('sorry')    
        elif 'dino' in query:
            speakm('ok playing daino game. but i am decent in that game')
            def auto_dino():
                def hit(key):
                    pyautogui.keyDown(key)
                    return

                def isCollide(data):
                    for i in range(255, 505):
                        for j in range(520, 650):
                            if data[i, j] > 80 and data[i, j]<255:
                                
                                hit("up")
                                return
                    # Draw the rectangle for birds
                    for i in range(300, 415):
                        for j in range(410, 563):
                            if data[i, j] > 80 and data[i, j] < 255:
                                hit("down")
                                return

                    
                    return


                driver = webdriver.Chrome('C:\\webdrivers\\chromedriver')
                driver.get('chrome://dino')
                driver.maximize_window()
                print("Hey.. Dino game about to start in 3 seconds")
                time.sleep(1)
                hit('up') 
                # time.sleep(2)
                def wh():

                    while True:
                        image = ImageGrab.grab().convert('L')  
                        data = image.load()
                        isCollide(data)

                try:
                    wh()
                    
                except Exception as e:
                    # print(e)
                    print('over')
                    # v = input('agin?')
                    # if v == 'y':
                    #     driver.find_element_by_xpath('/html/body/div[1]/div[4]/canvas').click()
                    # else:
                    #     exit() 
            auto_dino()         
        elif 'take' in query and 'photo' in query:
            def takephoto():
                speakm('ok taking photo please wait')
                print('He said : Taking photo')
                pyautogui.moveTo(12,1057,0.5)
                pyautogui.click()
                time.sleep(1)
                pyautogui.typewrite('camera')
                time.sleep(2)
                pyautogui.moveTo(77,538,1)  
                pyautogui.click() 
                time.sleep(2)
                speakm('get ready i am about to take the photo')
                pyautogui.click(1861,537)
                time.sleep(1)
                speakm('clicked')
                speakm('here is the photo')
                pyautogui.click(1864,1015)
            takephoto()        

        elif 'active cases' in query:
            def cor():
                
                rum = requests.get("https://www.mohfw.gov.in/")
                rum1=rum.text
                # print(rum1)
                soup = BeautifulSoup(rum1, 'html.parser')
                # print(soup)
                tr_data = ""
                for table in soup.find_all('tbody')[0].find_all('tr'):
                    tr_data += table.get_text()
                tr_data = tr_data[1:]    
                items = tr_data.split("\n\n")
                speakm('ok type the name of the state')
                state = input('ok type the name of the state : ')
                state1 = state.split()
                # print(state1)
                # print(len(state1))
                n1 = int(len(state1))
                for item in items[0:35]:
                    corona_list = item.split('\n')
                    u1 = 0
                    if corona_list[1] in state1[0:n1]:
                        # print(corona_list[2])
                        u1 = u1 + 1
                        # print(state1[u1])
                newstate = string.capwords(state)
                # print(newstate)        
                for item in items[0:35]:
                    corona_list = item.split('\n')
                    if corona_list[1] in newstate:
                        act=corona_list[2]
                        # print(newstate)
                    else:
                        act='not found'    
                        
                speakm(f"the current active cases of {state} is almost {act} due to Covid-19")
                print(f"The current active cases of {state} is almost {act} due to Covid-19")



            cor()            
        elif 'disconnect the wi-fi' in query or 'wifi disconnect' in query:
            try:

                speakm('disconnecting from wi-fi')
                print('He said : Disconecting from wifi')
                pyautogui.click(1707,1065)
                time.sleep(3)
                pyautogui.click(1822,589)
                speakm('disconnected')
                print('He said : Disconnected')
            except Exception as wi:
                # print(wi)
                print('error in disconected wi-fi')    
        elif 'write a print statement and run' in query or 'print' in query:
            def prin1():

                speakm('what should i print?')
                pr = input('What should I print : ')
                speakm('ok! wait')
                pyautogui.click(1046,351)
                nm = random.choice(string.ascii_letters)
                rn = random.randint(1,2000)
                pri = f'{nm}{rn}.py'
                time.sleep(1)
                pyautogui.hotkey('ctrl','n')
                pyautogui.hotkey('ctrl','s')
                time.sleep(3)
                pyautogui.typewrite(pri)
                pyautogui.click(371,45)
                pyautogui.hotkey('ctrl','c')
                time.sleep(2)
                pyautogui.click(387,435)
                time.sleep(1)
                pyautogui.keyDown('enter')
                time.sleep(3)
                pyautogui.write(f"print('{pr}')",interval=0.1)
                time.sleep(3)
                pyautogui.hotkey('ctrl','s')
                pyautogui.click(12,1057)
                time.sleep(1)
                pyautogui.typewrite('cmd')
                
                time.sleep(2)
                pyautogui.click(77,538) 
                time.sleep(1)
                pyautogui.typewrite('cd..')
                pyautogui.keyDown('enter')
                pyautogui.typewrite('cd..')
                pyautogui.keyDown('enter')
                pyautogui.typewrite("D:")
                pyautogui.keyDown('enter')
                pyautogui.typewrite('cd ')
                pyautogui.hotkey('ctrl','v')
                # pyautogui.typewrite('cd assistant(ks)')
                pyautogui.keyDown('enter')
                time.sleep(0.4)
                pyautogui.typewrite(f"python {pri}")
                time.sleep(0.5)
                pyautogui.keyDown('enter')
            try:
                prin1()
            except Exception as prn:
                # print(prn)
                speakm('error, try again') 
                print('He said : Try again')       

        elif 'open file manager' in query or 'open my computer' in query or 'open this pc' in query or 'launch this pc' in query or 'this pc' in query or 'go to this oc' in query:
            try:

                speakm('opening this pc')
                print('He said : Opening this pc')
                pyautogui.click(12,1057)
                pyautogui.typewrite('this pc')
                time.sleep(1)
                pyautogui.click(77,538) 
            except Exception as fm:
                # print(fm)
                print('error in opening file manager')     
        elif 'go to the d drive' in query or 'd drive' in query or 'open d drive' in query or 'launch d drive' in query or 'go to d drive' in query:
            speakm('opening d drive')
            print('He said : opening D drive')
            pyautogui.moveTo(12,1057,0.5)
            pyautogui.click()
            pyautogui.typewrite('this pc')
            time.sleep(1)
            pyautogui.moveTo(77,538,0.5)
            pyautogui.click() 
            time.sleep(1)
            pyautogui.moveTo(529,382,0.5) 
            pyautogui.doubleClick()
        elif 'go to the e drive' in query or 'e drive' in query or 'open e drive' in query or 'launch e drive' in query or 'go to e drive' in query or 'open the last drive' in query or 'open last drive' in query or 'open the third drive' in query or 'open third drive' in query or 'third drive' in query or 'last drive' in query:
            speakm('opening e drive')
            print('He said : opening E drive')
            pyautogui.click(12,1057)
            pyautogui.typewrite('this pc')
            time.sleep(1)
            pyautogui.click(77,538) 
            time.sleep(1)
            pyautogui.doubleClick(810,386)    
        elif 'dolby' in query:
            speakf('opening dolby atmos')
            print('He said : Opening Dolby Atmos') 
            pyautogui.moveTo(12,1057,0.5)
            pyautogui.click()
            pyautogui.typewrite('dolby audio')
            time.sleep(2)
            pyautogui.moveTo(77,538,1)  
            pyautogui.click()   
        elif 'dashlane' in query:
            speakf('opening dashlane')
            print('He said : Opening Dashlane') 
            pyautogui.moveTo(12,1057,0.5)
            pyautogui.click()
            pyautogui.typewrite('dashlane')
            time.sleep(2)
            pyautogui.moveTo(77,538,1)  
            pyautogui.click()            
        elif 'camera' in query:
            speakm('opening camera')
            print('He said : Opening Camera')
            pyautogui.moveTo(12,1057,0.5)
            pyautogui.click()
            time.sleep(1)
            pyautogui.typewrite('camera')
            time.sleep(2)
            pyautogui.moveTo(77,538,1)  
            pyautogui.click() 
        elif 'xampp' in query:
            speakm('opening xampp')    
            print('He said : Opening XAMPP')
            pyautogui.moveTo(310,1073,0.5)
            pyautogui.click()
        elif 'settings' in query or 'setting' in query:
            speakm('opening settings')
            print('He said : Opening Settings')
            pyautogui.moveTo(12,1057,0.5)
            pyautogui.click()
            pyautogui.typewrite('settings')
            time.sleep(2)
            pyautogui.moveTo(77,538,1)  
            pyautogui.click()   
        elif 'capital of india' in query:
            speakm('The capital of india is Delhi')
            print('He said : Delhi') 
        elif 'inventor of windows' in query or 'who invented the windows' in query or 'invented windows' in query:
            speakm('windows operating system is invented by Bill Gates')    
            print('He said : Bill Gates')
        elif 'factorial' in query:
            
            def fac():

                try :
                    speakm('enter the number which you wana get factorial')
                    f = int(input('Enter the number : '))
                    b = math.factorial(f)
                    speakm('here is your factorial')
                    print(f'He said : {b}') 
                except Exception as k:
                    # print(k)
                    speakm('enter only number')
                    print('He said : Enter only number')
                    fac()
                    
            fac()    

        elif 'repeat after me' in query or 'say after me' in query or 'after me' in query:
            
            def tell():
                  query1 = takeCommand1().lower()
                  speakm(query1)
            tell()        
        elif 'do you talk' in query or 'you can talk' in query or 'do you talk to anyone' in query:
            speakm('i would love to talk')
        elif 'youtube' in query:
            speakm('opening youtube')
            # webbrowser.open("youtube.com")
            driver = webdriver.Chrome('C:\\webdrivers\\chromedriver')
            driver.get('https://youtube.com')
            driver.maximize_window()
            def yout():

                speakm('if you want to search anything in youtube then tell me?')  
                y = takeCommand()
                speakm(f'searching {y} in youtube')
                search = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input').send_keys(y)
                button = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button').click()
                
            yout()
        # elif 'facebook' in query:
        #     speakm('opening facebook')
        #     print('Opening Facebook')
        #     webbrowser.open("facebook.com")  
              
        elif query == 'open my site' or query == 'open my website' or query == 'launch my website' or query == 'launch my site':
            speakm('Opening your site')
            driver = webdriver.Chrome('C:\\webdrivers\\chromedriver')
            driver.get('https://kunal95.netlify.com')
            def log():
                speakm('You want to login in your website?')
                # l = input('You want to login in your website(Y/N) : ')
                l = takeCommand()

                l = l.upper()
                if 'YES' in l:
                    name = driver.find_element_by_xpath('/html/body/div[3]/center[2]/div/table/tbody/tr/th[2]/form/font/input[1]').send_keys('KUNAL')
                    email = driver.find_element_by_xpath('/html/body/div[3]/center[2]/div/table/tbody/tr/th[2]/form/font/input[2]').send_keys('ksen09067@gmail.com')
                    pas = driver.find_element_by_xpath('/html/body/div[3]/center[2]/div/table/tbody/tr/th[2]/form/font/input[3]').send_keys('kunal95')
                    time.sleep(2)
                    check = driver.find_element_by_xpath('/html/body/div[3]/center[2]/div/table/tbody/tr/th[2]/form/font/input[4]').click()
                    time.sleep(2)
                    button = driver.find_element_by_xpath('/html/body/div[3]/center[2]/div/table/tbody/tr/th[2]/form/font/button').click()
                    speakm('logged in to yokunalur site')
                    print('Logged in to your site')
                elif 'NO' in l:
                    speakm('ok! your site is opened')
                    print('He said : Ok! your site is opened')    
                else:
                    speakm('wrong value')
                    print('Type the right value')
                    log()  

            log()    
        elif 'open website' in query or 'website' in query:
            def ob():
                speakm('tell me the name of the website')
                def voi():
                    web = takeCommand()
                    driver = webdriver.Chrome('C:\\webdrivers\\chromedriver')
                    driver.get(f'https://{web}')
                voi()
            ob()        

        elif 'edit person database' in query or 'edit the person database' in query:
            def data():
                speakm("Which person's database you want to edit?")
                fd = input("Which person's database you want to edit : ") 
                fd = fd.upper()
                if fd == 'RAIMA':
                    
                    with open('info.txt','r') as q1:
                        q2 = q1.read()
                        print('Her previous data is ' + q2)
                        speakf('her previous data is ' + q2)
                    with open('info.txt','a') as q3:
                        speakm('Enter the new data about Raima')
                        t = input('Enter the new data about Raima')
                        q3.write('\n'+t+'\n')
                else:
                    speakm('No match found')
                    print('No match found') 
                    
                               
            data()
                       
        elif 'open google' in query:
            webbrowser.open("google.com")
            speakm('opening google')

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com") 
            speakm('opening stackoverflow')
            print('Opening Stackoverflow') 
        elif query == 'open notepad' or query == 'start notepad' or query == 'notepad':
            speakm('opening notepad')
            
            print('He said : opening notepad')
            os.system("start notepad")
            
            #  print('anything i can do?')
            #  audio = r.listen(source)
            #  text = r.recognize_google(audio)
            #  turn()
        elif query == 'where are you from' or query == 'where do you live':
            speakm('this is my home')
            print('He said : This is my home')
                
        elif query == 'how are you':
            print("He said : I'm good. what about you?")
        elif 'chrome' in query:
            speakm('opening chrome')
            print('opening chrome') 
            os.system("start chrome") 
             
        # elif query == 'open Chrome' or query == 'start Chrome' or query == 'Chrome':
        #     speakm('opening chrome')
        #     print("He said : Opening Chrome")
            # os.system("start chrome") 
        elif 'about raima' in query:
            def learn():
                with open('info.txt','r+') as f:
                    f1 = f.read()
                    speakf(f'she said that{f1}')
            learn()    
        elif 'whatsapp' in query:
            speakm('opening whatsapp')
            print('Opening Whatsapp')
            os.startfile('C:\\Users\\KUNAL\\AppData\\Local\\WhatsApp\\WhatsApp.exe')  
        elif 'ms office word' in query or 'microsoft office word' in query or 'microsoft office word ' in query or 'office word' in query or 'office word' in query:
            try:

                def op():

                    speakm('ok! opening ms office')
                    print('Opening MS-Office')
                    os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk')
                def op1():
                    def w():
                        speakm('which type do you want blank or blog post?')
                        v = takeCommand().lower()
                        if 'blank' in v:
                            x = 651
                            y = 284
                            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk')
                            time.sleep(3)
                            pyautogui.click(17,19)
                            # print(x,y)
                            time.sleep(0.3)
                            pyautogui.click(48,66)
                            time.sleep(0.5)
                            pyautogui.click(x,y)
                            pyautogui.click(1389,928)
                            speakm('created blank document')
                            print('created blank document')
                            # pyautogui.click(651,284)
                        elif 'post' in v or 'blog' in v:
                            x = 755
                            y = 288
                            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk')
                            time.sleep(3)
                            pyautogui.click(17,19)
                            # print(x,y)
                            time.sleep(0.3)
                            pyautogui.click(48,66)
                            time.sleep(0.5)
                            pyautogui.click(x,y)
                            pyautogui.click(1389,928)
                            speakm('created blog post document')
                            print('created blog post document')
                            # pyautogui.click(755,288) 
                        elif 'anything' in v or 'any of them' in v or 'any' in v:
                            x = 651
                            y = 284
                            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk')
                            time.sleep(3)
                            pyautogui.click(17,19)
                            # print(x,y)
                            time.sleep(0.3)
                            pyautogui.click(48,66)
                            time.sleep(0.5)
                            pyautogui.click(x,y)
                            pyautogui.click(1389,928)
                            speakm('created document')
                            print('created document')

                        else:
                            speakm('just say blank or blog post')
                            print('just say blank or blog post :')    
                            w()
                    w()        
                if 'new file' in query or 'new' in query:
                    op1()
                else:
                    op()        
            except Exception as e1:
                print(e1)
                print('error') 



        elif 'magnifier' in query:
            speakm('opening magnifier')
            print('Opening Magnifier')
            os.startfile('C:\\Windows\\System32\\Magnify.exe') 
        elif 'screenshot' in query:
            try:
                ss = ImageGrab.grab()
                ss.load()
                ss.show()    
            except Exception as s:
                # print(s)
                speakm("Can't take screenshot")
                print("He said : Can't take screenshot")

        elif 'keyboard' in query:
            speakm('opening onscreen keyboard')
            print('Opening onscreen keyboard')
            os.startfile('C:\\Windows\\System32\\osk.exe') 
        elif 'my facebook account' in query:
            speakm('opening your facebook account')
            print('Opening your facebook account')
            driver = webdriver.Chrome('C:\\webdrivers\\chromedriver')
            driver.get('https://facebook.com')
            num = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input').send_keys('9475622804')
            passd = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input').send_keys('Kunalsen95%')
            button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input').click()    
        elif 'quick heal' in query:
            speakm('opening quickheal antivirus')
            print('opening QuickHeal')
            os.startfile("C:\\Program Files\\Quick Heal\\Quick Heal Total Security\\SCANNER.EXE")  
        elif 'antimalware' in query:
            os.startfile("C:\\Program Files\\Quick Heal\\Quick Heal Total Security\\ASMAIN.EXE")      
        elif query == 'open command prompt' or query == 'cmd' or query == 'start command prompt' or query == 'command prompt' or query == 'run command prompt' or query == 'run cmd' or query == 'open cmd':
            speakm('opening commandprompt') 
            print('Opening Command Prompt')
            os.startfile('C:\\Windows\\System32\\cmd.exe')       
        elif 'arduino' in query:
            speakm('starting arduino')
            os.startfile('D:\\Programme Files\\arduino-1.8.9-windows\\arduino-1.8.9\\arduino.exe')   
            print('He said : Starting Arduino') 
        elif 'turn' in query:
            # def led():


            
            def led_on():
                ser = serial.Serial('COM3',19200)
                def le():

                    speakm('enter the key')
                    led_pass = int(pyautogui.prompt('KSX', 'Enter the key'))
                    
                    if led_pass == 123456789:
                        speakm('ok turning on the LED')
                        print('He said : ok! turning on the led')
                        ser.write(b'1')
                        ser.close()
                    else:
                        speakm('wrong value try again')
                        le()
                le()


            def led_off():
                ser1 = serial.Serial('COM3',9600)
                speakm('okk turning off the led')  
                      
                ser1.write(b'0')
                # ser.close()
                
                
            def led_try():
                if 'on' in query:
                    led_on()
                elif 'off' in query:
                    led_off()
            try:

                led_try() 
            except Exception as noled:
                print(noled)
                speakm('there is no led connected')
                print('He said : There is no led connected')           

                

                
        elif 'generate a random number' in query or 'random number' in query:
            def bet():
                v = []
                v = query
                li = v.split(" ",100)
                for i in li:
                    if str(i).isnumeric():
                        l_l = i
                        lowerlimit = int(i)
                li.remove(l_l)
                for j in li:
                    if str(j).isnumeric():
                        upperlimit = int(j)
                lowerlimit,upperlimit = upperlimit, lowerlimit
                # print(lowerlimit,upperlimit)
                final = random.randint(lowerlimit, upperlimit)
                speakm(f'{final}')
                print(f'here is your random number {final}')

            try:

                bet()    
                
            except Exception as be:
                # print(be)
                 print('error')    
            def re():
                speakm('ok! here is the number')
                r_n = random.randint(0,10)
                speakm(r_n)
                print(r_n)
              
        elif query == "what do you know" or query == "your knowledge limit" or query == "knowledge limit":
            speakm('i am still filling my database and still learning')
            print("He said : I am still filling my database and still learning")
        elif 'who are you' in query:
            speakm('i am KSX') 
            print('He said : I am KSX') 
        elif 'minimise' in query or 'minimise this window' in query or 'minimize' in query:
            pyautogui.click(1785,12)  
            speakm('minimized')  
            print('He said : Minimized')
        elif 'photos' in query:
            speakm('opening photos folder')
            print('He said : Opening photos folder')
            try:
                os.startfile('D:\\photos')
            except Exception as ph:
                # print(ph)
                speakm('not found')
                print('He said : Not found')  
        elif 'followers' in query:
            speakm('ok checking the current amount of followers')
            print('He said : Ok! Checking the current amount of followers')
            try:

                driver = webdriver.Chrome()
                driver.get('https://instagram.com')
                time.sleep(2)

                # user_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys('kunalsurja')
                user_insta = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input'))).send_keys('kunalsurja')
                time.sleep(2)
                pas_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys('Kunalsen95%')
                time.sleep(1)
                log_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
                time.sleep(3)
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div[3]/button[2]'))).click()
                # no_insta = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
                time.sleep(0.5)
                me_insta = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img').click() 
                time.sleep(2)   
                v_insta = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/section/main/div/header/section/ul/li[2]/a'))).text
                # v_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').text
                v = v_insta.replace('followers', '')  
                driver.close()
                
                speakm(f'you have {v} followers in instagram')            
                print(f'He Said :  You have {v} followers in instagram') 
            except Exception as insta:
                # print(insta)
                speakm('sorry there was a problem it seems that its the internet problem but it could be anything. try again') 
                print('He said : problem')   
        elif 'last post' in query:
            def instag():
                try:
                    speakm('wait just let me see the current amount of likes')
                    print('Hs said : Wait')
                    driver = webdriver.Chrome()
                    driver.get('https://instagram.com')
                    # time.sleep(2)
                    us = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')))
                    us.send_keys('snappyeternals@gmail.com')
                    # user_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys('kunalsurja')
                    time.sleep(2)
                    pas_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys('KILLED WITH SHUTTER')
                    time.sleep(1)
                    log_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
                    time.sleep(5)
                    no_insta = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div[3]/button[2]'))).click()
                    # no_insta = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
                    time.sleep(0.5)
                    me_insta = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img').click() 
                    time.sleep(2)
                    # driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[2]').click()
                    pos = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[2]')))
                    pos.click()
                    # pyautogui.moveTo(165,815,0.2)
                    # pyautogui.click()
                    time.sleep(2)
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button'))).click()
                    # driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button').click()
                    time.sleep(2)
                    n = int(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button/span'))).text)
                    # n = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/h4/span').text
                    driver.close()
                    n = n + 1
                    speakm(f'your last post on instagram gets {n} likes')
                    print(f'He said : Your last post on instagram gets {n} likes')
                except Exception as ins:
                    # print(ins)
                    speakm("some internet problem occured. why don't you upgrade your network system!")
                    print('error')
            instag()            

        elif query == 'text file' or query == 'new text file' or query == 'create a new text file' or query == 'create new text file':

            def tex():
                speakm('what will be the name of the text file')
                k = input("what will be the name of the text file : ")
                t = open(k+".txt","w")
                engine.say('you want to write something?')
                engine.runAndWait()
                w = input('you want to write something(Y/N) : ')
                w = w.upper()
                if w == "Y":
                    speakm('Enter what you want to write in the text file')
                    
                    q = input('Enter what you want to write in the text file : ')
                    t.write(q)
                    speakm("text file created")
                    print("text file created")
                    
                elif w == "N":
                
                    t.close()
                else:
                    speakm('you are typing wrong values')
                    print('wrong value')

                    tex()
            
            
            tex()
            
                     

        elif 'add numbers' in query or 'sum' in query or 'add number' in query:
            def en():

                try:

                    speakm('Enter how many numbers you wana add')
                    v = int(input('Enter how many numbers you wana add : '))
                    speakm('enter the numbers respectively')
                    try:
                        def su():
                            v1 = 0
                            for i in range(v):
                                
                                b = int(input('Enter the number : '))
                                v1 = v1 + b
                            speakm(f'the answer is {v1}')    
                            print(f'He said : The answer is {v1}')    
                        su()        
                    except Exception as s:
                        # print(s)
                        speakm('just type a number')
                        print('just type a number')
                        su()        
                except Exception as m:
                    # print(m)
                    speakm('enter only number')
                    print('Enter only number') 
                    en()   
            en()        
        elif 'quadratic equation' in query:
            speakm('ok, all quadratic equations have a special form a x square  plus b x plus c') 
            print('All quadratic equations have a special from of ax^2 + bx +c')
            speakm('so i need to know the values of a, b and c')  
            print('So I need to know the values of a, b and c')
            def eq():
                speakm('tell me the value of a')
                eq_a = int(input('Enter the value of a = '))
                speakm('tell me the value of b')
                eq_b = int(input('Enter the value of b = '))
                speakm('tell me the value of c')
                eq_c = int(input('Enter the value of c = '))
                eq_d = (eq_b**2) - (4*eq_a*eq_c)
                x1 = (-eq_b + cmath.sqrt(eq_d)) / (2 * eq_a)
                x2 = (-eq_b - cmath.sqrt(eq_d)) / (2 * eq_a)
                speakm(f'here is the roots of the quadratic equation {x1} and {x2}')
                print(f'The roots are {x1} and {x2}')
            try:
                eq()
            except Exception as eq_error:
                # print(eq_error)
                speakm('error try again')
                print('try again')    
                eq()    
            
        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'drink anything' in query:
            speakm('nooo! mann i dont drink anything , i just drink electricity via the system')
            print('He said : nooo! mann i dont drink anything , i just drink electricity via the system')
        elif 'time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speakm(f"the time is {strTime}")
        elif 'exit' in query:
            # speakm('exiting program')
            # speakf('ksx going offline')
            
            # print('Exiting program')
            
            # print(start_time-end_time)
            # print(h1 - s)
            # exit()
            def exit1():

                speakm('exiting program') 
                playsound('D:\\assistant(ks)\\close.mp3')
                speakf('ksx going offline')
                
                e1 = time.time()
                e2 = e1 - s
                print(e2)
                ti = open('time','a')
                ti.write(f'The time duration : {e2}')
                ti.close()
                exit()  
            exit1()    
            
        else:
            speakm('it seems to new for me i will learn soon')
            
            print('my database is not enough')   
            im = open("new","a")
            im.write("new words = ")
            im.write(query+'\n')
            im.close()
            speakm(f"i will learn about {query}")
        def ex():

            speakm('Any other thing you have i can do?')   
        
            ans = input('Any other thing you have i can do(Y/N) : ')
            ans = ans.upper()
            if ans == "Y":
                com()
            elif ans == "N":
                def exit2():
                    speakm('exiting program') 
                    playsound('D:\\assistant(ks)\\close.mp3')
                    speakf('ksx going offline')
                    
                    e1 = time.time()
                    e2 = e1 - s
                    print(e2)
                    ti = open('time','a')
                    ti.write(f'The time duration : {e2}')
                    ti.close()
                    exit() 
                exit2()    
               
            else:
                speakm('enter right value')
                print('Enter right value')
                ex()    
        ex()        

    # elif 'open code' in query:
    #         codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    #         os.startfile(codePath)
# wishMe()



#--------------------------------------------------------------------------- Locking mechanism ----------------------------------------------------------------------------------------



def usert():
    
    
    speakf('enter your name and password')
    
    name = pyautogui.prompt('Enter your name', 'KSX')
    
    password = pyautogui.password('Enter the password', 'KSX','','*')
    if name == "kunal" and password == "kunal95":
        playsound('D:\\assistant(ks)\\start.mp3')
        speakf("ksx online")
        wishMe()

    
    
    else:
        playsound('D:\\assistant(ks)\\error1.mp3')
        speakf('you are typing wrong values')
        vid = cv2.VideoCapture(0)
        check, frame = vid.read()
        # time.sleep(1)
        vid.release()
        r = random.randint(1,200)
        # cv2.imshow('goctcha', frame)
        cv2.imwrite(f'D:\\assistant(ks)\\kalprint\\kalprint-{r}.jpg',frame)

        # cv2.waitKey(2)
        # cv2.destroyAllWindows
        pyautogui.alert('wrong values', 'KSX')
        
        
        print('wrong input')
        
         
        def ove():
            speakf('do you want to override?')
    
            ov = pyautogui.confirm('do you want to override')
            ov = ov.upper()   
            if ov == "OK":
                speakf('Enter the override command')
                speakf("Remember you will get only one chance to override so don't miss")
                
                print("Remember you will get only one chance to override so don't miss")
                op = pyautogui.password('Enter the override command')
                if op == "Kunalsen95%":
                        speakf(f'override system by {name}')
                        playsound('D:\\assistant(ks)\\start.mp3')
            
                        person = open("override.txt","w")
                        person.write(f'override system by {name}')
                        person.close()
                        print('system override')
                        wishMe()
                else:
                        speakf('override canceled')
            
                        print('override canceled')
                        exit()
                        
            elif ov == "CANCEL":
                speakf('good then try to remember the name and password')
        
                # print("good bye")
                # exit()   
                usert()
            else:
                speakf('enter right value')
                print('Enter right value')
                ove()
                # speakf('overwrite canceled')
        
                # print("cancel overwrite")
                # exit()
        ove()                 
usert()










#------------------------------------------------------------------------------- CREATED BY KUNAL SEN ------------------------------------------------------------------------------------------
