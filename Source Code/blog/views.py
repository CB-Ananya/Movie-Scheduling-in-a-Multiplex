
from re import I
from turtle import Screen
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from . import fpsd_project_updated as project
from . import TTvisualgen as format
import csv
import pandas as pd
import json

# Create your views here.

global D ,K,Screen_Info,k,userid
global l
D=[];Screen_Info=[];MovieNames=[];RelDate=[];Bdg=[];Lng=[];Aud=[];IntScore=[];l=[];k=[]

def screens_reset(request):
    with open("blog\JSON_FILE\Main.json","r") as f:
        data=json.load(f)
        #Screen_Facility_Information=data[userid][2]
    data[userid].pop(2)
    with open("blog\JSON_FILE\Main.json","w") as f:
        json.dump(data,f)
    d=dict(request.POST)
    print(d)
    Screen_Info.append(d)
    print(Screen_Info) 
    
    for i in Screen_Info:
        if i!={}:
            if i['ScreenName'][0] not in k:
                k.append(i['ScreenName'][0])

    
    return render(request,'blog/Screen_input.html',{'k':k})

def screens(request):
    
    d=dict(request.POST)
    print(d)
    Screen_Info.append(d)
    print(Screen_Info) 
    
    for i in Screen_Info:
        if i!={}:
            if i['ScreenName'][0] not in k:
                k.append(i['ScreenName'][0])

    
    return render(request,'blog/Screen_input.html',{'k':k})

def MovieDetails(request):
    
    dic=dict(request.POST)
    print(request.POST)
    D.append(dic)
    print(D) #D is a list of dictionaries(input)
    
    for i in D:
        if i!={}:
            if i['NameOfMovie'][0] not in l:
                l.append(i['NameOfMovie'][0])

    return render(request,'blog/Movie_form.html',{'l':l})

def output(request):

    i=0
    while i<len(D):
        if D[i]=={}:
            D.pop(i)
        else:
            i=i+1
            

    Movie_Facility_Information={}
    for i in D:
        Movie_Facility_Information[i['NameOfMovie'][0]]=[1,0,0,0]
        MovieNames.append(i['NameOfMovie'][0])
        Lng.append(i['Language'][0])
        RelDate.append(i['ReleaseDate'][0])
        Bdg.append(float(i['Budget'][0]))
        Aud.append(i['AudienceType'][0])
        if 'Facilities' in i:
            if i['Facilities'][0]=='IMAX':
                Movie_Facility_Information[i['NameOfMovie'][0]][2]=1
            elif i['Facilities'][0]=='3D':
                Movie_Facility_Information[i['NameOfMovie'][0]][3]=1
            elif i['Facilities'][0]=='DOLBY ATMOS' :
                Movie_Facility_Information[i['NameOfMovie'][0]][1]=1

        
    Movie_Information={}
    IntScore=list(project.TrendsScore(MovieNames).values())
        
    """HighestBdg = max(Bdg)
    for i in range(len(MovieNames)):
            MovieScore[MovieNames[i]]=project.TotalScore(MovieNames[i], RelDate[i], Lng[i], Bdg[i], Aud[i], IntScore[i], HighestBdg)"""

    #Movies={"Gargi":[[1,0,0,0],'2022-07-01','Tamil',40000000,'U'],"Vikram":[[1,0,0,0],'2022-06-20','Tamil',20000000,'U/A'], "Top Gun Maverick":[[1,1,0,0],'2022-07-07','English',10000000,'U/A'], "Legend": [[1,1,0,0], '2022-08-01', 'Tamil', 10000000, 'U'], "Thor: Love and Thunder":[[1,0,1,0],'2022-06-20','English',30000000,'U'],  "Minions": [[1,0,0,1], '2022-07-20', 'English', 12000000, 'U']}
    Movie_Information={}
    for i in range(len(MovieNames)):
        Movie_Information[MovieNames[i]]=[Movie_Facility_Information[MovieNames[i]],RelDate[i],Lng[i],Bdg[i],Aud[i]]

    with open("blog\JSON_FILE\Main.json","r") as f:
        data=json.load(f)
        Screen_Facility_Information=data[userid][2]
        #Screenings=list(ScreenScore.keys())
        #TotalScreens=len(Screenings)

    """MaxNoOfShows = project.TotalNoOfShows(MovieNames, list(MovieScore.values()), TotalScreens)
    TimeTables=project.BruteTimeTables(Screenings,MovieNames,MaxNoOfShows)
    Bt=project.Maximisation(TimeTables, ScreenScore, MovieScore)
    print(Bt)"""

    print(Movie_Information)
    BestTT= project.ScreensAndMoviesToBestTT(Screen_Facility_Information, Movie_Information, IntScore)
    print(BestTT)
    screens=list(Screen_Facility_Information.keys())
    Slots = ['08:00am', '12:00pm', '04:00pm', '09:00pm']
    OpTT=format.VisualTT(BestTT,screens,Slots)
  
    return render (request, 'blog/OP.html',{'Slots':Slots,'OpTT':OpTT})

