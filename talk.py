import speech_recognition as sr

#from gtts import gTTS 
import pyttsx3  
import sys
# import Os module to start the audio file
import os 

engine = pyttsx3.init()
    



def turn():
    t = True
    while t:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            voices = engine.getProperty("voices")       
            engine.setProperty("voice",voices[0].id)
            engine.say('Hi! what can I do for you')
            engine.runAndWait()
            print("Hi! what can I do for you :")
            
            
            audio = r.listen(source)
        text = r.recognize_google(audio)

        print(f"You said : {text}")
        voices = engine.getProperty("voices")       
        engine.setProperty("voice",voices[0].id)
        if text == 'who are you' or text == 'what is your name':
            print('He said : I am an assistant for KUNAL SEN')
            
        elif text == 'open notepad' or text == 'start notepad' or text == 'notepad':
            engine.say('opening notepad')
            engine.runAndWait()
            print('He said : opening notepad')
            os.system("start notepad")
            
            #  print('anything i can do?')
            #  audio = r.listen(source)
            #  text = r.recognize_google(audio)
            #  turn()
        elif text == "where are you from" or text == "where do you live" or text == "where is your home":
            engine.say('this is my home')
            print('He said : This is my home')
            engine.runAndWait()    
        elif text == 'how are you':
            print("He said : I'm good. what about you?")
             
        elif text == 'open Chrome' or text == 'start Chrome' or text == 'Chrome':
            engine.say('opening chrome')
            print("He said : Opening Chrome")
            engine.runAndWait()
            os.system("start chrome") 
        elif text == "what do you know" or text == "your knowledge limit" or text == "knowledge limit":
            engine.say('i am still filling my database and still learning')
            print("He said : I am still filling my database and still learning")
            engine.runAndWait()

        elif text == 'crate text file' or text == 'text' or text == 'text file' or text == 'new text' or text == 'new text file':

            
            
            engine.say('what will be the name of the text file')
            engine.runAndWait()
            k = input("what will be the name of the text file : ")
            t = open(k+".txt","w")
            engine.say('you want to write something?')
            engine.runAndWait()
            w = input('you want to write something(Y/N) : ')
            w = w.upper()
            if w == "Y":
                engine.say('Enter what you want to write in the text file')
                engine.runAndWait()
                q = input('Enter what you want to write in the text file : ')
                t.write(q)
                engine.say("text file created")
                print("text file created")
                engine.runAndWait()
            elif w == "N":
                
                t.close()
            else:
                print('wrong value')
                exit()

            
            
            

        else:
            engine.say('it seems to new for me i will learn soon')
            engine.runAndWait()
            print('my database is not enough')   
            im = open("new","w")
            im.write("new words = ")
            im.write(text+",")
            im.close()
        engine.say('Any other thing you have i can do?')   
        engine.runAndWait() 
        ans = input('Any other thing you have i can do(Y/N) : ')
        ans = ans.upper()
        if ans == "Y":
            text = r.recognize_google(audio)
            turn()
        else:
            exit()
            

          
def vi():
    # engine.say("speak again : ")
    # print("Speak again!")
    # engine.runAndWait()
    # lp()
    v = input('Speak again(Y/N): ')
    v = v.upper()
    if (v == "Y"):
        
        lp()
        
           
   
            
           
    elif(v == "N"):
        print('good day')
        exit()
            
    else:
        print('wrong value')
        vi()

  

def lp():
    try:

        turn()
        
            

    except:
        engine.say("Sorry could not recognize what you said")

        print("Sorry could not recognize what you said")
        engine.runAndWait()
        vi()
        #exit()
        # else:
        #     turn()  
    
def usert():
    
    engine.setProperty("rate",130)
    voices = engine.getProperty("voices")       
    engine.setProperty("voice",voices[1].id)
    engine.say('enter your name and password')
    engine.runAndWait()
    name = input('enter your name : ')
    password = input('enter the password : ')
    if name == "kunal" and password == "kunal95":
        voices = engine.getProperty("voices")       
        engine.setProperty("voice",voices[1].id)
        engine.say("assistant online")
        lp()

    
    
    else:
        engine.say('you are typing wrong values')
        engine.runAndWait()
        print('wrong input')
        
    engine.say('do you want to overwrite?')
    engine.runAndWait()
    ov = input('do you want to overwrite(Y/N)?')
    ov = ov.upper()    
    if ov == "Y":
        engine.say('Enter the overwrite command')
        engine.say("Remember you will get only one chance to overwrite so don't miss")
        engine.runAndWait()
        print("Remember you will get only one chance to overwrite so don't miss")
        op = input('Enter the overwrite command : ')
        if op == "Kunalsen95%":
            engine.say(f'overwrite system by {name}')
            engine.runAndWait()
            person = open("overwrite","w")
            person.write(f'overwrite system by {name}')
            person.close()
            print('system overwrite')
            lp()
        else:
            engine.say('overwrite canceled')
            engine.runAndWait()
            print('overwrite canceled')
            exit()
    elif ov == "N":
        engine.say('good then try to remember the name and password')
        engine.runAndWait()
        # print("good bye")
        # exit()   
        usert()
    else:
        engine.say('overwrite canceled')
        engine.runAndWait()
        print("cancel overwrite")
        exit()         
usert()
def bh():
    exit()

                   

       