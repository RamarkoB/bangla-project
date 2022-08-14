#import modules
import random as rand
import tkinter as tk
import csv

#intializes lists to sort letters into
letters = list()
conjuncts = list()
vowels = list()
consonents = list()

#opens csv file
data = open("bangla.csv")
data = csv.reader(data)

#parses csv file and seperates into categories
for line in data:
    if line[2] == "Conjunct":
        conjuncts.append(line)
    elif line[2] == "Vowel Sign":
        vowels.append(line)
    elif line[2] == "Vowel Full":
        letters.append(line)
    elif line[2] == "Consonent":
        consonents.append(line)
        int = rand.randint(0,len(vowels) - 1)
        a = line[0] + vowels[int][0] 
        b = line[1].replace("a", vowels[int][1].lower()) 
        c = "Combination"
        letters.append([a,b,c])

#randomizes a list of all Bangla letters
length = len(letters)
conlength = len(conjuncts)
rand.shuffle(letters)
rand.shuffle(conjuncts)

#initializes a global mode variable and a global iterable variable
i = 0

#restarts process
def restart():
        #resets global variables
        global i
        global letters
        global conjuncts
        i = 0

        #remixes vowel/consonent combinations
        letters = [combo for combo in letters if combo[2] != "Combination"]
        for letter in consonents:
            int = rand.randint(0,len(vowels) - 1)
            a = letter[0] + vowels[int][0] 
            b = letter[1].replace("a", vowels[int][1].lower()) 
            c = "Combination"
            letters.append([a,b,c])

        #reshuffles letters
        rand.shuffle(letters)
        rand.shuffle(conjuncts)
        labelen.pack_forget()
        labelba.pack_forget()

        #reopens menu
        menu()

#english-to-bangla practice
def tobangla():
    #sets global variables
    global mode
    mode = "bangla"

    #resets screen geometry
    root.geometry('250x385')
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    button5.pack_forget()

    #Creates labels and buttons
    labelen.config(text=letters[i][1], font=("Arial", 80))
    labelba.config(text="?", font=("Arial", 150))
    button1.config(text="Answer", command=answer)
    button2.config(text="Restart", command=restart)

    #starts off with first letter
    labelen.pack(side="top")
    labelba.pack(side="top")
    button1.pack(side="bottom")

#bangla-to-english practice
def toenglish():
    #sets global variables
    global mode
    mode = "english"
    
    #resets screen geometry
    root.geometry('250x385')
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    button5.pack_forget()
        
    #Creates labels and buttons
    labelen.config(text="???", font=("Arial", 80))
    labelba.config(text=letters[i][0], font=("Arial", 150))
    button1.config(text="Answer", command=answer)
    button2.config(text="Restart", command=restart)

    #starts off with first letter
    labelen.pack(side="top")
    labelba.pack(side="top")
    button2.pack(side="bottom")

#letters-to-conjuncts practice
def toconjuncts():
    #sets global variables
    global mode
    mode = "conjuncts"

    #resets screen geometry
    root.geometry('400x385')
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    button5.pack_forget()
        
    #Creates labels and buttons
    labelen.config(text=conjuncts[i][1], font=("Arial", 80))
    labelba.config(text="?", font=("Arial", 150))
    button1.config(text="Answer", command=answer)
    button2.config(text="Restart", command=restart)

    #starts off with first letter
    labelen.pack(side="top")
    labelba.pack(side="top")
    button1.pack(side="bottom")

#conjuncts-to-letters practice
def toletters():
    #sets global variables
    global mode
    mode = "letters"

    #resets screen geometry
    root.geometry('400x385')
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    button5.pack_forget()
        
    #Creates labels and buttons
    labelen.config(text="???", font=("Arial", 80))
    labelba.config(text=conjuncts[i][0], font=("Arial", 150))
    button1.config(text="Answer", command=answer)
    button2.config(text="Restart", command=restart)

    #starts off with first letter
    labelen.pack(side="top")
    labelba.pack(side="top")
    button1.pack(side="bottom")

