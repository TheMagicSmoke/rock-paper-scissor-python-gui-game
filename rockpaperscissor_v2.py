from tkinter import *
from tkinter.font import *
from PIL import ImageTk,Image
import random,time

game_list = ['rock','paper','scissor']
score = [0,0] #pc,user

app = Tk()
app.geometry("700x500+300+100")
app.title('Rock  ,  Paper  ,  Scissor   Game  !!   Created   by   @Kaustav')

pcImage = Image.open('Images/pc_image.jpg')
pcImage = pcImage.resize((150,150))
pcImageObject = ImageTk.PhotoImage(pcImage)

userImage = Image.open('Images/user_image.jpg')
userImage = userImage.resize((150,150))
userImageObject = ImageTk.PhotoImage(userImage)

pcCel = Image.open('Images/dab_left.png')
pcCel = pcCel.resize((100,100))
pcCelObject = ImageTk.PhotoImage(pcCel)

userCel = Image.open('Images/dab.png')
userCel = userCel.resize((100,100))
userCelObject = ImageTk.PhotoImage(userCel)

tie = Image.open('Images/tie.png')
tie = tie.resize((100,100))
tieObject = ImageTk.PhotoImage(tie)


ruleString = ''' 1. Player vs Computer. First to reach 5 points wins. 2. Basic rock,paper,scissor rules apply, duh!
 3. Pc avatar to the left and User to the right.  4. Follow notepad file to paste your own avatar. Enjoy !!  '''

msgFont = Font(size=10,weight='bold')

intro = Label(app, text='RULES :',font=msgFont)
intro.pack()
msg = Message(app,text=ruleString,width=700,font=msgFont)
msg.place(x=10,y=25)

pcImageLabel = Label(app,image=pcImageObject)
pcImageLabel.place(x=20,y=75)

userImageLabel = Label(app,image=userImageObject)
userImageLabel.place(x=515,y=75)

ValFont = Font(size = 18,weight='bold')

pcVal = Label(app,font=ValFont)
pcVal.place(x=180,y=135)

CelLabel = Label(app)
CelLabel.place(x=293,y=95)

userVal = Label(app,font=ValFont)
userVal.place(x=400,y=135)

pcScore = Label(app,text='PC\nScore: ',font=ValFont)
pcScore.place(x=20,y=235)

userScore = Label(app,text='USER\nScore: ',font=ValFont)
userScore.place(x=515,y=235)

verdict = Label(app,font=ValFont)
verdict.place(x=275,y=215)

def cleanSlate() :

    pcVal['text']=''
    CelLabel['image']=''
    userVal['text']=''
    verdict['text']=''

def playAgain() :
    score[0],score[1] = 0,0
    pcScore['text']='PC\nScore :'
    userScore['text']='USER\nScore :'
    cleanSlate()

def rock() :
    if score[0] < 5 and score[1] < 5 :
        cleanSlate()
        time.sleep(0.3)
        pc = random.choice(game_list)
        pcVal['text'] = pc.upper()
        userVal['text'] = 'ROCK'

        if pc == 'rock' :
            CelLabel['image'] = tieObject
        elif pc == 'paper' :
            CelLabel['image'] = pcCelObject
            score[0] += 1
        else :
            CelLabel['image'] = userCelObject
            score[1] += 1
        pcScore['text'] = 'PC\nScore: '
        pcScore['text'] += str(score[0])
        userScore['text'] = 'USER\nScore:'
        userScore['text'] += str(score[1])

        if score[0] is 5 :
            verdict['text'] = 'PC Wins!!'
        if score[1] is 5 :
            verdict['text'] = 'User Wins!!'


def paper() :
    if score[0] < 5 and score[1] < 5 :
        cleanSlate()
        time.sleep(0.3)
        pc = random.choice(game_list)
        pcVal['text'] = pc.upper()
        userVal['text'] = 'PAPER'

        if pc == 'paper' :
            CelLabel['image'] = tieObject
        elif pc == 'rock' :
            CelLabel['image'] = userCelObject
            score[1] += 1
        else :
            CelLabel['image'] = pcCelObject
            score[0] += 1
        pcScore['text'] = 'PC\nScore: '
        pcScore['text'] += str(score[0])
        userScore['text'] = 'USER\nScore:'
        userScore['text'] += str(score[1])

        if score[0] is 5 :
            verdict['text'] = 'PC Wins!!'
        if score[1] is 5 :
            verdict['text'] = 'User Wins!!'


def scissor() :
    if score[0] < 5 and score[1] < 5 :
        cleanSlate()
        time.sleep(0.3)
        pc = random.choice(game_list)
        pcVal['text'] = pc.upper()
        userVal['text'] = 'SCISSOR'

        if pc == 'scissor' :
            CelLabel['image'] = tieObject
        elif pc == 'paper' :
            CelLabel['image'] = userCelObject
            score[1] += 1
        else :
            CelLabel['image'] = pcCelObject
            score[0] += 1
        pcScore['text'] = 'PC\nScore: '
        pcScore['text'] += str(score[0])
        userScore['text'] = 'USER\nScore:'
        userScore['text'] += str(score[1])

        if score[0] is 5 :
            verdict['text'] = 'PC Wins!!'
        if score[1] is 5 :
            verdict['text'] = 'User Wins!!'

rockButton = Button(app,text='ROCK',font=ValFont,width=12,command=rock)
rockButton.place(x=20,y=320)

paperButton = Button(app,text='PAPER',font=ValFont,width=12,command=paper)
paperButton.place(x=240,y=320)

scissorButton = Button(app,text='SCISSOR',font=ValFont,width=12,command=scissor)
scissorButton.place(x=460,y=320)

playButton = Button(app,text='PLAY AGAIN',font=ValFont,width=18,command=playAgain)
playButton.place(x=20,y=420)

quitButton = Button(app,text='QUIT',font=ValFont,width=18,command=app.destroy)
quitButton.place(x=370,y=420)



mainloop()