def login(request):
    global userid
    login_details=dict(request.POST)
    print(login_details)
    if login_details!={}:
        userid=login_details['username'][0]
        pwd=login_details['password'][0]

        with open("blog\JSON_FILE\Main.json","r") as f:
            data=json.load(f)

        print(data)
        print(type(userid))
        #data=list(data.keys())       
        if userid in data and pwd==data[userid][1]:
                messages.success(request,'Successful Login')
                return redirect('/profile/')
        elif userid in data and pwd!=data[userid][1]:
                messages.error(request,'Incorrect Password.Try Again')
                return redirect('/login/')
        else:
                messages.error(request,'Account Does Not Exist . Create a New Account')
                return redirect('/login/')
                           

    return render (request, 'blog/LOGIN.html')

def signup(request):
    global userid
    signup_details=dict(request.POST)
    print(signup_details)

    if signup_details!={}:
        name=signup_details["Name"][0]
        pwd=signup_details['password']
        con_pwd=signup_details['confirmpassword']
        if pwd != con_pwd:
            
            
            messages.error(request,'ERROR: The passwords did not match. Try again.')
            return redirect('/signup/')
    
        else: 
            with open("blog\JSON_FILE\Main.json","r") as f:
                data = json.load(f)
                userid=str(len(data)+1)
                l=[name,pwd[0]]
                data[userid]=l
            

            with open("blog\JSON_FILE\Main.json","w") as f:
                json.dump(data,f)

            messages.success(request,f'Account Created Successfully! - Username:{userid}')
            return redirect('/screens/')
        
    return render (request, 'blog/SIGNUP.html')

def profile(request):

    with open("blog\JSON_FILE\Main.json","r") as f:
        data=json.load(f)
    Slots = ['08:00am', '12:00pm', '04:00pm', '09:00pm']
    if len(data[userid])<3 :    
        Screen_Facilities={}
        Slots = ['08:00am', '12:00pm', '04:00pm', '09:00pm']
        #k is the list of screen numbers obtained from user 
        if k!=[]:

            Screens=k
            for i in range(len(Screens)):
                if int(Screens[i])<=9:
                    Screens[i]='Scr0'+k[i]
                else:
                    Screens[i]='Scr'+k[i]
        i=0
        while i< (len(Screen_Info)):
            if Screen_Info[i]=={}:
                Screen_Info.pop(i)
            else: i=i+1
        print(Screen_Info)
        i=0
        for j in Screen_Info:
            print(j)
            if j!={}:
                print(i)
                Screen_Facilities[Screens[i]]=[1,0,0,0,0,0,0,0]
                if 'Facilities' in j:
                    if j['Facilities'][0]=='IMAX':
                        Screen_Facilities[Screens[i]][2]=1
                    elif j['Facilities'][0]=='3D':
                        Screen_Facilities[Screens[i]][3]=1
                    elif j['Facilities'][0]=='DOLBY ATMOS' :
                        Screen_Facilities[Screens[i]][1]=1
                    
                
                if  '12 AM - 3 PM' in j:
                    Screen_Facilities[Screens[i]][5]=1
                if  '8 AM - 1 AM' in j:
                    Screen_Facilities[Screens[i]][4]=1
                if  '4 PM - 7 PM' in j:
                    Screen_Facilities[Screens[i]][6]=1
                if  '9 PM - 12 PM' in j:
                    Screen_Facilities[Screens[i]][7]=1

                i=i+1
    
        with open("blog\JSON_FILE\Main.json","r") as f:
            data = json.load(f)
            print("@@@@",data,userid,type(userid))
            data[userid]=data[userid]+[Screen_Facilities]
            Name=data[userid][0]
        
        with open("blog\JSON_FILE\Main.json","w") as f:
            json.dump(data,f)

    else:
        Screen_Facilities=[]
        with open("blog\JSON_FILE\Main.json","r") as f:
            data = json.load(f)
            print("@#@",data)
        Screen_Facilities=data[userid][2]
        Name=data[userid][0]

        #Screenings=list(Screen_Information.keys())
        #TotalScreens=len(Screenings)
   
    Slots=['2D','Dolby Atmos','Imax','3D']+Slots
    TotalNoOfScreens=len(data[userid][2])
    ImaxScreenings=ThreeDScreenings=DolbyScreenings=TwoDScreenings=0
    
    for i in Screen_Facilities:
        #DOLBY SCREENS
        
        if Screen_Facilities[i][1]==1:
            DolbyScreenings=DolbyScreenings+Screen_Facilities[i][4:].count(1)
        elif Screen_Facilities[i][2]==1:
            ImaxScreenings=ImaxScreenings+Screen_Facilities[i][4:].count(1)
        elif Screen_Facilities[i][3]:
            ThreeDScreenings=ThreeDScreenings+Screen_Facilities[i][4:].count(1)
        else:
            TwoDScreenings=TwoDScreenings+Screen_Facilities[i][4:].count(1)
        

    print(Screen_Facilities)    

    return render(request,'blog/profile.html',{'TwoDScreenings':TwoDScreenings,'DolbyScreenings':DolbyScreenings,'ImaxScreenings':ImaxScreenings,'ThreeDScreenings':ThreeDScreenings, 'TotalNoOfScreens':TotalNoOfScreens,'Slots':Slots,'Screen_Facilities':Screen_Facilities,'Name':Name})