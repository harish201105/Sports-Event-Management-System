import turtle
import time
import random
import math
from tkinter import *
import mysql.connector

turtle.bgcolor('light blue')
turtle.color('brown')
style=('Times new roman','35','bold')
turtle.write('_SPORTS EVENT MANAGEMENT SYSTEM_',font=style, align='center')
turtle.hideturtle()
time.sleep(5)
# Object tr for turtle    
tr = turtle.Turtle()
 
# Set thickness for each ring
tr.pensize(5)
tr.color("blue")
tr.penup()
tr.goto(-110, -25)
tr.pendown()
tr.circle(45)
tr.color("black")
tr.penup()
tr.goto(0, -25)
tr.pendown()
tr.circle(45)
tr.color("red")
tr.penup()
tr.goto(110, -25)
tr.pendown()
tr.circle(45)
tr.color("yellow")
tr.penup()
tr.goto(-55, -75)
tr.pendown()
tr.circle(45)
tr.color("green")
tr.penup()
tr.goto(55, -75)
tr.pendown()
tr.circle(45)

# MYSQL
con = mysql.connector.connect(host='localhost', user='root', password='YOUR PASSWORD', database='sports')
cur = con.cursor()
print('*****WELCOME TO SPORTZEVENTO*****')
print()
print('Press 1 or 2')
print('1.Organizer')
print('2.Player')
user = int(input('Enter 1 or 2:'))

# User defined functions for organizer
def Register():
    name = input('Enter your name:')
    emailid = input('Enter your email id:')
    passwd = input('Enter your password:')
    phoneno = int(input('Enter your phone number:'))

    Query = "INSERT INTO myorg VALUES('{}', '{}', '{}', {})".format(name, emailid, passwd, phoneno)
    cur.execute(Query)
    con.commit()
    print('Your account has been created successfully!')

def Login():
    Name = input('Enter your name:')
    passwd = input('Enter your password:')
    Query = "SELECT * FROM myorg WHERE NAME='{}' AND Passwd='{}'".format(Name, passwd)
    cur.execute(Query)
    data = cur.fetchone()
    if data is not None:
        print('You have logged into your account successfully!')
        print('1.Create Tournament')
        print('2.Display Participants')
        print('3.Knockout')
        print('4.League')
        print('5.Round_Robin')
    else:
        print('Enter Valid details')

#Pairing mode for organiser
#Complementary
#T denotes the teams playing
#n denotes the round number
#L denotes the lost team

def DisplayParticipants():
    eventname=input('Your eventname to select the participant details:')
    Query="SELECT * FROM pdetails where Eventname='{}'".format(eventname)
    cur.execute(Query)
    data=cur.fetchall()
    for i in data:
        print(i)
    print('No.of participants registered so far in your event is',cur.rowcount)

def Knockout(T,n):
    if len(T)%2!=0:
        T.append('BYE')
    T1=list(T)
    x=math.floor(len(T)/2)
    for i in range(math.floor(len(T)/2)):
        print('Round',n)
        print(T[i],'vs',T[x])
        x=x+1
        L=input('The knocked out team is:')
        T1.remove(L)
    
    print('The qualified teams for next round are',T1)
    n=1
    if len(T1)!=1:
        n=n+1
        Knockout(T1,n)
    if len(T1)==1:
        print('The winner is',T1[0])
        