#just mess me up, my guy
def messmeup():
    global mode
    global messrand
    global messlen
    global messlist
    mode = "messmeup"
    #resets screen geometry
    root.geometry('400x385')
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    button5.pack_forget()
    
    #creates variables for list
    messlist = letters + conjuncts
    rand.shuffle(messlist)
    messlen = len(messlist)

    #randomizes labels and creates buttons
    messrand = rand.randint(0,1)
    if messrand == 0:
        labelen.config(text="???", font=("Arial", 80))
        labelba.config(text=messlist[i][0], font=("Arial", 150))
    if messrand == 1:
        labelen.config(text=messlist[i][1], font=("Arial", 80))
        labelba.config(text="?", font=("Arial", 150))
    button1.config(text="Answer", command=answer)
    button2.config(text="Restart", command=restart)

    #starts off with first letter
    labelen.pack(side="top")
    labelba.pack(side="top")
    button1.pack(side="bottom")

#stops process
def stop():
    root.geometry('210x145')
    labelba.pack_forget()
    labelen.config(text="Done!")
    button1.config(text="Stop", command=root.destroy)
    button2.pack(side="bottom")

#updates widget with new letter
def update():
    global i
    global messlen
    global messrand
    i += 1
    if mode == "bangla":
        if i == length:
            stop()
            return
        labelen.config(text=letters[i][1])
        labelba.config(text="?")
    if mode == "english":
        if i == length:
            stop()
            return
        labelba.config(text=letters[i][0])
        labelen.config(text="???")
    if mode == "conjuncts":
        if i == conlength:
            stop()
            return
        labelen.config(text=conjuncts[i][1])
        labelba.config(text="?")
    if mode == "letters":
        if i == conlength:
            stop()
            return
        labelba.config(text=conjuncts[i][0])
        labelen.config(text="???")
    if mode == "messmeup":
        if i == messlen:
            stop()
            return
        messrand = rand.randint(0,1)
        if messrand == 0:
            labelen.config(text="???", font=("Arial", 80))
            labelba.config(text=messlist[i][0], font=("Arial", 150))
        if messrand == 1:
            labelen.config(text=messlist[i][1], font=("Arial", 80))
            labelba.config(text="?", font=("Arial", 150))
    button1.config(text="Answer", command=answer)

#reveals answer
def answer():
    global i
    if mode == "bangla":
        print(i, letters[i])
        labelba.config(text=letters[i][0])
    if mode == "english":
        print(i, letters[i])
        labelen.config(text=letters[i][1])
    if mode == "conjuncts":
        print(i, conjuncts[i])
        labelba.config(text=conjuncts[i][0])
    if mode == "letters":
        print(i, conjuncts[i])
        labelen.config(text=conjuncts[i][1])
    if mode == "messmeup":
        if messrand == 0:
            labelen.config(text=messlist[i][1])
        if messrand == 1:
            labelba.config(text=messlist[i][0])
    button1.config(text="New", command=update)   

#menu buttons
def menu():
    root.geometry('210x90')
    button1.config(text="English-to-Bangla", command=tobangla)
    button1.pack(side="top")
    button2.config(text="Bangla-to-English", command=toenglish)
    button2.pack(side="top")
    button3.config(text="Letters-to-Conjuncts", command=toconjuncts)
    button3.pack(side="top")
    button4.config(text="Conjuncts-to-Letters", command=toletters)
    button4.pack(side="top")
    button5.config(text="mess-Me-Up", command=messmeup)
    button5.pack(side="top")


#creates root and frame
root = tk.Tk()
root.title('Bangla Practice')
frame = tk.Frame(root)
frame.pack()

#creates labels and buttons
labelen = tk.Label(frame, text="???", font=("Arial", 80))
labelba = tk.Label(frame, text="?", font=("Arial", 150),pady=30,padx=25)
button1 = tk.Button(frame)
button2 = tk.Button(frame)
button3 = tk.Button(frame)
button4 = tk.Button(frame)
button5 = tk.Button(frame)

#opens main screen
menu()

#main loop
root.mainloop()