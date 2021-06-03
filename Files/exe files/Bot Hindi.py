import pyttsx3
import time
from datetime import datetime
from datetime import date

# Time
def Yourtime():
    localtime= time.asctime(time.localtime(time.time()))
    print('Your Current Time',localtime)
    return localtime


def Printday(today):
    wd = date.weekday(today)
    days = ['monday','tuesday','wednesday','thurday','friday','saturday','sunday']
    return days[wd]

today = date.today()
now = datetime.now()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Jarvis speaking ....")    
fline = "मैं जार्विस हूं और मैं शीबेन बीओटी हूं"
Sline = "आज गुरुवार है",
Tline = "हमारे पास आपके चयन के लिए कई विकल्प हैं। पहले कृपया एक वाक्य जारी रखने के लिए इनपुट."

speak(fline)
speak(Sline)
speak(Tline)


mystr = input('Please input Sentence :')

def point6():

    for i in mystr:
        if i==' ':
            print('*')
        else:
            print(i)



while(True):

    print("What Do You Want?")
    print(' 1.Lenght')
    print(' 2.Count of Word')
    print(' 3.Split by Word')
    print(' 4.LowerCase')
    print(' 5.UpperCase')
    print(' 6.Replace Space By *')
    print(' 7.All Word Frist Letter Capital')
    print(' 8.Your Current time')
    print(' 9.View Your Sentence')  
    print(' 10.Print Today Date')
    print(' 11.Time')
    print(' 12.Year')
    print(' 13.DateTime')
    print(' 14.Month')
    print()
    speak("कृपया अपनी पसंद का चयन करें। आपके पास 14 विकल्प हैं.")

    myask = input('Please Enter You Choice  :')
    spl = mystr.split()
    if myask == '1':
        print(len(mystr))
    elif myask == '2':
        print(len(spl))
    elif myask == '3':
        for x in spl:
            print(x)
    elif myask == '4':
        print(mystr.lower())
    elif myask == '5':
        print(mystr.upper())
    elif myask == '6':
        point6()
    elif myask == '7':
        for y in spl:
            z = y.capitalize()
            print(z,end=" ")
    elif myask == '8':
        print(Yourtime.strftime('%d %H %M')) 
    elif myask == '9':
        print(mystr) 
    elif myask == '10':
        print(Printday(today))
    elif myask == '11':
        t = datetime.time(datetime.now())
        print('Today date is',t)
    elif myask == '12':
        print( now.strftime("%Y"))
    elif myask == '13':
        print ("today date is",now.strftime('%A,%d,%B') )
    elif myask == '14':
        print ('Current Month Is',now.strftime('%B'))




    else:
        speak("गलत इनपुट प्रदान किया गया। कृपया केवल 1 से 7 के बीच विकल्पों का चयन करें.")
        print("incorrect input...")

    myask2 = ""

    speak("प्रेस सी जारी रखने के लिए और प्रेस क्यू छोड़ने के लिए..")
    print('To continue press c and to quit press q  :')
    
    while (myask2 != 'q' and myask2 !='c'):
        myask2 = input()
        if myask2 == 'q':
            speak("अलविदा! आपका दिन अच्छा हो.")
            exit()
        elif myask2 == 'c':
            continue
    # input("Press enter to close program")