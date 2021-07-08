import pyautogui
import time
from selenium import webdriver
import pyttsx3
import math
from playsound import playsound
import os
# import pyowm
import requests
import speech_recognition as sr
from pprint import pprint
import json
import random
import string
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image, ImageGrab # pip install pillow
import cv2
import matplotlib.pyplot as plt
import numpy as np
import cmath
import matplotlib.pyplot as plt 
# import serial
# import plyer
# from win10toast import ToastNotifier
from bs4 import BeautifulSoup



# a = int(input("Enter first number : "))
# b = int(input("Enter first number : "))
# temp = a
# a = b
# b = temp
# print(a,b)
# list1 = []
# list2 = []
# n = int(input("enter the number of elements : "))
# for i in range(n):
#     element = int(input())
#     list1.append(element)
# for j in list1:
#     if j not in list2:
#          list2.append(j)
# print(list2)

# seq = {50,40,6,7,8,5}
# i = int(input("Enter the number"))
# def search(a,b):
#     if b in a:
#        return True
#     else:
#        return False   
# w=search(seq,i)
# print(w)
driver = webdriver.Chrome()
driver.get('https://youtube.com')
driver.maximize_window()
# state = ['west bengal','gujarat']
# v = input('skjbckhsdgcjhsdv: ')
# v1 = v.split(" ",100)
# print(v1)

# for i in state:
#     for j in v1:
#         if j in i:
#            n = str(i)
#         elif 'bengal' in j:
#             n = 'west bengal'
#         elif 'west' in j:
#             n = 'west bengal'         
#         else:
#             n = 'not found'
# print(n)





















# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# def speakf(audio):
#     engine.setProperty("rate",120)
#     engine.setProperty('voice', voices[1].id)
#     engine.say(audio)
#     engine.runAndWait()
# speakf("Akaash bejj, The writer of this community")   


# rum = requests.get("https://www.mohfw.gov.in/")
# rum1=rum.text
# # print(rum1)
# soup = BeautifulSoup(rum1, 'html.parser')
# # print(soup)
# tr_data = ""
# for table in soup.find_all('tbody')[0].find_all('tr'):
#     tr_data += table.get_text()
# tr_data = tr_data[1:]    
# items = tr_data.split("\n\n")
# state = input('hjvjvfjv : ')
# state1 = state.split()
# # print(state1)
# # print(len(state1))
# n1 = int(len(state1))
# for item in items[0:35]:
#     corona_list = item.split('\n')
#     u1 = 0
#     if corona_list[1] in state1[0:n1]:
#         # print(corona_list[2])
#         u1 = u1 + 1
#         # print(state1[u1])
# newstate = string.capwords(state)
# # print(newstate)        
# for item in items[0:35]:
#     corona_list = item.split('\n')
#     if corona_list[1] in newstate:
#        act=corona_list[2]
#         # print(newstate)
#     else:
#         act='not found'    
         
# print(act)






# a = 1
# b = -7
# c = 12









# 100 linearly spaced numbers
# x = np.linspace(-10,10,200)

# the function, which is y = e^x here
# y = a * (x**2) + (b * x) + c
# fig = plt.figure()

# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# plt.plot(x,y)
# plt.show()

# setting the axes at the centre


# plot the function
# plt.plot(x,y, 'y', label='y=e^x')
# plt.legend(loc='upper left')

# show the plot
# plt.show()
# x1=np.linspace(-3,6,10,endpoint=False)
# y1=np.sin(90)
# plt.plot(x1,y1)
# plt.show()
# print(y1)
# print(x1)
# print('the quadratic equation neede three value a, b, c')
# a = int(input('tell me the value of a'))
# b = int(input('tell me the value of b'))
# c = int(input('tell me the value of c'))
# d = (b**2) - (4*a*c)
# x1 = (-b + cmath.sqrt(d)) / (2 * a)
# x2 = (-b - cmath.sqrt(d)) / (2 * a)
# x_plot = [x1, x2, 0]
# y_plot = [0,0,c]
# plt.plot(x_plot,y_plot)
# plt.show()
# print(x1,x2)
# np.linspace(x1,x2,20)
# plt.plot(x1,x2)
# plt.show()
driver = webdriver.Chrome()
# driver.get('https://www.facebook.com/')
# m=[]
# b=[]
# m=input()
# y=m.split(" ", 100)
# print(y)

