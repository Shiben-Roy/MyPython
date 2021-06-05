print('Preparing System')
import pyttsx3

import speech_recognition as SR
import random
import time

# Audio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    userinput = ""
comp_input = ''

# Rock Paper Scissor
def rockpaperscissor():
    while (True):
        countinue1 = ''
        print(" Please enter [R]ock or  [P]aper or [S]cissor")
        userinput = input('User Input : ')
        userinput = userinput.capitalize()
        mylist = ['R','P','S']

        if userinput not in mylist:
            print('Incorrect Input, Please enter [R]ock or  [P]aper or [S]cissor   ...........')
        else:
            comp_input = random.choice(mylist)
            print(f"user input is {userinput} and Computer input is {comp_input}")

        print()
        print()

        # Paper
        if  userinput == 'P' and comp_input == 'R':
            print('User Win!!!')
        elif userinput == 'P' and comp_input == 'S':
            print('Computer Wins')
        elif userinput == 'P' and comp_input == 'P':
            print('Draw!!')
        # Rock       
        elif userinput == 'R' and comp_input == 'P':
            print('Computer Win!!!')
        elif userinput == 'R' and comp_input == 'R':
            print('Draw!!!')
        elif userinput == 'R' and comp_input == 'S':
            print('User Win !!!')      
        # Scissor  
        elif userinput == 'S' and comp_input == 'R':
            print('Computer Win !!!')
        elif userinput == 'S' and comp_input == 'S':
            print('Draw!!!')
        elif userinput == 'S' and comp_input == 'P':
            print('User Win !!!') 
        
        print()
        print('To Countinue Type - C -  And to Quit Type - Q - .......................')          
        
        while (countinue1 != 'Q' and countinue1 != 'C'):
            countinue1 = input()
            countinue1 = countinue1.capitalize()
            if countinue1 == 'Q': 
                exit()
            elif countinue1 == 'C':
                continue

# Starting
speak("Hi, I am Sheeben's Bot!")
speak('Please, Enter your name')
print('Names In Server')
print('Srijan')
Name1 = input('Name? ')
Name1 = Name1.capitalize()
if Name1 == 'Srijan':
    print()
    print('Welcome Srijan')
speak('Welcome Sreejon')
time.sleep(0.5)
speak('Haappy birthday Sreejon!')
print('Happy Birthday Srijan!')
while (True):
    print()
    print('We Have Many Option For You')
    print('1.Do you know what is the meanig of your Name')
    print(' 2.Play a game, Rock Paper Scissor ')
    print(' 3.Funny Riddle')
    print(' 4.Birthday Poem for you')
    ask1 = input('Select Your Choice')

    if ask1 == '3':
        print('1. riddle')
        print('2. ridlle')
        rid  = input('Enter Your Riddle')
        
    elif ask1 == '2':
        rockpaperscissor()
    elif ask1 == '4':
        print('Happy Birthday to my very best friend.')    
        print('Your special day has come by again.')
        print('We had so much fun last time around.')
        time.sleep(1)
        print('Each year June 7th is a wonderful day')
        print('As we march forth in our own fun way.')
        print('Just hanging around and laughing a lot')
        print('It is truly amazing what we have got.')
    elif ask1 == '4':
        print("Your Name Meaning Is 'Creation' ")
    print('To Countinue Type - C -  And to Quit Type - Q - .......................3')
    
    myask2 = ''
    while (myask2 != 'q' and myask2 !='c'):
        
        myask2 = input()
        if myask2 == 'q':
            speak("Good Bye! Have a good day.")
            exit()
        elif myask2 == 'c':
            continue        