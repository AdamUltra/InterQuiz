from tkinter import *
import time
U = ''
persona = ['Why do you keep pushing the no word 😂', 'You are a rebel who likes to try new things',
           'You are an adventurer who don\'t fear death', 'You have a courageous character', 'You don\'t follow the herd',
           'You like living but want to change your life', 'You are brave but don\'t like adventure',
           'You don\'t care about what people say about you', 'You never stop helping your friends',
           'You care about what people say too much', 'You have a huge potential',
           'You fear darkness', 'Cheater alarm!! You keep pressing the yes button 😂']


def entry():
    global Answer
    Answer = Q_entry.get()


def Quit():
    quit()


def getinput():
    textArea.insert(END, persona[per])


def ask():
    global U
    global per
    per = 0
    Q = ('Do you like beaches?', 'Do you like chocolates?', 'Do you go cycling', 'DO you wake up early?',
         'Do you go swimming?', 'Do you have a crush 😉',)
    entry()
    for i in Q:
        U = i
        if Answer == 'yes':
            per += 2
        elif Answer == 'no':
            per += 0
        else:
            per += 1
    # print(persona[per])


window = Tk()
window.geometry("850x850")
window.title(" InterQuiz by AdamUltra ")
Question = Label(text="Question: {UInp}".format(UInp=U))
Question.grid(column=0, row=1)
Q_entry = Entry()
Q_entry.grid(column=1, row=1)
Persona = Label(text="Your Personality!!")
Persona.grid(column=1, row=2)
textArea = Text(master=window, height=10, width=25)
textArea.grid(column=1, row=6)
button = Button(window, text="Know personality", command=getinput, bg="pink")
button.grid(column=3, row=5)
button2 = Button(window, text="Quit", command=Quit, bg="red")
button2.grid(column=3, row=4)
answer = "Hi, let's answer some questions to know your personality \n But please don't take it seriously, it's just for fun 😀"
textArea.insert(END, answer)
ask()


window.mainloop()
