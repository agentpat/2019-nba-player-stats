import pandas as pd
from tkinter import *
header = {
    'functions file'
}

pdata = pd.read_csv("nbaplayerstats2019.csv")

root = Tk()
root.title("NBA Filter")

Display = Text(root, height=30,width=150)
TitleLabel = Label(root,text="Player Data")
Search = Text(root,height=1, width=43)
Search.insert(END,"Enter a player's full name (case sensitive)")

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)
Display.insert(END,pdata.head(50).to_string())
TitleLabel.pack()
Display.pack()
Search.pack()

def findPlayer(event):
    Display.delete(1.0,END)
    player_name = str(Search.get("1.0",END)).strip()
    player = pdata[pdata['Player'].str.contains(player_name)==True]
    Display.insert(END,player.to_string())

SearchButton = Button(root,text="Search")
SearchButton.bind("<Button-1>",findPlayer)
SearchButton.pack()

def topPlayers(stat):
    display = pdata.sort_values(stat,ascending=False)
    display = display.reset_index(drop=True)
    return(display.head(50).to_string())

def PTS(event):
    Display.delete(1.0,END)
    Display.insert(END,topPlayers("PTS"))

def BLK(event):
    Display.delete(1.0,END)
    Display.insert(END,topPlayers("BLK"))

def STL(event):
    Display.delete(1.0,END)
    Display.insert(END,topPlayers("STL"))

def AST(event):
    Display.delete(1.0,END)
    Display.insert(END,topPlayers("AST"))

def Rbds(event):
    Display.delete(1.0,END)
    Display.insert(END,topPlayers("RB"))

def Threes(event):
    Display.delete(1.0,END)
    Display.insert(END,topPlayers("3P"))

PtsButton = Button(leftFrame,text="PTS")
PtsButton.bind("<Button-1>",PTS)
PtsButton.pack()

BLKButton = Button(leftFrame,text="BLKS")
BLKButton.bind("<Button-1>",BLK)
BLKButton.pack()

STLButton = Button(leftFrame,text="STLS")
STLButton.bind("<Button-1>",STL)
STLButton.pack()

RBButton = Button(leftFrame,text="RBDS")
RBButton.bind("<Button-1>",Rbds)
RBButton.pack()

AssistButton = Button(leftFrame,text="ASTS")
AssistButton.bind("<Button-1>",AST)
AssistButton.pack()

ThreesButton = Button(leftFrame,text="3PM")
ThreesButton.bind("<Button-1>",Threes)
ThreesButton.pack()

# player search touched up, multiple years (2018), 
#error handling in search

root.mainloop()

    

