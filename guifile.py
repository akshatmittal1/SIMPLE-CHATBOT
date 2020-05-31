# import require files like json(for stored data) tkinter(for making gui struture) etc
from tkinter import *
# import message from tkinter display error , info , and also use to ask question alert
from tkinter import messagebox
# get_close_matches  this is used to find out the similar word in a list
from difflib import get_close_matches
# java script object notation file is used to a data and retrive a data easily
import json
# in this we load a intent.json file which store all basic command
data1 = json.load(open("intent.json"))
# data.json store a huge data with the help of we find the meaning of word
data = json.load(open("data.json"))
# this help to find out he date and time
import datetime
# create an object
root=Tk()
# to set a dimendion widthxheight+x(location of screen from x)+y(from y)
root.geometry("400x470+1100+300")
# off resizable because to maintain proper structure of gui
root.resizable(width=FALSE, height=FALSE)
# to set a title
root.title("CHATBOT")
# to set an icon
root.iconbitmap("a.ico")

# here we describe all function which we used
# help button fuction
def helpbutton():
    # create a message box
    messagebox.showinfo("HELP BOX","1. It is a simple chatbot answer a basic input (like helloo ,name,byee,etc) .\n\n"
                                   "2. It also used to find out the difficult words\n\n"
                                   "3. 'CLEAR' word is use to clean initialize the display.\n\n"
                                   "4. 'Exit' word is use to close Assiatant.")



def translate(w):
    # w is a word which we send fron text widget
    # then we convert into lower case lower() and also remove starting and ending useless spacing from the word strip()
    w = w.lower().strip()
    # we replace a space between sentence and to make a single word easy to compare
    w=w.replace(" ","")
    if w=="exit":
        # close predefined function
        exit()
    if w=="clear":
        # it is used to clean response text widget
        response.delete("0.0", END)
        # again wishme function
        wishme()
        # return blank word
        return ''
    if w in data1:
        # initially we check word / sentence is present in intent.json if exactly similar result found then return value
        return data1[w]
    elif len(get_close_matches(w, data1.keys())) > 0:
        # again try to find the word with get_close_matches and if found then return value else ignore it
        return data[get_close_matches(w, data1.keys())[0]]

    if w in data:
        # it is used to check word is present in data.json if exactly similar result found then return value
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        # again try to find the word with get_close_matches and if found then ask user word correct or not with messagebox
        yn = messagebox.askyesnocancel("WORD CONFIRMATION ","Did you mean %s instead? Enter Y if yes, or N if no : " %get_close_matches(w, data.keys())[0])
        # if message box return value is True then return value
        if yn == True:
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == False:
            # if not then return this statement
            return "The word doesn't exist. Please double check it."
        else:
            return "The word doesn't exist. Please double check it."

    else:
        # if word is not find in both file then return this statement
        return "This word is not present in a files so please add manually"


# result display function
def result(e):
    '''
        with the get() method we fetch the data from request text widget
        some arguement pass like "1.0" means starts from 1st line.. 0 character..
        "end-1c"  end to 2nd last character ( -(minus) 1 c(character)) because last character store next line variable
    '''
    content = request.get("1.0", 'end-1c').strip()
    # then delete all text fron request text widget
    request.delete("0.0", END)
    request.insert("0.0","")
    # check weather content is non empty
    if content != '':
        # response.config normal because we want to write something through program
        response.config(state=NORMAL)
        # print a word that we pass to program
        response.insert(END, "User : " + content + '\n\n')
        # this is use pass the content to translate function so some condition will be apply
        output1 = translate(content)
        # sometimes our resut come in list form this is to convert in string
        if type(output1) == list:
            for item in output1:
                output2 = item
        else:
            output2 = output1
        # if output is blank then skip this
        if output2 !='':
            # print a output on reponse text widget
            response.insert(END, "Bot: " + output2 + '\n\n')
    response.config(state=DISABLED)
    # this is used to see the last message on the text widget
    response.yview(END)


# wishme function
def wishme():
    # insert a hello in a response text widget
    response.insert(INSERT, "Bot: Hello")
    response.insert(INSERT, "\n\n")
    # find out the current hour
    hour = int(datetime.datetime.now().hour)
    # with help of condition set response result
    if hour >=0 and hour<=12:
        response.insert(INSERT,"Bot: Good Morning! ")
    elif hour>=12 and hour <18:
        response.insert(INSERT,"Bot: Good Aftenoon!")
    else:
        response.insert(INSERT,"Bot: Good Evening! ")
    # for proper spacing
    response.insert(INSERT, "\n\n")









# create text widget which is used to display data
response = Text(root)
# change configuration to set display text color font and size
response.config(foreground="black", font=("Verdana", 14),bd=0)

# create text widget where we type a sentence and send to computer
request = Text(root)
# change configuration to set sending text color font and size
request.config(foreground="black", font=("Times", 16),bd=0)
# create a button that send a request to computer program
send = Button(root, text="Send" ,command=lambda :result(e=0))
# set a configuration of button
send.config(fg='white',bg="limegreen",font=("Times", 18, 'bold'))
# create a scrollbar
scrlbar = Scrollbar(root)
# set a config according to axis vertical=yview and horizontal=xview
scrlbar.config(command=response.yview)
# set config to combine scrollbar and response text widget
response.config(yscrollcommand=scrlbar.set)
# load a image
icon=PhotoImage(file = "help.png")
#create a image button to provide informatiom to new user as a messagebox
HelpButton = Button(root,image=icon,bd=0,command=helpbutton)





# it is used to bind the request text widget to enter button in keyboard
request.bind("<Return>", result)




'''1. At the last we pack all widget in tk window
   2. There are 3 typer of manager pack() grid() place()
   3. place() is advance and easy to use manager in this we define position in form x&y and height and width also  '''
HelpButton.place(x=377, y=6, height=24)
response.place(x=6, y=6, height=406, width=370)
request.place(x=6, y=420, height=40, width=300)
scrlbar.place(x=376, y=30, height=382)
send.place(x=300, y=420, height=40,width=85)


# call wish me fuction to initialize response
wishme()
# it is used user cannot type on response text widget
response.config(state=DISABLED)
# bind a whole str. in a loop to display continous result
root.mainloop()
