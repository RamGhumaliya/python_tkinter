import threading
from tkinter import*
import random
root = Tk()
root.config(bg="#6c6c6c")
root.title('GAME~1, more to go')
root.geometry("534x456")
comp_choice=['stone','paper','scissor']
computer_score = 0
player_score = 0
wid_of_tie_screen = 30
def time_collapse():
    root.destroy()
def press():
    global computer_score
    global player_score
    play_computer=random.choice(comp_choice)
    #print(play_computer)
    if play_computer == (comp_choice[0]):
        l6=Label(root,text="Player beats computer this round...!",fg="red",font="lucid 12 italic")
        l6.place(x=135,y=230)
        print("player wins")
        l2=Label(root,text="stone",width=10,font="helvetica 13 ")
        l2.place(x=315,y=340)
        player_score += 1
        if player_score >= 10:
            print("THE WINNER OF THE GAME IS OUR PLAYER")
            show_time = threading.Timer(3,time_collapse)
            show_time.start()
        l5.config(text="Player score:" + str(player_score))
    elif play_computer == comp_choice[1] :
        print("tie")
        l6=Label(root,text="round got tied...!",fg="red",font="lucid 12 italic",justify=CENTER,width=wid_of_tie_screen)
        l6.place(x=135,y=230)
        l2=Label(root,text="paper",width=10,font="helvetica 13")
        l2.place(x=315,y=340)
    elif play_computer == comp_choice[2] :
        l6=Label(root,text="Computer beats player this round...!",fg="red",font="lucid 12 italic")
        l6.place(x=135,y=230)
        print("computer wins")
        computer_score += 1
        if computer_score >= 10:
            print("COMPUTER WINS, WOULD NOW AI OVERPOWER THE HUMAN BRAIN !")
            show_time = threading.Timer(3,time_collapse)
            show_time.start()
        print(computer_score)
        l4.config(text="Computer score:" + str(computer_score))
        l2=Label(root,text="scissor",width=10,font="helvetica 13 ")
        l2.place(x=315,y=340)
                
def press1():
    global computer_score
    global player_score
    play_computer=random.choice(comp_choice)
    #print(play_computer)
    if play_computer == (comp_choice[0]):
        print("tie")
        l6=Label(root,text="round got tied...!",fg="red",font="lucid 12 italic",width=wid_of_tie_screen,justify=CENTER)
        l6.place(x=135,y=230)
        l2=Label(root,text="stone",width=10,font="helvetica 13 ")
        l2.place(x=315,y=340)
    elif play_computer == comp_choice[1] :
        l6=Label(root,text="Computer beats player this round...!",fg="red",font="lucid 12 italic")
        l6.place(x=135,y=230)
        print("computer wins")
        computer_score += 1
        if computer_score >= 10:
            print("COMPUTER WINS, WOULD NOW AI OVERPOWER THE HUMAN BRAIN !")
            show_time = threading.Timer(3,time_collapse)
            show_time.start()
        print(computer_score)
        l4.configure(text="Computer score:" + str(computer_score))
        l2=Label(root,text="paper",width=10,font="helvetica 13")
        l2.place(x=315,y=340)
    elif play_computer == comp_choice[2] :
        l6=Label(root,text="Player beats computer this round...!",fg="red",font="lucid 12 italic")
        l6.place(x=135,y=230)
        print("player wins")
        l2=Label(root,text="scissor",width=10,font="helvetica 13 ")
        l2.place(x=315,y=340)
        player_score += 1
        if player_score >= 10:
            print("THE WINNER OF THE GAME IS OUR PLAYER")
            show_time = threading.Timer(3,time_collapse)
            show_time.start()
        l5.configure(text="Player score:" + str(player_score))
                
def press2():
    global computer_score
    global player_score
    play_computer=random.choice(comp_choice)
    #print(play_computer)
    if play_computer == (comp_choice[0]):
        l6=Label(root,text=" Computer beats player this round...!",fg="red",font="lucid 12 italic")
        l6.place(x=135,y=230)
        print("computer wins")
        computer_score += 1
        if computer_score >= 10:
            print("COMPUTER WINS, WOULD NOW AI OVERPOWER THE HUMAN BRAIN !")
            show_time = threading.Timer(3,time_collapse)
            show_time.start()
        print(computer_score)
        l4.config(text="Computer score:" + str(computer_score))
        l2=Label(root,text="stone",width=10,font="helvetica 13 ")
        l2.place(x=315,y=340)
    elif play_computer == comp_choice[1] :
        l6=Label(root,text="Player beats computer this round...!",fg="red",font="lucid 12 italic")
        l6.place(x=135,y=230)
        print("player wins")
        l2=Label(root,text="paper",width=10,font="helvetica 13")
        l2.place(x=315,y=340)
        player_score += 1
        if player_score >= 10:
            print("THE WINNER OF THE GAME IS OUR PLAYER")
            show_time = threading.Timer(3,time_collapse)
            show_time.start()
        l5.config(text="Player score:" + str(player_score))
    elif play_computer == comp_choice[2] :
        print("tie")
        l6=Label(root,text="round got tied...!",fg="red",font="lucid 12 italic",width=wid_of_tie_screen,justify=CENTER)
        l6.place(x=135,y=230)
        l2=Label(root,text="scissor",width=10,font="helvetica 13 ")
        l2.place(x=310,y=340)
                
f1 = Frame(root,bg="#303030")
f1.pack(side=TOP,fill=X)

l1= Label(f1,text="  STONE PAPER SCISSORS   ",font="helvetica 28 bold ",bg="#000000",fg="#e8ceb6",justify=CENTER,relief=FLAT)
l1.pack(side=TOP,padx=23,pady=36)

l3=Label(root,text="COMP. CHOICE IS:",width=20,font="helvetica 13 bold")
l3.place(x=130,y=340)

b1=Button(root,text="PAPER",font="comicsans 16 bold",fg="powder blue",command=press,relief=FLAT)
b1.place(x=220,y=140)

b2=Button(root,text=" STONE ",font="comicsans 16 bold",fg="powder blue",command=press1,relief=FLAT)
b2.place(x=75,y=140)

b3=Button(root,text="SCISSOR",font="comicsans 16 bold",fg="powder blue",command=press2,relief=FLAT)
b3.place(x=350,y=140)

l4 = Label(root,text="Computer score:",font="helvetica 12 italic",bg="#e8ceb6",justify=CENTER)
l4.place(x=500,y=400,anchor="se")
l5 = Label(root,text="Player score:",font="helvetica 12 italic",bg="#e8ceb6",justify=CENTER)
l5.place(x=140,y=400,anchor="se")

root.mainloop()

print("Computer final score was: ",computer_score)
print("Player's final score was: ",player_score)