# for i in y:
#     if str(i).isnumeric():
#         a = i
#         k = int(i)
# y.remove(a)
# for j in y:
#     if str(j).isnumeric():
#         c = int(j)
# k,c=c,k
# print(k,c)
# print(random.randint(k,c))
# driver.get('https://www.youtube.com/watch?v=YXlRTFhfE_4')
# driver = webdriver.Chrome()
# driver.get('https://www.facebook.com/')
# driver.maximize_window()
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input').send_keys('9475622804')
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input').send_keys('Kunalsen95%')
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input').click()
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/a/div[1]/div'))).click()
# n = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/a[3]/div[1]').text()
# print(n)
# m_x= np.linspace(-1,1,5)
# m_y = np.sin(m_x)
# plt.plot(m_x,m_y)
# plt.show()

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
# ser = serial.Serial('COM3', 9600)

# def led_on_off():
#     user_input = input("\n Type on / off / quit : ")
#     if user_input =="on":
#         print("LED is on...")
#         time.sleep(0.1) 
#         ser.write(b'H')
#         # ser.close()

#         # time.sleep(2)
#         led_on_off()
#     elif user_input =="off":
#         print("LED is off...")
#         time.sleep(0.1)
#         ser.write(b'L')
#         # ser.close()
#         led_on_off()
#     elif user_input =="quit" or user_input == "q":
#         print("Program Exiting")
#         time.sleep(0.1)
#         ser.write(b'L')
#         ser.close()
#     else:
#         print("Invalid input. Type on / off / quit.")
#         led_on_off()

# time.sleep(2) # wait for the serial connection to initialize

# led_on_off()

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         # speakf('speak sir')
#         print("Listening...")
#         r.pause_threshold = 1.2
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You said: {query}")
#         return query

#     except Exception as e:
#         # print(e)    
#         # speakm("Sorry could not recognize what you said")
#         print("Sorry could not recognize what you said")  
#         return ''
        
# takeCommand() 
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')



 
# img = numpy.zeros((512,1112,3), numpy.uint8)
# img = cv2.line(img,(100,100),(100,300),(255,200,0),5)
# cv2.imshow('fghdhk',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.mp4',fourcc, 60.0, (640,480))
# while(True):
    
#     ret, frame = cap.read()

    
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         out.write(frame)
#         break


# cap.release()
# cv2.destroyAllWindows()
# b = cv2.imread('xm.png',0)
# cv2.imshow('image',b)
# # v = cv2.waitKey(0) & 0xFF
# # print(v)
# # b = vq
# def bh():
#     v = cv2.waitKey(0) & 0xFF
#     print(v)
#     # b = v
#     if v == ord('e'):
#         cv2.destroyAllWindows()
#     elif v == ord('s'):
#         cv2.imwrite('xm2.jpg',b)    
#     else:   
#         print('try again')
        
#         bh()
# bh()        
# print(random.randint(1,10))
# vid = cv2.VideoCapture(0)
# check, frame = vid.read()
# time.sleep(3)
# vid.release()

# cv2.imshow('goctcha', frame)
# cv2.imwrite('l.jpg',frame)

# cv2.waitKey(2000)
# cv2.destroyAllWindows
# img = cv2.imread('xm.png')
# from numpy import asarray
# n = 'jl.py'
# pyautogui.hotkey('ctrl','n')
# pyautogui.hotkey('ctrl','s')
# time.sleep(1)
# pyautogui.typewrite(n)
# time.sleep(2)
# pyautogui.keyDown('enter')
# time.sleep(1)
# pyautogui.write("print('hello world')")
# pyautogui.hotkey('ctrl','s')
# pyautogui.click(12,1057)
# pyautogui.typewrite('cmd')
# time.sleep(1)
# pyautogui.click(77,538) 
# time.sleep(1)
# pyautogui.typewrite("D:")
# pyautogui.keyDown('enter')
# pyautogui.typewrite('cd assistant(ks)')
# pyautogui.keyDown('enter')
# time.sleep(0.4)
# pyautogui.typewrite(n)
# pyautogui.keyDown('enter')
# pyautogui.hotkey('ctrl','f5')


# def hit(key):
#     pyautogui.keyDown(key)
#     return

# def isCollide(data):
#     for i in range(255, 505):
#         for j in range(520, 650):
#             if data[i, j] > 80 and data[i, j]<255:
                
#                 hit("up")
#                 return
#     # Draw the rectangle for birds
#     for i in range(300, 415):
#         for j in range(410, 563):
#             if data[i, j] > 80 and data[i, j] < 255:
#                 hit("down")
#                 return

    
#     return


# driver = webdriver.Chrome()
# driver.get('chrome://dino')
# driver.maximize_window()
# print("Hey.. Dino game about to start in 3 seconds")
# time.sleep(1)
# hit('up') 
# # time.sleep(2)