def League():
    teams = eval(input('Enter team_names or player_names to pair:'))

    if len(teams)%2!=0:
        teams.append('Bye')
    n=len(teams)
    matchs = []
    fixtures = []
    return_matchs = []

    for fixture in range(1, n):
        for i in range(n//2):
            matchs.append((teams[i], teams[n - 1 - i]))
            return_matchs.append((teams[n - 1 - i], teams[i]))
        teams.insert(1,teams.pop())
        fixtures.insert(len(fixtures)//2, matchs)
        fixtures.append(return_matchs)
        matchs = []
        return_matchs = []
    n=1#Round no
    for fixture in fixtures:
        print('Round',n)
        n=n+1
        print(fixture)

        

def Roundrobin():
    teams = eval(input('Enter team_names or player_names to pair:'))
    if len(teams)%2!=0:
       teams.append('Bye')
    n=len(teams)
    matchs = []
    fixtures = []

    for fixture in range(1, n):
        for i in range(n//2):
            matchs.append((teams[i], teams[n - 1 - i]))
        teams.insert(1,teams.pop())
        fixtures.insert(len(fixtures)//2, matchs)
        matchs = []   
    n=1 #Round no
    for fixture in fixtures:
        print('Round',n)
        n=n+1
        print(fixture)

if user == 1:
    print('1.Register if a new organizer')
    print('2.Login')
    orgchoice = int(input('Enter your choice:'))

    if orgchoice==1:
        Register()
                                                                                                                                                                                                                                                                                                                                                                                                                                   
    if orgchoice==2:
       Login()
       create=int(input('Enter your choice:'))
       if create==1:
           eventname=input('Enter event title:')
           sportsname=input('Enter sports name:')                                                                          
           sponsorsname=input('Enter sponsors name:')
           eventdate=input('Enter the event date:')
           location=input('Enter the location:')
           Query="INSERT INTO eventdetails VALUES('{}','{}','{}','{}','{}')".format(eventname,sportsname, sponsorsname,eventdate, location)

           cur.execute(Query)                                                        
           con.commit()
           print('You have created your event successfully!')

       if create==2:
            DisplayParticipants()
       if create==3:
            T=eval(input('Enter teams to be paired'))
            Knockout(T,1)    
       if create==4:
            League()
       if create==5:
            Roundrobin()
        
#Players form - Tkinter
base = Tk()  
base.geometry("500x500")  
base.title("Players Registration form")
base.configure(bg='aquamarine')
def Player():
    global L
    L=[]
    name=StringVar() 
    lb1= Label(base, text="Enter Name", width=10,bg='white',fg='black', font=("arial",12))
    lb1.place(x=20, y=120)
    en1= Entry(base,textvariable=name)
    def P_name():
        global Name
        Name=name.get()
        return Name 
    en1.place(x=200, y=120)
    age=IntVar()
    lb3= Label(base, text="Player Age",bg='white',fg='black', width=10, font=("arial",12))  

    lb3.place(x=19, y=160)  
    en3= Entry(base,textvariable=age)

    def P_Age():
        global Age 
        Age= age.get() 
        return Age
    en3.place(x=200, y=160)
    cno=IntVar() 
    lb4= Label(base, text="Contact Number",bg='white',fg='black',width=13,font=("arial",12))  
    lb4.place(x=19, y=200)  
    en4= Entry(base,textvariable=cno)

    def P_Contactno():
        global Contactno
        Contactno= cno.get()
        return Contactno
    en4.place(x=200, y=200)  
    lb5= Label(base, text="Select Gender",bg='white',fg='black', width=15, font=("arial",12))  
    lb5.place(x=5, y=240)  
    vars = IntVar()

    def P_Gender():
        global Gender
        Gender= vars.get()
        return Gender
    Radiobutton(base, text="Male", padx=5,variable=vars, value=1).place(x=180, y=240)  
    Radiobutton (base, text="Female", padx =10, variable=vars, value=2).place(x=240,y=240) 
    Radiobutton (base, text="others", padx=15, variable=vars, value=3).place(x=310,y=240)  

    list_of_Skill_Division = ("Beginner", "Intermediate", "Advanced","Expert")  
    cv = StringVar()  
    drplist= OptionMenu(base, cv, *list_of_Skill_Division)  

    drplist.config(width=15)  
    cv.set("Beginner")
    lb2= Label(base, text="Skill Division",bg='white',fg='black', width=13,font=("arial",12))  
    lb2.place(x=14,y=280)  
    drplist.place(x=200, y=275)  

    districtname=StringVar()  
    lb6= Label(base, text="District Name",bg='white',fg='black',width=13,font=("arial",12))  
    lb6.place(x=19, y=320)
    def P_Districtname():
        global Districtname 
        Districtname =districtname.get()
        return Districtname
    en6= Entry(base,textvariable=districtname)  
    en6.place(x=200, y=320)  

    emailid=StringVar()  
    lb7= Label(base, text="Email Id",bg='white',fg='black',width=15,font=("arial",12))  
    lb7.place(x=19, y=360)
    def P_Emailid():
        global Emailid 
        Emailid=emailid.get()
        return Emailid
    en7=Entry(base,textvariable=emailid)  
    en7.place(x=200, y=360)

    eventname=StringVar()  
    lb8= Label(base, text="Event Name",bg='white',fg='black',width=15,font=("arial",12))  
    lb8.place(x=20, y=400)
    def P_Eventname():
        global Eventname
        Eventname=eventname.get()
        return Eventname
    en8=Entry(base,textvariable=eventname)  
    en8.place(x=200, y=400)
  
    # import messagebox from tkinter module
    import tkinter.messagebox
  
    # Create a messagebox showinfo

    def Register():
          tkinter.messagebox.showinfo("Welcome to Sports Event", "Registered successfully")
    
    # Create a Buttons
    Button1 = Button(base, text="Register", command=Register,pady=10)
    Button1.pack(side=BOTTOM)

    base.mainloop()
    
    #Jersey_Number
    J= random.randint(1,200)
    L.append(J)
           
    P_name()
    L.append(Name)
    del name

    P_Age()
    L.append(Age)
    del age

    P_Contactno()
    L.append(Contactno)
    del contactno

    P_Districtname()
    L.append(Districtname)
    del districtname


    P_Emailid()
    L.append(Emailid)
    del emailid

    P_Eventname()
    L.append(Eventname)
    del eventname

    print('The given details are',L)
    Query="INSERT INTO pdetails  VALUES({},'{}',{},{},'{}','{}','{}')".format(j,name,age,contactno,districtname,emailid,eventname)
    cur.execute(Query)                                                        
    con.commit()
    print('Your registration is completed successfully')
    print('The brief details will be sent in your email id')
    
if user==2:
    Q="SELECT*FROM EVENTDETAILS"
    cur.execute(Q)
    print('***DASHBOARD***')
    print()
    events=cur.fetchall()
    for i in range(len(events)):
        print('Tournament No',i+1)
        print('EventName:',events[i][0])
        print('SportsName:',events[i][1])
        print('SponsorsName:',events[i][2])
        print('Date:',events[i][3])
        print('Location:',events[i][4])
        print()
    Player()

