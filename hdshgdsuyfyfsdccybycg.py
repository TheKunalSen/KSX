import pyttsx3  
engine = pyttsx3.init()
voices = engine.getProperty('voices')



def speakf(audio):
    engine.setProperty("rate",130)
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
def speakm(audio):
    engine.setProperty("rate",180)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def learn():
    with open('info.txt','r+') as f:
        f1 = f.read()
        speakf(f'she said that{f1}')
def wr():
    with open('info.txt','a') as g:
        q = input('enter what you want to write about her : ')
        
        f2 = g.write(q)  
def v():

    d = input('you want to write somthing')
    d = d.upper()
    if d == 'YES':
        wr()
    elif d == 'NO':
        exit()
    else:
        speakf('enter yes or no')
        v()                
def c():
    speakf('enter what you want to search')
    r = input('enter what you want to search')
    r = r.lower()
    if r == 'raima':
        learn()
        v()
    else:
        print('none') 
        exit()
c()     
     