# while True:
#     image = ImageGrab.grab().convert('L')  
#     data = image.load()
#     try:

#         isCollide(data)
        
#     except Exception as e:
#         print(e)
#         print('over')
#         v = input('agin?')
#         if v == 'y':
#             driver.find_element_by_xpath('/html/body/div[1]/div[4]/canvas').click()
#         else:
#             exit()    
    # image.show()
      
# print(asarray(image))

# Draw the rectangle for cactus
    # for i in range(255, 505):
    #     for j in range(560, 650):
    #         data[i, j] = 0

    # # Draw the rectangle for birds
    # for i in range(250, 300):
    #     for j in range(410, 563):
    #         data[i, j] = 171

    # image.show()
    # break

# driver = webdriver.Chrome()
# driver.get('https://instagram.com')
# time.sleep(2)

# user_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys('kunalsurja')
# time.sleep(2)
# pas_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys('Kunalsen95%')
# time.sleep(1)
# log_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
# time.sleep(3)
# no_insta = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
# time.sleep(0.5)
# me_insta = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img').click() 
# time.sleep(2)
# pyautogui.moveTo(165,815,0.2)
# pyautogui.click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button').click()
# time.sleep(2)
# n = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/h4/span').text
# print(n)


# driver = webdriver.Chrome()
# driver.get('https://facebook.com')
# num = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input').send_keys('9475622804')
# passd = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input').send_keys('Kunalsen95%')
# button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input').click()  
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div[1]/span/div/div[1]/img').click()
# time.sleep(5)
# driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span').click()
# time.sleep(5)
# # driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.5)")
# # time.sleep(2)
# var = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[2]/div/div/div[1]/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/a[3]/div[1]/span/span/span')
# # b = driver.find_element_by_xpath('')

# # print(b.text)
# driver = webdriver.Chrome()
# driver.get('https://instagram.com')
# time.sleep(2)

# user_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys('kunalsurja')
# time.sleep(2)
# pas_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys('Kunalsen95%')
# time.sleep(1)
# log_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
# time.sleep(3)
# no_insta = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
# time.sleep(0.5)
# me_insta = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img').click() 
# time.sleep(2)   
# v_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').text
# v = v_insta.replace('followers', '')

# print(v)

# b = str(input('gfyefcerk'))
# b = b.lower()
# if 'ms word' in b:
#     try:

#         def op():

            
#             print('Opening MS-Office')
#             os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk')
#         def op1():
#             def w():
#                 v = input('blank or post : ')
#                 v = v.lower()
#                 if 'blank' in v:
#                     x = 651
#                     y = 284
#                     os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk')
#                     time.sleep(3)
#                     pyautogui.click(17,19)
#                     # print(x,y)
#                     time.sleep(0.3)
#                     pyautogui.click(48,66)
#                     time.sleep(0.5)
#                     pyautogui.click(x,y)
#                     pyautogui.click(1389,928)
#                     print('created')
#                     # pyautogui.click(651,284)
#                 elif 'post' in v or 'blog' in v:
#                     x = 755
#                     y = 288
#                     os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk')
#                     time.sleep(3)
#                     pyautogui.click(17,19)
#                     # print(x,y)
#                     time.sleep(0.3)
#                     pyautogui.click(48,66)
#                     time.sleep(0.5)
#                     pyautogui.click(x,y)
#                     pyautogui.click(1389,928)
#                     print('created')
#                     # pyautogui.click(755,288) 
#                 else:
#                     print('just say blank or post :')    
#                     w()
#             w()        
           
            

            
            
            


#         if 'new file' in b or 'new' in b:
#             op1()
#         else:
#             op()        
#     except Exception as e:
#         print(e)
#         print('error')        
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# print(datetime.datetime.now().month)

# def speakf(audio):
#     engine.setProperty("rate",127)
#     engine.setProperty('voice', voices[1].id)
#     engine.say(audio)
#     engine.runAndWait()
# city = input('enter the city : ')

# url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=0dfd0858683905639ed72d2af8ffebff'.format(city)
# res = requests.get(url)

# data = res.json()

# tempmax = data['main']['temp_max']
# tempmin = data['main']['temp_min']
# humidity = data['main']['humidity']
# tempmax = tempmax - 273
# tempmin = tempmin - 273
# t = round(tempmax)
# t1 = round(tempmin)
# wind = data['wind']['speed']
# print(f'the wind speed is {wind}')
# print(f'the humidity level is {humidity}')
# if t == t1:
#     print(f'the avg is{t}')
# else:
#     print(f'{t1} to {t}')

