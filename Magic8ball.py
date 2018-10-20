'''

The Magic 8-Ball is a toy used for fortune-telling or seeking advice, developed in the 1950s and manufactured by Mattel.
The user asks a question to the large plastic ball, then turns it over to reveal a written answer which appears on the surface of the toy.

https://en.wikipedia.org/wiki/Magic_8-Ball
'''
from random import randint
print("Your magic 8 ball is here!")
question=input("Ask me something! What's on your mind\n")

answer=randint(1,21)




answerdict={'1':'It is certain.',
'2':'As I see it, yes.',
'3':'Reply hazy, try again',
'4':'Don\'t count on it.',
'5':' It is decidedly so.',
'6':'Most likely.',
'7':'Ask again later.',
'8':'My reply is no.',
'9':'Without a doubt.',
'10':'Outlook good.',
'11':'Better not tell you now.',
'12':'My sources say no.',
'13':'Yes - definitely.',
'14':'Yes',
'15':'Cannot predict now.',
'16':'Outlook not so good.',
'17':'You may rely on it.',
'18':'Signs point to yes.',
'19':'Concentrate and ask again.',
'20':'Very doubtful',
}

for k , val in answerdict.items():
    if int(k)==answer:
        print(val)
