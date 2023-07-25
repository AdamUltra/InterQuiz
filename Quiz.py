print('Hi!!')
print('Let\'s do a quiz to know your personality!!')
print('Answer with (yes, no, sometimes)')
per = 0
persona = ['Why do you keep pushing the no word 😂', 'You are a rebel who likes to try new things',
           'You are an adventurer who don\'t fear death', 'You have a courageous character', 'You don\'t follow the herd',
           'You like living but want to change your life', 'You are brave but don\'t like adventure',
           'You don\'t care about what people say about you', 'You never stop helping your friends',
           'You care about what people say too much', 'You have a huge potential',
           'You fear darkness', 'Cheater alarm!! You keep pressing the yes button 😂']


def ask():
    global per
    per = 0
    Q = ('Do you like beaches?', 'Do you like chocolates?', 'Do you go cycling', 'DO you wake up early?',
         'Do you go swimming?', 'Do you have a crush 😉',)
    for i in Q:
        UInp = (input(i))
        if UInp == 'yes':
            per += 2
        elif UInp == 'no':
            per += 0
        else:
            per += 1
    print(persona[per])
    UInp = input('Do you want to play again?')
    if UInp == 'yes':
        ask()
    else:
        quit()


ask()
