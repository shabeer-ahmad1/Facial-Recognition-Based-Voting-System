from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
import twilio
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random

try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PollingAgentClass,ElectionCommisionClass,VoterClass,AddCandidateClass,AddPollingAgentClass,ViewResultClass,AddVoter,PageNine):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PollingAgentClass")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class PollingAgentClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")


        GButton_520=tk.Button(self)
        GButton_520["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#ffffff"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Election Commission"
        GButton_520.place(x=0,y=0,width=200,height=50)
        GButton_520["command"] = self.GButton_520_command

        GButton_629=tk.Button(self)
        GButton_629["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times',size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#000000"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Polling Agent"
        GButton_629.place(x=200,y=0,width=200,height=50)
        GButton_629["command"] = self.GButton_629_command

        GButton_737=tk.Button(self)
        GButton_737["bg"] = "#d0cdcd"
        ft = tkfont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#ffffff"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "Voter"
        GButton_737.place(x=400,y=0,width=200,height=50)
        GButton_737["command"] = self.GButton_737_command

        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=60,width=600,height=40)

        GLabel_705=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"

        GLabel_705["justify"] = "center"
        GLabel_705["text"] = "CNIC"
        GLabel_705.place(x=30,y=150,width=100,height=25)

        GLineEdit_191=tk.Entry(self)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "center"
        GLineEdit_191["text"] = ""
        GLineEdit_191["relief"] = "solid"
        GLineEdit_191.place(x=180,y=150,width=350,height=25)

        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"

        GLabel_827["justify"] = "center"
        GLabel_827["text"] = "Password"
        GLabel_827.place(x=50,y=210,width=100,height=25)

        GLineEdit_360=tk.Entry(self,show="*")
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"

        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"

        GLineEdit_360.place(x=180,y=210,width=350,height=25)

        GLabel_154=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_154["font"] = ft
        GLabel_154["fg"] = "#333333"
        GLabel_154["bg"] = "#ffffff"

        GLabel_154["justify"] = "center"
        GLabel_154["text"] = "Constituency"
        GLabel_154.place(x=40,y=270,width=130,height=25)

        OPTIONS = [
            "Attock-1(PP-1)",
            "Attock-1(PP-2)",
            "Attock-2(PP-3)",
            "Attock-2(PP-4)",
            "Attock-2(PP-5)"
        ]

        variable = tk.StringVar(self)
        variable.set(OPTIONS[0])

        GListBox_541 = tk.OptionMenu(self, variable, *OPTIONS)
        GListBox_541["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GListBox_541["font"] = ft
        GListBox_541["bg"] = "#ffffff"

        GListBox_541["fg"] = "#000000"
        GListBox_541["justify"] = "center"

        GListBox_541.place(x=180,y=270,width=350,height=25)

        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Login"
        GButton_499["relief"] = "solid"



        GButton_499.place(x=460,y=340,width=70,height=25)
        GButton_499["command"] = self.GButton_499_command
        self.password = GLineEdit_360
        self.cnicNo = GLineEdit_191
        self.constituency = variable


    def GButton_520_command(self):
        self.controller.show_frame("ElectionCommisionClass")


    def GButton_629_command(self):
        print("command")


    def GButton_737_command(self):
        self.controller.show_frame("VoterClass")


    def GButton_499_command(self):
        if len(self.password.get()) == 0 or len(self.cnicNo.get()) == 0:
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            PollingAgentAlreadyExist = False

            exists = os.path.isfile("VotingData\PollingAgentData.csv")

            if exists:
                with open("VotingData\PollingAgentData.csv", "r", newline='') as f:
                    reader = csv.reader(f, delimiter=',', quotechar='"')
                    for line_num, content in enumerate(reader):
                        if content[2] == str(self.cnicNo.get()) and content[4] == str(self.password.get()) and content[
                            8] == str(self.constituency.get()):
                            PollingAgentAlreadyExist = True
                            self.controller.show_frame("AddVoter")

                            # display msg to take photos first then save profile
                            mess.showinfo("Important",
                                          "1). If user is being registered on run time then you have to take photos first before saving the profile.\n\n2). If user images are already saved in training dataset then simply click on save profile button.")

                            self.cnicNo.delete(0, 'end')
                            self.password.delete(0, 'end')
                            break
                    if not PollingAgentAlreadyExist:
                        mess.showwarning("No Record", "Agent Does not Exist")

                    print("command")
                f.close()


class ElectionCommisionClass(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")


        GButton_520=tk.Button(self)
        GButton_520["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#000000"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Election Commission"
        GButton_520.place(x=0,y=0,width=200,height=50)
        GButton_520["command"] = self.GButton_520_command

        GButton_629=tk.Button(self)
        GButton_629["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#ffffff"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Polling Agent"
        GButton_629.place(x=200,y=0,width=200,height=50)
        GButton_629["command"] = self.GButton_629_command

        GButton_737=tk.Button(self)
        GButton_737["bg"] = "#d0cdcd"
        ft = tkfont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#ffffff"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "Voter"
        GButton_737.place(x=400,y=0,width=200,height=50)
        GButton_737["command"] = self.GButton_737_command

        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=60,width=600,height=40)



        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"

        GLabel_827["justify"] = "center"
        GLabel_827["text"] = "Username"
        GLabel_827.place(x=50,y=210,width=100,height=25)

        GLineEdit_360=tk.Entry(self)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"

        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"

        GLineEdit_360.place(x=180,y=210,width=350,height=25)

        GLabel_154=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_154["font"] = ft
        GLabel_154["fg"] = "#333333"
        GLabel_154["bg"] = "#ffffff"

        GLabel_154["justify"] = "center"
        GLabel_154["text"] = "Password"
        GLabel_154.place(x=40,y=270,width=130,height=25)

        GLineEdit_63=tk.Entry(self,show="*")
        GLineEdit_63["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_63["font"] = ft
        GLineEdit_63["fg"] = "#333333"
        GLineEdit_63["justify"] = "center"
        GLineEdit_63["text"] = ""
        GLineEdit_63["relief"] = "solid"

        GLineEdit_63.place(x=180,y=270,width=350,height=25)

        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Login"
        GButton_499["relief"] = "solid"


        GButton_499.place(x=460,y=340,width=70,height=25)
        GButton_499["command"] = self.GButton_499_command
        self.userName=GLineEdit_360
        self.password=GLineEdit_63

    def GButton_520_command(self):
        print("command")


    def GButton_629_command(self):
        self.controller.show_frame("PollingAgentClass")


    def GButton_737_command(self):
        self.controller.show_frame("VoterClass")


    def GButton_499_command(self):
        UserExists=False
        with open("VotingData/ElectionCommisionData.csv", "r", newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for line_num, content in enumerate(reader):
                if content[0] == str(self.userName.get()) and content[2] == str(self.password.get()):
                    UserExists=True
                    break
        #if self.userName.get() == "abc@ec.com" and self.password.get() == "election123":
        if UserExists:
            self.controller.show_frame("AddCandidateClass")
            self.userName.delete(0,'end')
            self.password.delete(0,'end')
        else:
            mess.showinfo("Wrong Credentials","Please Enter Correct Credentials")
            print(self.userName.get())
            print(self.password.get())



class Pages:
    p = ''
    q = ''
    r=''
class PageNine(tk.Frame,Pages):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        GLabel_705 = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"
        GLabel_705["text"] = "Candidate"
        GLabel_705.place(x=40, y=200, width=130, height=25)







        party = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        party["font"] = ft
        party["fg"] = "#333333"
        party["bg"] = "#ffffff"
        GButton_520 = tk.Button(self)
        GButton_520["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times', size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#ffffff"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Election Commission"
        GButton_520.place(x=0, y=0, width=200, height=50)
        GButton_520["command"] = self.GButton_520_command

        GButton_629 = tk.Button(self)
        GButton_629["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times', size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#ffffff"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Polling Agent"
        GButton_629.place(x=200, y=0, width=200, height=50)
        GButton_629["command"] = self.GButton_629_command

        GButton_737 = tk.Button(self)
        GButton_737["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times', size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#000000"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "Voter"
        GButton_737.place(x=400, y=0, width=200, height=50)
        GButton_737["command"] = self.GButton_737_command

        GLabel_711 = tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times', size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0, y=60, width=600, height=40)

        party["justify"] = "center"
        party["text"] = "Party"
        party.place(x=40, y=150, width=130, height=25)

        from PIL import ImageTk, Image
        ab = Image.open("ImageResources/pti.png")
        im1 = ab.resize((50, 50))
        img = ImageTk.PhotoImage(im1)

        canvas = tk.Label(self, image=img)
        canvas.image = img
        canvas.place(x=450, y=150, width=50, height=45)

        OPTIONS = [
            "PTI",
            "PMLN",
            "PPP",
            "JUI",
            "IND"
        ]

        variable = tk.StringVar(self)
        variable.set("Select Party")

        partydropdown = tk.OptionMenu(self, variable, *OPTIONS, command=self.func)
        partydropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        partydropdown["font"] = ft
        partydropdown["fg"] = "#333333"
        partydropdown["justify"] = "center"
        partydropdown["text"] = "Entry"
        partydropdown["relief"] = "solid"

        partydropdown.place(x=180, y=150, width=250, height=25)

        candidate = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        candidate["font"] = ft
        candidate["fg"] = "#333333"
        candidate["bg"] = "#ffffff"

        candidate["justify"] = "center"
        candidate["text"] = "Candidate"
        candidate.place(x=40, y=200, width=130, height=25)
        candidates = [
            ""

        ]

        variableCand = tk.StringVar(self)
        variableCand.set("")

        candidatedropdown = tk.OptionMenu(self, variableCand, *candidates)
        candidatedropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        candidatedropdown["font"] = ft
        candidatedropdown["fg"] = "#333333"
        candidatedropdown["justify"] = "center"
        candidatedropdown["text"] = ""
        candidatedropdown["relief"] = "solid"

        candidatedropdown.place(x=180, y=200, width=250, height=25)

        GButton_499 = tk.Button(self)
        GButton_499["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times', size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#000000"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Cast Vote"
        GButton_499["relief"] = "solid"

        GButton_499.place(x=460, y=430, width=70, height=25)
        GButton_499["command"] = self.GButton_499_command

        #button3.bind("<Button-1>", self.pasvariable)

        #self.labID = GLineEdit_360

        self.cons = variable
        self.canvas = canvas
        self.candidates = variableCand
        self.candidatedd = candidatedropdown


    def GButton_520_command(self):
        self.controller.show_frame("ElectionCommisionClass")

    def GButton_629_command(self):
        self.controller.show_frame("PollingAgentClass")

    def GButton_737_command(self):
        print("command")

    def GButton_499_command(self):
        if ( self.candidates.get() !="" and self.cons.get()!="" and self.cons.get()!="Select Party"):
            self.SaveVoter()
        else:
            mess.showinfo("Please Fill all details","Some Data Missing")

    def SaveVoter(self):
        attendance = [str(Pages.q), '',Pages.r,'', Pages.p, '', self.cons.get(), '', self.candidates.get()]
        col_names = ['Id', '','Name','', 'Constituency', '', 'Party Voted', '', 'Candidate']

        exists = os.path.isfile("VotingData\AVotingData.csv")
        VoterAlreadyExist = False
        if exists:
            with open("VotingData\AVotingData.csv", "r", newline='') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                for line_num, content in enumerate(reader):
                    if content[0] == str(Pages.q):
                        VoterAlreadyExist = True
                        break
            if not VoterAlreadyExist:
                with open("VotingData\AVotingData.csv", 'a+', newline='') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(attendance)
                csvFile1.close()

                #self.candidatedd.delete(0, 'end')
            else:
                mess.showinfo("Already Voted", "Already Voted")


        else:

            with open("VotingData\AVotingData.csv", 'a+', newline='') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()

        # cam.release()
        cv2.destroyAllWindows()

    def func(self, value):
        from PIL import ImageTk, Image
        labName = Pages.p



        if str(value) == str("PMLN"):
            ab = Image.open("ImageResources/pmln.png")
        elif str(value) == str("PTI"):
            ab = Image.open("ImageResources/pti.png")
        elif str(value) == str("PPP"):
            ab = Image.open("ImageResources/ppp.png")
        elif str(value) == str("JUI"):
            ab = Image.open("ImageResources/jui.png")
        else:
            ab = Image.open("ImageResources/indy.png")
        im1 = ab.resize((50, 50))
        img = ImageTk.PhotoImage(im1)

        self.canvas.configure(image=img)
        self.canvas.image = img
        listOfCandidate = []
        with open("VotingData\CandidateData.csv", "r", newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for line_num, content in enumerate(reader):
                if content[6] == str(labName) and content[0] == str(self.cons.get()):
                    listOfCandidate.append(content[2])
        f.close()

        def callback(*args):
            self.candidates.set('')
            listOfCandidate = []
            with open("VotingData\CandidateData.csv", "r", newline='') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                for line_num, content in enumerate(reader):
                    if content[6] == str(labName) and content[0] == str(self.cons.get()):
                        listOfCandidate.append(content[2])
            f.close()
            #prtyName = ""
            print(listOfCandidate)

            self.candidatedd.configure(state='active')
            self.candidatedd['menu'].delete(0, 'end')
            for fi in listOfCandidate:
                self.candidatedd['menu'].add_command(label=fi, command=lambda fi=fi: self.candidates.set(fi))

            f.close()

        self.cons.trace("w", callback)

    '''
    def pasvariable(self, var):
        # m = PageOne.__init__(self,parent,controller)
        self.labID.delete(0, 'end')
        self.labName.delete(0, 'end')
        self.labName.insert(0,str(Pages.p))
        self.labID.insert(0,str(Pages.r))
        listOfCandidate=[]
        with open("VotingData\CandidateData.csv", "r", newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for line_num, content in enumerate(reader):
                if content[6] == str(Pages.p) and content[0] == str(self.cons.get()):
                    listOfCandidate.append(content[2])
        f.close()
        def callback(*args):
            self.candidates.set('')
            listOfCandidate = []
            with open("VotingData\CandidateData.csv", "r", newline='') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                for line_num, content in enumerate(reader):
                    if content[6] == str(self.labName.get()) and content[0] == str(self.cons.get()):
                        listOfCandidate.append(content[2])
            f.close()
            prtyName = ""

            self.candidatedd.configure(state='active')
            self.candidatedd['menu'].delete(0, 'end')
            for fi in listOfCandidate:
                self.candidatedd['menu'].add_command(label=fi, command=lambda fi=fi: self.candidates.set(fi))


            f.close()


        self.candidatedd.configure(state='active')
        for fi in listOfCandidate:
            self.candidatedd['menu'].add_command(label=fi, command=lambda fi=fi: self.candidates.set(fi))
        self.cons.trace("w", callback)
        '''


    #mess.showinfo(Pages.p,Pages.p)





class VoterClass(tk.Frame,Pages):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")


        GButton_520=tk.Button(self)
        GButton_520["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#ffffff"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Election Commission"
        GButton_520.place(x=0,y=0,width=200,height=50)
        GButton_520["command"] = self.GButton_520_command

        GButton_629=tk.Button(self)
        GButton_629["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#ffffff"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Polling Agent"
        GButton_629.place(x=200,y=0,width=200,height=50)
        GButton_629["command"] = self.GButton_629_command

        GButton_737=tk.Button(self)
        GButton_737["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#000000"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "Voter"
        GButton_737.place(x=400,y=0,width=200,height=50)
        GButton_737["command"] = self.GButton_737_command

        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=60,width=600,height=40)

        GLabel_705=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"

        GLabel_705["justify"] = "center"
        GLabel_705["text"] = "CNIC"
        GLabel_705.place(x=50,y=150,width=100,height=25)

        GLineEdit_191=tk.Entry(self)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "center"
        GLineEdit_191["text"] = ""
        GLineEdit_191["relief"] = "solid"
        GLineEdit_191.place(x=180,y=150,width=350,height=25)

        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"

        GLabel_827["justify"] = "center"
        GLabel_827["text"] = "Phone #"
        GLabel_827.place(x=50,y=210,width=100,height=25)

        GLineEdit_360=tk.Entry(self)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"

        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"

        GLineEdit_360.place(x=180,y=210,width=350,height=25)

        GLabel_154=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_154["font"] = ft
        GLabel_154["fg"] = "#333333"
        GLabel_154["bg"] = "#ffffff"

        GLabel_154["justify"] = "center"
        GLabel_154["text"] = "Password"
        GLabel_154.place(x=40,y=270,width=130,height=25)

        GLineEdit_63=tk.Entry(self)
        GLineEdit_63["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_63["font"] = ft
        GLineEdit_63["fg"] = "#333333"
        GLineEdit_63["justify"] = "center"
        GLineEdit_63["text"] = ""
        GLineEdit_63["relief"] = "solid"

        GLineEdit_63.place(x=180,y=270,width=350,height=25)

        GLabel_705["justify"] = "center"
        GLabel_705["text"] = "Constituency"
        GLabel_705.place(x=30, y=320, width=150, height=25)

        GLineEdit_192 = tk.Entry(self)
        GLineEdit_192["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GLineEdit_192["font"] = ft
        GLineEdit_192["fg"] = "#333333"
        GLineEdit_192["justify"] = "center"
        GLineEdit_192["text"] = ""
        GLineEdit_192["relief"] = "solid"
        GLineEdit_192.place(x=180, y=320, width=350, height=25)

        GLabel_827 = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"

        GLabel_827["justify"] = "center"
        GLabel_827["text"] = "Name"
        GLabel_827.place(x=30, y=360, width=140, height=25)

        GLineEdit_361 = tk.Entry(self)
        GLineEdit_361["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GLineEdit_361["font"] = ft
        GLineEdit_361["fg"] = "#333333"

        GLineEdit_361["justify"] = "center"
        GLineEdit_361["text"] = ""
        GLineEdit_361["relief"] = "solid"

        GLineEdit_361.place(x=180, y=360, width=350, height=25)

        '''

        party = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        party["font"] = ft
        party["fg"] = "#333333"
        party["bg"] = "#ffffff"


        party["justify"] = "center"
        party["text"] = "Party"
        party.place(x=40, y=330, width=130, height=25)

        from PIL import ImageTk, Image
        ab = Image.open("ImageResources/pti.png")
        im1 = ab.resize((50, 50))
        img = ImageTk.PhotoImage(im1)

        canvas = tk.Label(self, image=img)
        canvas.image = img
        canvas.place(x=450, y=330, width=50, height=45)

        OPTIONS = [
            "PTI",
            "PMLN",
            "PPP",
            "JUI",
            "IND"
        ]

        variable = tk.StringVar(self)
        variable.set(OPTIONS[0])

        partydropdown = tk.OptionMenu(self, variable, *OPTIONS,command=self.func)
        partydropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        partydropdown["font"] = ft
        partydropdown["fg"] = "#333333"
        partydropdown["justify"] = "center"
        partydropdown["text"] = "Entry"
        partydropdown["relief"] = "solid"

        partydropdown.place(x=180, y=330, width=250, height=25)

        candidate = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        candidate["font"] = ft
        candidate["fg"] = "#333333"
        candidate["bg"] = "#ffffff"

        candidate["justify"] = "center"
        candidate["text"] = "Candidate"
        candidate.place(x=40, y=390, width=130, height=25)
        candidates = [
            ""

        ]

        variableCand = tk.StringVar(self)
        variableCand.set(candidates[0])

        candidatedropdown = tk.OptionMenu(self, variableCand, *candidates)
        candidatedropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        candidatedropdown["font"] = ft
        candidatedropdown["fg"] = "#333333"
        candidatedropdown["justify"] = "center"
        candidatedropdown["text"] = ""
        candidatedropdown["relief"] = "solid"

        candidatedropdown.place(x=180, y=390, width=250, height=25)
        '''



        fetchImagebtn = tk.Button(self)
        ft = tkfont.Font(family='Times', size=10)
        fetchImagebtn["font"] = ft
        fetchImagebtn["fg"] = "#ffffff"
        fetchImagebtn["bg"] = "#11595F"
        fetchImagebtn["justify"] = "center"
        fetchImagebtn["text"] = "Fetch Details"
        fetchImagebtn["relief"] = "solid"
        fetchImagebtn.place(x=180, y=400, width=80, height=25)
        fetchImagebtn["command"] = self.fetchbtn_command

        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Login"
        GButton_499["relief"] = "solid"


        GButton_499.place(x=460,y=400,width=70,height=25)
        GButton_499["command"] = self.GButton_499_command

        self.labName = GLineEdit_191
        self.labName.config(state='readonly')
        self.labID = GLineEdit_360
        self.labID.config(state='readonly')
        self.voteParty =GLineEdit_63
        self.constituency=GLineEdit_192

        self.name=GLineEdit_361

        self.constituency.config(state='readonly')
        self.name.configure(state='readonly')
        '''
        self.cons = variable
        self.canvas = canvas
        self.candidates = variableCand
        self.candidatedd = candidatedropdown
        '''
    def func(self, value):
        from PIL import ImageTk, Image

        if str(value) == str("PMLN"):
            ab = Image.open("ImageResources/pmln.png")
        elif  str(value) == str("PTI"):
            ab = Image.open("ImageResources/pti.png")
        elif  str(value) == str("PPP"):
            ab = Image.open("ImageResources/ppp.png")
        elif  str(value) == str("JUI"):
            ab = Image.open("ImageResources/jui.png")
        else:
            ab=Image.open("ImageResources/indy.png")



        im1 = ab.resize((50, 50))
        img = ImageTk.PhotoImage(im1)

        self.canvas.configure(image=img)
        self.canvas.image = img


    def fetchbtn_command(self):
        self.TrackImages()



    def GButton_520_command(self):
        self.controller.show_frame("ElectionCommisionClass")


    def GButton_629_command(self):
        self.controller.show_frame("PollingAgentClass")


    def GButton_737_command(self):
        self.labName.config(state='normal')
        self.labID.config(state='normal')
        self.constituency.config(state='normal')
        self.name.delete(state='normal')
        self.labName.delete(0, 'end')
        self.labID.delete(0, 'end')
        self.voteParty.delete(0,'end')
        self.constituency.delete(0,'end')
        self.name.delete(0,'end')



    def GButton_499_command(self):
        if len(self.labName.get()) == 0 or len(self.labID.get()) == 0 or len(
                self.voteParty.get()) == 0:
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            self.SaveVoter()

    def assure_path_exists(self, path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    def check_haarcascadefile(self):
        exists = os.path.isfile("haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            mess._show(title='Some file missing', message='Please contact us for help')

    def TrackImages(self):
        self.check_haarcascadefile()
        self.assure_path_exists("VotingData/")
        self.assure_path_exists("VoterDetails/")

        msg = ''
        self.i = 0
        j = 0
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
        if exists3:
            recognizer.read("TrainingImageLabel\Trainner.yml")
        else:
            mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
            return
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
        exists1 = os.path.isfile("VoterDetails\VoterDetails.csv")
        if exists1:
            df = pd.read_csv("VoterDetails\VoterDetails.csv")
        else:
            mess._show(title='Details Missing', message='Voter details are missing, please check!')
            cam.release()
            cv2.destroyAllWindows()
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values

                    ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                    constituency = df.loc[df['SERIAL NO.'] == serial]['CONSTITUENCY'].values

                    name = df.loc[df['SERIAL NO.'] == serial]['VOTERNAME'].values

                    #cons = df.loc[df['SERIAL NO.'] == serial]['CONSTITUENCY'].values
                    ID = str(ID)
                    ID = ID[1:-1]
                    bb = str(aa)
                    bb = bb[1:-1]
                    constituency=str(constituency)
                    name=str(name)
                    constituency=constituency[2:-2]
                    name = name[2:-2]


                    #cons = str(cons)
                    #cons = cons[2:-2]


                else:
                    Id = 'Unknown'
                    bb = str(Id)
                cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('Taking Attendance', im)
            if (cv2.waitKey(1) == ord('q')):
                break

        def callback(*args):
            listOfCandidate = []
            with open("VotingData\CandidateData.csv", "r", newline='') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                for line_num, content in enumerate(reader):
                    if content[6] == str(self.voteParty.get()) and content[0] == str(self.cons.get()):
                        listOfCandidate.append(content[2])
            f.close()
            prtyName = ""

            self.candidatedd.configure(state='active')
            self.candidatedd['menu'].delete(0, 'end')
            for fi in listOfCandidate:
                self.candidatedd['menu'].add_command(label=fi, command=lambda fi=fi: self.candidates.set(fi))

            cam.release()
            cv2.destroyAllWindows()
            f.close()

        self.labName.config(state='normal')
        self.labID.config(state='normal')
        self.constituency.config(state='normal')
        self.name.config(state='normal')

        self.labName.delete(0, 'end')
        self.labID.delete(0, 'end')
        self.constituency.delete(0, 'end')
        self.name.delete(0, 'end')

        self.labName.insert(0, bb)
        self.labID.insert(0, ID)
        self.labName.config(state='readonly')
        self.labID.config(state='readonly')
        self.constituency.insert(0, constituency)
        self.name.insert(0,name)
        self.constituency.config(state='readonly')
        self.name.config(state='readonly')

        #self.voteParty.insert(0, cons)
        self.ID = ID
        self.bb = bb
        listOfCandidate = []
        '''

        with open("VotingData\CandidateData.csv", "r", newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for line_num, content in enumerate(reader):
                if content[6] == str(self.voteParty.get()) and content[0] == str(self.cons.get()):
                    listOfCandidate.append(content[2])
        f.close()

        self.candidatedd.configure(state='active')
        for fi in listOfCandidate:
            self.candidatedd['menu'].add_command(label=fi, command=lambda fi=fi: self.candidates.set(fi))
        self.cons.trace("w", callback)
        '''

        cam.release()
        cv2.destroyAllWindows()


    def SaveVoter(self):
        passwordCorrect=False
        Constituency=''
        Name=''
        CNICNo=''
        phoneNum=''



        with open("VoterDetails\VoterDetails.csv", "r", newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for line_num, content in enumerate(reader):
                if content[4] == str(self.labName.get()) and content[10] == str(self.voteParty.get()):
                    passwordCorrect=True
                    Constituency=content[6]
                    Name=content[4]
                    CNICNo=content[8]
                    phoneNum=content[2]
                    break
        f.close()
        #print(Constituency)
        Pages.p=Constituency
        print(Pages.p)
        Pages.q=Name
        Pages.r=CNICNo

        #print(Pages.p)
        if passwordCorrect:
            self.otp = random.randint(1000, 9999)
            print("Your OTP is - ", self.otp)
            # Your Account Sid and Auth Token from twilio.com/console
            # DANGER! This is insecure. See http://twil.io/secure
            account_sid = 'AC0a63a25263fb79ab594d8fe7c09f5fea'
            auth_token = '81d1495c80c63926704f50d06c153e0e'

            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body='Your Secure Device OTP is - ' + str(self.otp) + ' ',
                from_='+18316619698',
                to=str(phoneNum)
            )
            password = tsd.askstring('OTP', 'Enter OTP', show='*')
            print(password)
            otp = self.otp
            print(otp)
            if str(password) == str(otp):
                self.controller.show_frame("PageNine")
            else:
                mess.showerror("Wrong OTP"," OTP Does not Match")

        else:
            mess.showinfo("Failure","No Record")
        '''
        attendance = [str(self.ID), '', self.bb, '', self.voteParty.get(), '', self.cons.get(), '',
                      self.candidates.get()]
        col_names = ['Id', '', 'Name', '', 'Constituency', '', 'Party Voted', '', 'Candidate']

        exists = os.path.isfile("VotingData\AVotingData.csv")
        VoterAlreadyExist = False
        if exists:
            with open("VotingData\AVotingData.csv", "r", newline='') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                for line_num, content in enumerate(reader):
                    if content[0] == str(self.ID):
                        VoterAlreadyExist = True
                        break
            if not VoterAlreadyExist:
                with open("VotingData\AVotingData.csv", 'a+', newline='') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(attendance)
                csvFile1.close()
                self.labID.delete(0, 'end')
                self.labName.delete(0, 'end')
                self.voteParty.delete(0, 'end')
            else:
                mess.showinfo("Already Voted", "Already Voted")


        else:

            with open("VotingData\AVotingData.csv", 'a+', newline='') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()

        # cam.release()
        cv2.destroyAllWindows()
    '''

class AddCandidateClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")


        GButton_520=tk.Button(self)
        GButton_520["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#000000"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Add Candidate"
        GButton_520.place(x=0,y=0,width=200,height=50)
        GButton_520["command"] = self.GButton_520_command

        GButton_629=tk.Button(self)
        GButton_629["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#ffffff"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Add Polling Agent"
        GButton_629.place(x=200,y=0,width=200,height=50)
        GButton_629["command"] = self.GButton_629_command

        GButton_737=tk.Button(self)
        GButton_737["bg"] = "#d0cdcd"
        ft = tkfont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#ffffff"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "View Results"
        GButton_737.place(x=400,y=0,width=200,height=50)
        GButton_737["command"] = self.GButton_737_command

        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=60,width=600,height=40)

        GLabel_705=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"

        GLabel_705["justify"] = "center"
        GLabel_705["text"] = "Candidate Name"
        GLabel_705.place(x=0,y=150,width=180,height=25)

        GLineEdit_191=tk.Entry(self)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "center"
        GLineEdit_191["text"] = ""
        GLineEdit_191["relief"] = "solid"
        GLineEdit_191.place(x=180,y=150,width=350,height=25)

        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"

        GLabel_827["justify"] = "center"
        GLabel_827["text"] = "CNIC"
        GLabel_827.place(x=50,y=210,width=100,height=25)

        GLineEdit_360=tk.Entry(self)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"

        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"

        GLineEdit_360.place(x=180,y=210,width=350,height=25)



        party = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        party["font"] = ft
        party["fg"] = "#333333"
        party["bg"] = "#ffffff"

        party["justify"] = "center"
        party["text"] = "Party"
        party.place(x=40, y=330, width=130, height=25)

        OPTIONS = [
            "PTI",
            "PMLN",
            "PPP",
            "JUI",
            "IND"
        ]

        variable = tk.StringVar(self)
        variable.set(OPTIONS[0])

        partydropdown = tk.OptionMenu(self, variable, *OPTIONS)
        partydropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        partydropdown["font"] = ft
        partydropdown["fg"] = "#333333"
        partydropdown["justify"] = "center"
        partydropdown["text"] = "Entry"
        partydropdown["relief"] = "solid"

        partydropdown.place(x=180, y=330, width=350, height=25)

        candidate = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        candidate["font"] = ft
        candidate["fg"] = "#333333"
        candidate["bg"] = "#ffffff"

        candidate["justify"] = "center"
        candidate["text"] = "Constituency"
        candidate.place(x=40,y=270,width=130,height=25)


        OPTIONS2 = [
            "Attock-1(PP-1)",
            "Attock-1(PP-2)",
            "Attock-2(PP-3)",
            "Attock-2(PP-4)",
            "Attock-2(PP-5)"
        ]

        variable2 = tk.StringVar(self)
        variable2.set(OPTIONS2[0])

        cons = tk.OptionMenu(self, variable2, *OPTIONS2)
        cons["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        cons["font"] = ft
        cons["fg"] = "#333333"
        cons["justify"] = "center"

        cons.place(x=180,y=270,width=350,height=25)



        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Save"
        GButton_499["relief"] = "solid"
        GButton_499.place(x=180, y=390, width=80, height=25)
        GButton_499["command"] = self.GButton_499_command

        returnButton = tk.Button(self)
        returnButton["bg"] = "#DC4D41"
        ft = tkfont.Font(family='Times', size=10)
        returnButton["font"] = ft
        returnButton["fg"] = "#ffffff"
        returnButton["justify"] = "center"
        returnButton["text"] = "Logout"
        returnButton["relief"] = "solid"
        returnButton.place(x=460,y=390,width=70,height=25)
        returnButton["command"] = self.returnButton_command

        self.cons = variable2
        self.party = variable
        self.cnic = GLineEdit_360
        self.candName = GLineEdit_191

    def returnButton_command(self):
            self.controller.show_frame("ElectionCommisionClass")


    def GButton_520_command(self):
        print("command")


    def GButton_629_command(self):
        self.controller.show_frame("AddPollingAgentClass")


    def GButton_737_command(self):
        self.controller.show_frame("ViewResultClass")


    def GButton_499_command(self):
        if len(self.cnic.get()) == 0 or len(self.candName.get()) == 0:
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            exists = os.path.isfile("VotingData\CandidateData.csv")
            agentDetails = [str(self.party.get()), '', str(self.candName.get()), '', str(self.cnic.get()), '',
                            str(self.cons.get())]
            col_names = ['Party Name', '', 'Candidate Name', '', 'CNIC', '', 'Constituency']
            PollingAgentAlreadyExist = False

            if exists:
                with open("VotingData\CandidateData.csv", "r", newline='') as f:
                    reader = csv.reader(f, delimiter=',', quotechar='"')
                    for line_num, content in enumerate(reader):
                        if content[4] == str(self.cnic.get()):
                            PollingAgentAlreadyExist = True
                            break
                if not PollingAgentAlreadyExist:
                    with open("VotingData\CandidateData.csv", 'a+', newline='') as csvFile1:
                        writer = csv.writer(csvFile1)
                        writer.writerow(agentDetails)
                    csvFile1.close()
                    mess.showinfo("Success", "Candidate Added Successfully")
                    self.cnic.delete(0, 'end')
                    self.candName.delete(0, 'end')

                else:
                    mess.showinfo("Failed", "Candidate's CNIC Already Exists")
                    print("Candidate's CNIC Already Exists")


            else:

                with open("VotingData\CandidateData.csv", 'a+', newline='') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(col_names)
                    writer.writerow(agentDetails)
                csvFile1.close()
                mess.showinfo("Success", "Candidate Added Successfully")
                self.cnic.delete(0, 'end')
                self.candName.delete(0, 'end')


class AddPollingAgentClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")


        GButton_520=tk.Button(self)
        GButton_520["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#ffffff"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Add Candidate"
        GButton_520.place(x=0,y=0,width=200,height=50)
        GButton_520["command"] = self.GButton_520_command

        GButton_629=tk.Button(self)
        GButton_629["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times',size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#000000"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Add Polling Agent"
        GButton_629.place(x=200,y=0,width=200,height=50)
        GButton_629["command"] = self.GButton_629_command

        GButton_737=tk.Button(self)
        GButton_737["bg"] = "#d0cdcd"
        ft = tkfont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#ffffff"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "View Results"
        GButton_737.place(x=400,y=0,width=200,height=50)
        GButton_737["command"] = self.GButton_737_command

        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=60,width=600,height=40)

        GLabel_705=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"

        GLabel_705["justify"] = "center"
        GLabel_705["text"] = "Name"
        GLabel_705.place(x=30,y=150,width=100,height=25)

        GLineEdit_191=tk.Entry(self)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "center"
        GLineEdit_191["text"] = ""
        GLineEdit_191["relief"] = "solid"
        GLineEdit_191.place(x=180,y=150,width=350,height=25)

        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"

        GLabel_827["justify"] = "center"
        GLabel_827["text"] = "CNIC"
        GLabel_827.place(x=50,y=210,width=100,height=25)

        GLineEdit_360=tk.Entry(self)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"

        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"

        GLineEdit_360.place(x=180,y=210,width=350,height=25)

        GLabel_154=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_154["font"] = ft
        GLabel_154["fg"] = "#333333"
        GLabel_154["bg"] = "#ffffff"

        GLabel_154["justify"] = "center"
        GLabel_154["text"] = "Password"
        GLabel_154.place(x=40,y=270,width=130,height=25)

        GLineEdit_63=tk.Entry(self)
        GLineEdit_63["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_63["font"] = ft
        GLineEdit_63["fg"] = "#333333"
        GLineEdit_63["justify"] = "center"
        GLineEdit_63["text"] = ""
        GLineEdit_63["relief"] = "solid"

        GLineEdit_63.place(x=180,y=270,width=350,height=25)

        party = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        party["font"] = ft
        party["fg"] = "#333333"
        party["bg"] = "#ffffff"

        party["justify"] = "center"
        party["text"] = "Phone #"
        party.place(x=40, y=340, width=130, height=25)



        partydropdown = tk.Entry(self)
        partydropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        partydropdown["font"] = ft
        partydropdown["fg"] = "#333333"
        partydropdown["justify"] = "center"
        partydropdown["text"] = ""
        partydropdown["relief"] = "solid"

        partydropdown.place(x=180, y=330, width=350, height=25)

        candidate = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        candidate["font"] = ft
        candidate["fg"] = "#333333"
        candidate["bg"] = "#ffffff"

        candidate["justify"] = "center"
        candidate["text"] = "Constituency"
        candidate.place(x=40, y=390, width=130, height=25)

        OPTIONS = [
            "Attock-1(PP-1)",
            "Attock-1(PP-2)",
            "Attock-2(PP-3)",
            "Attock-2(PP-4)",
            "Attock-2(PP-5)"
        ]

        variable = tk.StringVar(self)
        variable.set(OPTIONS[0])

        GListBox_541 = tk.OptionMenu(self, variable, *OPTIONS)
        GListBox_541["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        GListBox_541["font"] = ft
        GListBox_541["fg"] = "#333333"
        GListBox_541["justify"] = "center"

        GListBox_541.place(x=180, y=390, width=350, height=25)


        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Save"
        GButton_499["relief"] = "solid"
        GButton_499.place(x=180, y=440, width=80, height=25)
        GButton_499["command"] = self.GButton_499_command

        returnButton = tk.Button(self)
        returnButton["bg"] = "#DC4D41"
        ft = tkfont.Font(family='Times', size=10)
        returnButton["font"] = ft
        returnButton["fg"] = "#ffffff"
        returnButton["justify"] = "center"
        returnButton["text"] = "Logout"
        returnButton["relief"] = "solid"
        returnButton.place(x=440,y=440,width=90,height=25)
        returnButton["command"] = self.returnButton_command

        self.GLineEdit_27 = GLineEdit_191
        self.variable = variable
        self.GLineEdit_676 = GLineEdit_360
        self.GLineEdit_232 = GLineEdit_63
        self.GLineEdit_777 =partydropdown

    def returnButton_command(self):
        self.controller.show_frame("ElectionCommisionClass")


    def GButton_520_command(self):
        self.controller.show_frame("AddCandidateClass")


    def GButton_629_command(self):
        print("command")


    def GButton_737_command(self):
        self.controller.show_frame("ViewResultClass")


    def GButton_499_command(self):
        if len(self.GLineEdit_27.get()) == 0 or len(self.GLineEdit_676.get()) == 0 or len(
                self.GLineEdit_777.get()) == 0 or len(self.GLineEdit_232.get()) == 0:
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            name1 = self.GLineEdit_27.get()
            constituency = self.variable.get()
            cnic = self.GLineEdit_676.get()
            password1 = self.GLineEdit_232.get()
            phone1 = self.GLineEdit_777.get()
            exists = os.path.isfile("VotingData\PollingAgentData.csv")
            agentDetails = [str(name1), '', cnic, '', password1, '', phone1, '', constituency]
            col_names = ['Name', '', 'CNIC', '', 'Password', '', 'Phone', '', 'Constituency']
            PollingAgentAlreadyExist = False

            if exists:
                with open("VotingData\PollingAgentData.csv", "r", newline='') as f:
                    reader = csv.reader(f, delimiter=',', quotechar='"')
                    for line_num, content in enumerate(reader):
                        if content[2] == str(cnic):
                            PollingAgentAlreadyExist = True
                            break
                if not PollingAgentAlreadyExist:
                    with open("VotingData\PollingAgentData.csv", 'a+', newline='') as csvFile1:
                        writer = csv.writer(csvFile1)
                        writer.writerow(agentDetails)
                    csvFile1.close()
                    self.GLineEdit_27.delete(0, 'end')
                    self.GLineEdit_232.delete(0, 'end')
                    self.GLineEdit_676.delete(0, 'end')
                    self.GLineEdit_777.delete(0, 'end')

                    mess.showinfo("Success", "Agent Added Successfully")
                else:
                    mess.showinfo("Failed", "Agent's CNIC Already Exists")
                    print("Agent's CNIC Already Exists")


            else:

                with open("VotingData\PollingAgentData.csv", 'a+', newline='') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(col_names)
                    writer.writerow(agentDetails)
                csvFile1.close()



class ViewResultClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")


        GButton_520=tk.Button(self)
        GButton_520["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#ffffff"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Add Candidate"
        GButton_520.place(x=0,y=0,width=200,height=50)
        GButton_520["command"] = self.GButton_520_command

        GButton_629=tk.Button(self)
        GButton_629["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#ffffff"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Add Polling Agent"
        GButton_629.place(x=200,y=0,width=200,height=50)
        GButton_629["command"] = self.GButton_629_command

        GButton_737=tk.Button(self)
        GButton_737["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#000000"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "View Results"
        GButton_737.place(x=400,y=0,width=200,height=50)
        GButton_737["command"] = self.GButton_737_command

        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=60,width=600,height=40)
        tv = ttk.Treeview(self, height=15, columns=('Party', 'Votes'))

        # tv.column('Candidate Name', width=70)
        tv.column('Party', width=200)
        tv.column('Votes', width=160)

        # tv.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
        # tv.heading('#0', text='Candidate Name')

        tv.heading('Party', text='Party')
        tv.heading('Votes', text='Votes')
        scroll = ttk.Scrollbar(self, orient='vertical', command=tv.yview)
        # scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
        tv.configure(yscrollcommand=scroll.set)
        tv.place(x=20, y=120)
        from collections import Counter
        from operator import itemgetter
        exists = os.path.isfile("VotingData\AVotingData.csv")
        i = 0
        if exists:

            with open("VotingData\AVotingData.csv", 'r', newline='') as csvFile1:
                reader1 = csv.reader(csvFile1)
                id_counts = Counter(map(itemgetter(6), reader1))
                id_counts = dict(id_counts)
                print(id_counts)


                for key in id_counts:
                    i = i + 1
                    if (i > 1):
                        # if (i % 2 != 0):
                        # iidd = str(lines[4]) + '   '
                        tv.insert('', 0, text=i, values=(str(key), str(id_counts[key]), str()))

                        # tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[0]), str(lines[6])))
            csvFile1.close()



        returnButton = tk.Button(self)
        returnButton["bg"] = "#DC4D41"
        ft = tkfont.Font(family='Times', size=10)
        returnButton["font"] = ft
        returnButton["fg"] = "#ffffff"
        returnButton["justify"] = "center"
        returnButton["text"] = "Logout"
        returnButton["relief"] = "solid"
        returnButton.place(x=490, y=460, width=80, height=25)
        returnButton["command"] = self.returnButton_command

    def returnButton_command(self):
        self.controller.show_frame("ElectionCommisionClass")


    def GButton_520_command(self):
        self.controller.show_frame("AddCandidateClass")


    def GButton_629_command(self):
        self.controller.show_frame("AddPollingAgentClass")


    def GButton_737_command(self):
        print("command")


    def GButton_499_command(self):
        print("command")

class AddVoter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#ffffff")

        GButton_520=tk.Button(self)
        GButton_520["bg"] = "#d3cbcb"
        ft = tkfont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#ffffff"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Election Commission"
        GButton_520.place(x=0,y=0,width=200,height=50)
        GButton_520["command"] = self.GButton_520_command

        GButton_629=tk.Button(self)
        GButton_629["bg"] = "#ffffff"
        ft = tkfont.Font(family='Times',size=10)
        GButton_629["font"] = ft
        GButton_629["fg"] = "#000000"
        GButton_629["justify"] = "center"
        GButton_629["text"] = "Polling Agent"
        GButton_629.place(x=200,y=0,width=200,height=50)
        GButton_629["command"] = self.GButton_629_command

        GButton_737=tk.Button(self)
        GButton_737["bg"] = "#d0cdcd"
        ft = tkfont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#ffffff"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "Voter"
        GButton_737.place(x=400,y=0,width=200,height=50)
        GButton_737["command"] = self.GButton_737_command

        GLabel_711=tk.Label(self)
        GLabel_711["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=18)
        GLabel_711["font"] = ft
        GLabel_711["fg"] = "#ffffff"
        GLabel_711["justify"] = "center"
        GLabel_711["text"] = "E-voting System Using Facial Recognition"
        GLabel_711.place(x=0,y=60,width=600,height=40)

        nameLabel = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        nameLabel["font"] = ft
        nameLabel["fg"] = "#333333"
        nameLabel["bg"] = "#ffffff"

        nameLabel["justify"] = "center"
        nameLabel["text"] = "Name"
        nameLabel.place(x=50, y=110, width=100, height=25)

        nameEntry = tk.Entry(self)
        nameEntry["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        nameEntry["font"] = ft
        nameEntry["fg"] = "#333333"
        nameEntry["justify"] = "center"
        nameEntry["text"] = ""
        nameEntry["relief"] = "solid"
        nameEntry.place(x=180, y=110, width=350, height=25)


        GLabel_705=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_705["font"] = ft
        GLabel_705["fg"] = "#333333"
        GLabel_705["bg"] = "#ffffff"
        GLabel_705["justify"] = "center"
        GLabel_705["text"] = "Phone #"
        GLabel_705.place(x=50,y=160,width=100,height=25)


        GLabel_PhoneFormate=tk.Label(self)
        ft = tkfont.Font(family='Times',size=10)
        GLabel_PhoneFormate["borderwidth"] = "1px"
        GLabel_PhoneFormate["font"] = ft
        GLabel_PhoneFormate["fg"] = "#333333"
        GLabel_PhoneFormate["bg"] = "#ffffff"
        GLabel_PhoneFormate["justify"] = "center"
        GLabel_PhoneFormate["text"] = "+92"
        GLabel_PhoneFormate.place(x=180,y=160,width=50,height=25)

        GLineEdit_191=tk.Entry(self)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "center"
        GLineEdit_191["text"] = ""
        GLineEdit_191["relief"] = "solid"
        GLineEdit_191.place(x=230, y=160, width=300, height=25)

        GLabel_827=tk.Label(self)
        ft = tkfont.Font(family='Times',size=18)
        GLabel_827["font"] = ft
        GLabel_827["fg"] = "#333333"
        GLabel_827["bg"] = "#ffffff"

        GLabel_827["justify"] = "center"
        GLabel_827["text"] = "CNIC"
        GLabel_827.place(x=50,y=210,width=100,height=25)

        GLineEdit_360=tk.Entry(self)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"

        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = ""
        GLineEdit_360["relief"] = "solid"

        GLineEdit_360.place(x=180,y=210,width=350,height=25)





        candidate = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        candidate["font"] = ft
        candidate["fg"] = "#333333"
        candidate["bg"] = "#ffffff"

        candidate["justify"] = "center"
        candidate["text"] = "Constituency"
        candidate.place(x=40,y=260,width=130,height=25)

        OPTIONS = [
            "Attock-1(PP-1)",
            "Attock-1(PP-2)",
            "Attock-2(PP-3)",
            "Attock-2(PP-4)",
            "Attock-2(PP-5)"
        ]

        variable = tk.StringVar(self)
        variable.set(OPTIONS[0])

        candidatedropdown = tk.OptionMenu(self, variable, *OPTIONS)
        candidatedropdown["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        candidatedropdown["font"] = ft
        candidatedropdown["fg"] = "#333333"
        candidatedropdown["justify"] = "center"
        candidatedropdown["text"] = ""
        candidatedropdown["relief"] = "solid"

        candidatedropdown.place(x=180,y=260,width=350,height=25)
        passWord = tk.Label(self)
        ft = tkfont.Font(family='Times', size=18)
        passWord["font"] = ft
        passWord["fg"] = "#333333"
        passWord["bg"] = "#ffffff"

        passWord["justify"] = "center"
        passWord["text"] = "Password"
        passWord.place(x=40,y=310,width=130,height=25)

        passEntry = tk.Entry(self)
        passEntry["borderwidth"] = "1px"
        ft = tkfont.Font(family='Times', size=10)
        passEntry["font"] = ft
        passEntry["fg"] = "#333333"

        passEntry["justify"] = "center"
        passEntry["text"] = ""
        passEntry["relief"] = "solid"
        passEntry.place(x=180,y=310,width=350,height=25)


        # profileStatus = tk.Label(self)
        # ft = tkfont.Font(family='Times', size=18)
        # profileStatus["font"] = ft
        # profileStatus["fg"] = "#333333"
        # profileStatus["bg"] = "#ffffff"
        #
        # profileStatus["justify"] = "center"
        # profileStatus["text"] = "1) Take Photo>>> 2) Save Profile"
        # profileStatus.place(x=130,y=340,width=440,height=20)

        takeImage = tk.Button(self)
        takeImage["bg"] = "#22B0BD"
        ft = tkfont.Font(family='Times', size=10)
        takeImage["font"] = ft
        takeImage["fg"] = "#ffffff"
        takeImage["justify"] = "center"
        takeImage["text"] = "Take Pictures"
        takeImage["relief"] = "solid"
        takeImage.place(x=180, y=370, width=90, height=25)
        takeImage["command"] = self.takeImage_command



        GButton_499=tk.Button(self)
        GButton_499["bg"] = "#3eb45f"
        ft = tkfont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#ffffff"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Save Profile"
        GButton_499["relief"] = "solid"
        GButton_499.place(x=280,y=370,width=90,height=25)
        GButton_499["command"] = self.GButton_499_command

        returnButton = tk.Button(self)
        returnButton["bg"] = "#DD4F42"
        ft = tkfont.Font(family='Times', size=10)
        returnButton["font"] = ft
        returnButton["fg"] = "#ffffff"
        returnButton["justify"] = "center"
        returnButton["text"] = "Logout"
        returnButton["relief"] = "solid"
        returnButton.place(x=440, y=370, width=90, height=25)

        self.txt = GLineEdit_191
        # self.message = message
        # self.message1 = profileStatus
        self.txt2 = GLineEdit_360
        self.constituency = variable
        self.name=nameEntry
        self.passWord=passEntry
    def getImagesAndLabels(self,path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # create empth face list
        faces = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(ID)
        return faces, Ids

    def TrainImages(self):
        self.check_haarcascadefile()
        self.assure_path_exists("TrainingImageLabel/")
        columns = ['SERIAL NO.', '', 'ID', '', 'NAME', '', 'CONSTITUENCY','','VOTERNAME','','PASSWORD']
        self.assure_path_exists("VoterDetails/")
        self.assure_path_exists("TrainingImage/")
        serial = 0
        exists = os.path.isfile("VoterDetails\VoterDetails.csv")
        if exists:
            with open("VoterDetails\VoterDetails.csv", 'r', newline='') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
        else:
            with open("VoterDetails\VoterDetails.csv", 'a+', newline='') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()
        Id = (self.txt.get())
        name = (self.txt2.get())
        con = self.constituency.get()
        voterName=self.name.get()
        passWord=self.passWord.get()

        if (name.isnumeric()):

            harcascadePath = "haarcascade_frontalface_default.xml"



            row = [serial, '', Id, '', name, '', con,'',voterName,'',passWord]
            with open('VoterDetails\VoterDetails.csv', 'a+', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            self.txt.delete(0,'end')
            self.txt2.delete(0,'end')
            self.passWord.delete(0,'end')
            self.name.delete(0,'end')
        else:
            if (name.isnumeric() == False):
                res = "Enter Correct name"
                mess.showwarning(res)
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, ID = self.getImagesAndLabels("TrainingImage")
        try:
            recognizer.train(faces, np.array(ID))
        except:
            mess._show(title='No Registrations', message='Please Register someone first!!!')
            return
        recognizer.save("TrainingImageLabel\Trainner.yml")
        res = "Profile Saved Successfully"

        self.message1.configure(text=res)
        #self.message.configure(text='Total Registrations till now  : ' + str(ID[0]))

    def assure_path_exists(self,path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    def check_haarcascadefile(self):
        exists = os.path.isfile("haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            mess._show(title='Some file missing', message='Please contact us for help')
            # window.destroy()

    def TakeImages(self):
        self.check_haarcascadefile()
        columns = ['SERIAL NO.', '', 'ID', '', 'NAME', '', 'CONSTITUENCY','','VOTERNAME','','PASSWORD']
        self.assure_path_exists("VoterDetails/")
        self.assure_path_exists("TrainingImage/")
        serial = 0

        exists = os.path.isfile("VoterDetails\VoterDetails.csv")
        if exists:
            with open("VoterDetails\VoterDetails.csv", 'r', newline='') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
        else:
            with open("VoterDetails\VoterDetails.csv", 'a+', newline='') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()
        name = (self.txt2.get())
        con=self.constituency.get()
        voterName = self.name.get()
        passWord = self.passWord.get()

        name = (self.txt2.get())
        Id = (self.txt.get())

        if ((name.isnumeric()) ):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    # display the frame
                    cv2.imshow('Taking Images', img)
                # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 30
                elif sampleNum > 30:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Images Taken for ID : " + Id
            '''
            #row = [serial, '', Id, '', name, '', con,'',voterName,'',passWord]
            with open('VoterDetails\VoterDetails.csv', 'a+', newline='') as csvFile:
                print("")
                #writer = csv.writer(csvFile)
                #writer.writerow(row)
            csvFile.close()
           '''
            self.message1.configure(text=res)
        else:
            if (name.isnumeric() == False):
                res = "Enter Correct name"
                mess.showwarning(res,"Incorrect Name")


    def psw(self):
        self.otp = random.randint(1000, 9999)
        print("Your OTP is - ", self.otp)
        # Your Account Sid and Auth Token from twilio.com/console
        # DANGER! This is insecure. See http://twil.io/secure

        account_sid = 'AC0a63a25263fb79ab594d8fe7c09f5fea'
        auth_token = '81d1495c80c63926704f50d06c153e0e'


        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body='Your Secure Device OTP is - ' + str(self.otp) + ' ',
            from_='+18316619698',
            to=str(self.txt.get())
        )

        self.assure_path_exists("TrainingImageLabel/")
        exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
        if exists1:
            tf = open("TrainingImageLabel\psd.txt", "r")
            key = tf.read()
        else:
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='No Password Entered', message='Password not set!! Please try again')
            else:
                tf = open("TrainingImageLabel\psd.txt", "w")
                tf.write(new_pas)
                mess._show(title='Password Registered', message='New password was registered successfully!!')
                return
        password = tsd.askstring('OTP', 'Enter OTP', show='*')
        print(password)
        otp=self.otp
        print(otp)
        if str(password) == str(otp):
            self.TrainImages()
        elif (password == None):
            pass
        else:
            mess._show(title='Wrong OTP', message='You have entered wrong OTP')
    def takeImage_command(self):
        self.TakeImages()

    def GButton_520_command(self):
        self.controller.show_frame("ElectionCommisionClass")


    def GButton_629_command(self):
        self.controller.show_frame("PollingAgentClass")



    def GButton_737_command(self):
        self.controller.show_frame("VoterClass")




    def GButton_499_command(self):
        if len(self.txt.get()) == 0 or len(self.txt2.get()) == 0 :
            mess.showwarning("Incomplete Data", "Please Fill all Details")
        else:
            self.psw()





if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()