from tkinter import *
U = ''
per = 0
personality = ''
# Personas
persona = ['Why do you keep pushing the no word 😂', 'You are a rebel who likes to try new things',
           'You are an adventurer who don\'t fear death', 'You have a courageous character', 'You don\'t follow the herd',
           'You like living but want to change your life', 'You are brave but don\'t like adventure',
           'You don\'t care about what people say about you', 'You never stop helping your friends',
           'You care about what people say too much', 'You have a huge potential',
           'You fear darkness', 'Cheater alarm!! You keep pressing the yes button 😂']
# Questions
Q = ['Q.1 Do you like beaches?', 'Q.2 Do you like chocolates?', 'Q.3 Do you go cycling', 'Q.4 DO you wake up early?',
     'Q.5 Do you go swimming?', 'Q.6 Do you watch the news?']

# index variable
ind = 0

question = Q[ind]


# Terminate program
def close():
    quit()


win = Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))

win.title(" InterQuiz by AdamUltra ")


# Reveal Personality
def know_personality():
    global personality, YourPersonality
    personality = persona[per]
    YourPersonality = Label(win, text=f"Your personality is {personality}", font='bold')
    YourPersonality.place(x=450, y=250)
    YourPersonality.update()


# Next Question
def next_q():
    global Question, ind, question, Input, per, entry
    Input = str(entry.get(1.0, "end-1c"))
    if Input == 'yes':
        per += 2
    elif Input == 'sometimes':
        per += 1
    elif Input == 'no':
        per += 0
    Question.destroy()
    ind += 1
    question = Q[ind]
    Question = Label(win, text=f'Question is {question}', font='bold')
    Question.place(x=350, y=150)
    Question.update()


# Buttons
QuitButton = Button(win, text="  Quit  ", command=close, bg="red", font="bold")
QuitButton.place(x=587, y=350)
PersonaButton = Button(win, text="Know Your Personality!!", command=know_personality, bg="blue")
PersonaButton.place(x=550, y=300)
NextQuestion = Button(win, text="Next Question!!", command=next_q, bg="blue")
NextQuestion.place(x=700, y=200)

# Labels
YourPersonality = Label(win, text=f"Your personality is {personality}", font='bold')
YourPersonality.place(x=450, y=250)
Intro = Label(win, text="Hi, let's answer some questions to know your personality \n "
                        "But please don't take it seriously, it's just for fun 😀", font='bold')
Intro.pack(side='top')

# Questions
Question = Label(win, text=f'Question is {question}', font='bold')
Question.place(x=350, y=150)

# textboxes
entry = Text(master=win, height=1, width=10)
entry.place(x=700, y=153)
win.mainloop()
