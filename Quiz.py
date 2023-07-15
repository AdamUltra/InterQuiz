print('Hi!!')
print('Let\'s do a quiz to know your personality!!')
print('Answer with (yes, no, sometimes)')
per = 0
persona = ['Why do you keep pushing the no word 😂', 'You are a rebel and likes to try new things',
           'You are an adventurer and don\'t fear death', 'You have a courageous character', ]
Q = ('Do you like beaches?', 'Do you like chocolates?', 'Do you go cycling', 'DO you wake up early?',
     'Do you go swimming?', 'Do you have a crush 😉', )
for i in Q:
    UInp = str(input(i))
    if UInp == 'yes':
        per += 2
    elif UInp == 'no':
        per += 0
    elif UInp == 'sometimes':
        per += 1
print(persona[per])