# pprint(data)
# pprint(datao)
# speakf(data)
# owm = pyowm.OWM('0dfd0858683905639ed72d2af8ffebff')

# location = owm.weather_at_place('delhi')
# weather = location.get_weather()
# print(weather)
# v = time.time()
# print(v)
# k = os.startfile('d:\\photos')
# time.sleep(2)

# playsound('start.mp3')
# playsound('close.mp3')
# import sys
# from pygame import mixer
# import winsound
# winsound.PlaySound("k" , winsound.SND_FILENAME)
# mixer.init()
# mixer.music.load(r"D:\assistant(ks)\k.mp3")
# mixer.music.play()
# v = int(input('kjvbfvksbvdf : '))

# v1 = 0
# for i in range(v):
#     b = int(input('kjbdk : '))
#     v1 = v1 + b
    
# print(v1)    
    
# p = int(input('kuugdhf'))
# b = math.factorial(p)
# print(b)
# b = int(input('How many numbers do you want to add'))
   
# while b:
    

#     b1 = int(input('enter the no = '))
    
# b = int(input('jvffhd'))
# print(b + 5)
# driver = webdriver.Chrome()
# driver.get('https://www.nasa.gov/')
# pyautogui.moveTo(310,1073,0.5)
# pyautogui.click()
# pyautogui.moveTo(1908,1)
# pyautogui.click()
# pyautogui.moveTo(12,1057,1)
# pyautogui.click()
# pyautogui.typewrite('dolby audio')
# time.sleep(2)
# pyautogui.moveTo(77,538,1)  
# pyautogui.click()      
# pyautogui.moveTo(22,1057,5)
# pyautogui.click()
# pyautogui.typewrite('this pc')
# time.sleep(1)
# pyautogui.click(77,538)
# time.sleep(1)
# # pyautogui.moveTo(1764,155)
# pyautogui.moveTo(529,382,0.5) 
# pyautogui.doubleClick()
# pyautogui.click(1764,155)
# pyautogui.typewrite('gndjbkd')
# pyautogui.moveTo(12,1057,0.7)
# pyautogui.click()
# time.sleep(0.7)
# pyautogui.typewrite('paint')
# time.sleep(1)
# pyautogui.moveTo(77,538,0.7) 
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(322,400,1)
# pyautogui.doubleClick()
# pyautogui.dragTo(322,600,1)
# pyautogui.dragTo(322,500,1)
# pyautogui.dragRel(500,600,1)
# pyautogui.dragTo(322,500,1)
# pyautogui.dragRel(100,-100,1)


 
# pyautogui.click()
# distance = 300
 
 
# while distance > 0:
#     pyautogui.dragRel(distance, 0,) # move right
#     distance = distance - 2
#     pyautogui.dragRel(0, distance,) # move down
 
#     pyautogui.dragRel(-distance, 0,) #move left
#     distance = distance - 2
 
#     pyautogui.dragRel(0, -distance,) #move up
# k = pyautogui.confirm('dfbb')
# print(k)
# k = pyautogui.locateAllOnScreen('xm.png')
# # l = pyautogui.center(k)
# pyautogui.screenshot()
# d = list(k)
# pyautogui.moveTo(k[0],k[1])
# print(pyautogui.position())
# c = time.time()
# print(c - v)
# pyautogui.moveTo(12,1550,2)
# pyautogui.moveTo(120,1590,2)
# pyautogui.moveTo(1,1540,2)
# pyautogui.moveTo(400,1540,2)
# pyautogui.moveTo(12,1540,2)
# pyautogui.moveTo(250,1540,2)
# pyautogui.moveTo(650,1540,2)
# pyautogui.moveTo(21,1540,2)
# pyautogui.moveTo(66,1540,2)
# pyautogui.moveTo(3,1540,2)
# pyautogui.moveTo(12,1540,2)
# pyautogui.click(12,1057)
# pyautogui.typewrite('camera')
# time.sleep(2)
# pyautogui.click(77,538)
# driver = webdriver.Chrome()
# time.sleep(5)
# pyautogui.click(542,68)
# pyautogui.typewrite('anything')
# pyautogui.typewrite(['enter'])
# pyautogui.click(1605,53)

# pyautogui.typewrite('kunal')anything

# pyautogui.typewrite(['enter'])
# time.sleep(2)
# pyautogui.doubleClick(43,543)
# time.sleep(2)
# pyautogui.doubleClick(780,678)
# time.sleep(2)

# pyautogui.click(1605,53)
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.hotkey('win', 'g')
