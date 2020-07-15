words = ['Open','Apple','man','consoles','Scratches','tiger','Game','Neccessary','door','External','Text','user'
         ,'file','View','navigate','Code','refactor','run','tools','Window','help','Libraries','Pycharm','python',
         'project','keyboard','Environment','polution','Terminal','Event','Favourite','login','Account','Examples']

def labelSlider():
    global count,sliderWords
    text = 'Increse your typing speed here'
    if(count >= len(text)):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontlabel.configure(text=sliderWords)
    fontlabel.after(110,labelSlider)

def time():
    global timeleft,score,miss
    if(timeleft>=11):
        pass
    else:
        timeLabelCount.configure(fg='red')

    if(timeleft>0):
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit={} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Notification','For play again hit Retry button')
        if(rr==True):
            score = 0
            timeleft = 60
            miss = 0
            timeLabelCount.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
#funnction for when we type text it save and clear text box
def startGame(event):
    global score,miss
    if(timeleft == 60):
        time()

    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordlabel['text']):
        score+=1
        scoreLabelCount.configure(text=score)
        print('Score',score)
    else:
        miss+=1

    random.shuffle(words)
    wordlabel.configure(text=words[0])
    print(wordEntry.get())
    wordEntry.delete(0,END)


from tkinter import *
import random
from tkinter import messagebox

#_________________________rootmethod_________________________
#making Screen
#it make screen but we cant see
root = Tk()
root.geometry('800x600+300+50')
#background colour
root.configure(bg='powder blue')
root.title('Typing Speed Increser Game')
root.iconbitmap('keyboard_icon.ico')

#__________________________Variables_____________________________
score = 0
timeleft = 60
count = 0
sliderWords = ''
miss = 0

#__________________________labelMethod__________________________

fontlabel = Label(root,text='',font=('arial',20,'italic bold'),bg='powder blue',fg='grey',width=20)
fontlabel.place(x=200,y=10)
labelSlider()

random.shuffle(words) #randomly pic words from wordsList
wordlabel=Label(root,text=words[0],font=('arial',20,'italic bold'),bg='powder blue')
wordlabel.place(x=350,y=200)

scoreLabel = Label(root,text='Your Score:',font=('arial',20,'italic bold'),bg='powder blue')
scoreLabel.place(x=20,y=150)

scoreLabelCount = Label(root,text=score,font=('arial',20,'italic bold'),bg='powder blue',fg='blue')
scoreLabelCount.place(x=70,y=190)

timerLabel = Label(root,text='Time Left:',font=('arial',20,'italic bold'),bg='powder blue')
timerLabel.place(x=635,y=150)

timeLabelCount = Label(root,text=timeleft,font=('arial',20,'italic bold'),bg='powder blue',fg='blue')
timeLabelCount.place(x=675,y=190)

gamePlayDetailLabel = Label(root,text='Type word And Hit Enter',font=('arial',30,'italic bold'),bg='powder blue',
                            fg='dark Grey')
gamePlayDetailLabel.place(x=100,y=450)

#__________________________entryMethod________________________
wordEntry = Entry(root,font=('arial',20,'italic bold'),bd=5,justify='center')
wordEntry.place(x=240,y=300)
#direct type into box not need to click in text box
wordEntry.focus_set()


root.bind('<Return>',startGame)
#this loop execute cont. so we can see the scree
root.mainloop()