# -*- coding: utf-8 -*-
"""FullBackend_OneModule.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VWuK-0s6kzYSSH37BOTuH83EgL41FmZj
"""

from pytrends.request import TrendReq as UTrendReq
GET_METHOD='get'

import requests

headers = {
    'authority': 'trends.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__utma=10102256.40848976.1660402253.1660402253.1660402253.1; __utmc=10102256; __utmz=10102256.1660402253.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=10102256.4.9.1660402268348; SID=Mwg-FN0s5Oun4gQ2EZO1L7ofBhpV62T4d2pM0pxVJJ9UfLP8tSMUdMB6ePOEk8tl_LV2HQ.; __Secure-1PSID=Mwg-FN0s5Oun4gQ2EZO1L7ofBhpV62T4d2pM0pxVJJ9UfLP86C-k6Xm05-IwVvvfWK_lfA.; __Secure-3PSID=Mwg-FN0s5Oun4gQ2EZO1L7ofBhpV62T4d2pM0pxVJJ9UfLP8zzId3CBdQBWPRI4R452l9g.; HSID=ANOClQDqHzrhuY-kw; SSID=AR_aTs1-oNptJagV8; APISID=zBdk6oPIM7uvqE_j/AOoeNgMlyK4abiv-S; SAPISID=c00acsSfNh4-xFmT/A0bbyAZSLW1PoQXig; __Secure-1PAPISID=c00acsSfNh4-xFmT/A0bbyAZSLW1PoQXig; __Secure-3PAPISID=c00acsSfNh4-xFmT/A0bbyAZSLW1PoQXig; AEC=AakniGNilmc5jwvK3Ym_Os53Bagg7MT8Vxu499ovz2dGELQHtMfv4DtNCd0; NID=511=qeQ4Vpe0PPCWhPM82iNIYH-Ro9sY7vV1pliT6Gg-bc5sX_095cPpcCR1tWZKIiXlP3yDb0orr_TFE2qdGTCZik-JqgyOkJlQ-rUVsc4-na6xXNv4J185nkdeolXtRR71SpaAr6skQSUge0Ucu4BSPcJ-a1LEophjqv_tkETKvU_pOcrCJydQfAGrY8dvbRPVubvBZRUg0YJwG167IYhPAhCIehqh9uGWS6wVx0l-9H7wupFJhNovjIOf6Vvqp8R3; 1P_JAR=2022-08-13-14; SIDCC=AEf-XMSbmldjdLosPSGkYgN_GU1Tft-2i3qC8l2othBebul3s7arTe44ch8cGtK57U8xsvyxSYY; __Secure-1PSIDCC=AEf-XMQLxh-4nobBF9fyRxybHS2-arCl0wzVysMPyULXmSH-JW5CIls1miEojmur1WzlbRlkYQ; __Secure-3PSIDCC=AEf-XMQETfNb31ml5OsMDRZky8kOxvCo-GftzR9J8C4mWl-t4fONAJ5vkrr6CanMGUl9pFmk3zs',
    'referer': 'https://trends.google.com/trends/?geo=IN',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-client-data': 'CKK1yQEIjLbJAQiitskBCMG2yQEIqZ3KAQiWjcsBCJOhywEI/KrMAQi7tMwBCOq7zAEIyrzMAQjcwMwBCJvBzAEIssHMAQjFwcwBCNfBzAEI3MTMAQjfxMwBCNfGzAEInMnMAQjjy8wBCLHMzAE=',
}


class TrendReq(UTrendReq):
    def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
        return super()._get_data(url, method=GET_METHOD, trim_chars=trim_chars, headers=headers, **kwargs)

#from pytrends.request import TrendReq
from datetime import date
from datetime import datetime
import time
from sympy.utilities.iterables import multiset_permutations
import numpy as np
import math

def ScreensAndMoviesToBestTT(Screens, Movies, IntScore):

    def TotalScore(NameOfMovie, RelDate, Lng, Bdg, Aud, IntScore, HighestBdg):
      NormBdg = (Bdg /HighestBdg)*30
      Today = date.today()
      Interest =0
      if Lng == 'Tamil':
          Interest=Interest+10
      elif Lng == 'English':
          Interest=Interest+9
      elif Lng == 'Hindi':
          Interest=Interest+8
      elif Lng == 'Telugu':
          Interest=Interest+7
      elif Lng == 'Malayalam':
          Interest=Interest+6.5
      else:
          Interest=Interest+5

      RelDate = date(int(RelDate[0:4]), int(RelDate[5:7]), int(RelDate[8:10]))
        
      Difference = Today - RelDate
      if (Difference.days) < 7:
          Interest=Interest+10
      elif (Difference.days) < 14:
          Interest=Interest+7
      elif (Difference.days) < 21:
          Interest=Interest+5
      else:
          Interest=Interest+2

      if (Aud=='U' or Aud=='U/A'):
          Interest=Interest+20
      else:
          Interest=Interest+10


      Interest=Interest+IntScore
      TotalScore= (Interest+NormBdg)/10

      return round(TotalScore, 4)


    def TotalNoOfShows(MovieNames, Scores, TotalScreens):
      sum_of_scores= sum(Scores)
      ratio_factor = TotalScreens/sum_of_scores
      MaxNoOfShows=[]
      for j in range(len(MovieNames)):
          MaxNoOfShows.append(round(Scores[j]*ratio_factor))
      ###
      
      if sum(MaxNoOfShows) > TotalScreens:
        Scores_sorted = sorted(Scores)
        for i in Scores_sorted:
          minimum=Scores.index(i)
          if MaxNoOfShows[minimum]!=0:
            MaxNoOfShows[minimum]=MaxNoOfShows[minimum]-1
            break
      elif sum(MaxNoOfShows) < TotalScreens:
          maximum=Scores.index(max(Scores))
          MaxNoOfShows[maximum]=MaxNoOfShows[maximum]+1
      
      ###
      return MaxNoOfShows

    from itertools import product

    def Maximisation(TimeTables, ScreenScore, MovieScore):
      #start = time.process_time()
      BestTimeTable=dict()
      BestScore=1
      for i in TimeTables:
        s=0
        for screening,movie in i.items():
          s=s+MovieScore[movie]*ScreenScore[screening]
        if s>BestScore:
          BestScore=s
          BestTimeTable=i
      #print("Maximization Time:",time.process_time() - start)
      return(BestTimeTable)
      


    def NewBruteTimeTables(Slots, Movies, MaxNoOfShows):
      start = time.process_time()
      List_freq = []
      import itertools
      for i in range(len(Movies)):
        for j in range(MaxNoOfShows[i]):
          List_freq.append(Movies[i])

      List_freq_arr=np.array(List_freq)
      ListOfLists = list(multiset_permutations(List_freq_arr))

      TimeTables=[]

      for OneTT in ListOfLists:
        d={}
        for j in range(len(Slots)):
          d[Slots[j]] = OneTT[j]
        TimeTables.append(d)

      return TimeTables


      


    def GenerateSlots(Screens):
      
      #This is a dict with the scr name as key (without timing) 
      #and value is it's score based on the features of the screen ALONE. (irrespective of timing)
      #structure:
      #{'Scr01' : 8, 'Scr02': 6, 'Scr03': 3...}

      Screens_Name_Score = {}
      for Names in Screens:
        if Screens[Names][0:4]==[1,0,0,1]:  #if it's a 3D screen
          ScoreForName=10
        elif Screens[Names][0:4]==[1,0,1,0]:  # if it's an IMAX screen
          ScoreForName=8
        elif Screens[Names][0:4]==[1,1,0,0]:  #if it's an Atmos screen
          ScoreForName=6
        else: #if it's a plain 2-D screen
          ScoreForName=3

        Screens_Name_Score[Names]=ScoreForName   
      
      
      FullSlot_Score={}
      #Dictionary with
      #key = Scrname_timing   value = Score accounting for type of score and timing  (out of 20)
      #Ex: Scr01 is a plain 2-D screen and has an 8 am slot: Scr01_08:00 am will have a total score of 3+3=6/20
      #structure
      #{'Scr01_08:00am':6, 'Scr01_12:00pm': 14, 'Scr02_04:00pm':17...}

      #Adding the score for the feature + the score for the timing to generate final score for a particular slot
      for i in Screens:
        if Screens[i][4]==1:
          FullSlot_Score[i+'_'+'08:00am'] = Screens_Name_Score[i] + 3     #Score for 8am TimeSlot -> 3/10 
        if Screens[i][5]==1:
          FullSlot_Score[i+'_'+'12:00pm'] = Screens_Name_Score[i] + 7     #Score for 12pm TimeSlot -> 7/10
        if Screens[i][6]==1:
          FullSlot_Score[i+'_'+'04:00pm'] = Screens_Name_Score[i] + 10    #Score for 4pm TimeSlot -> 10/10
        if Screens[i][7]==1:
          FullSlot_Score[i+'_'+'09:00pm'] = Screens_Name_Score[i] + 7     #Score for 7am TimeSlot -> 3/10


      return FullSlot_Score #, FullSlot_Features

    def ClassifyScreensAndMovies(Screens, FullSlot_Score, MovieVals, MovieNames): 

      Featurewise_Slots_Dict = {'2D':[], 'Atmos':[], 'IMAX': [], '3D':[]}
      #Structure
      #{'2D': List of 2D slots, 'Atmos' : List of Atmos Slots, 'IMAX': List of IMAX slots, '3D': List of 3D slots}
      #{'2D': ['Scr01_08:00am', 'Scr01_12:00pm'], 'Atmos' : ['Scr02_04:00pm', 'Scr02_09:00pm'], 'IMAX': ['Scr03_09:00pm'], '3D': ['Scr04_04:00pm']}

      for SlotName in FullSlot_Score:
        FeatureOfScreen = Screens[SlotName[0:5]][0:4] #Screens[first 5 characters of 'Scr01_08:00am'][0:4]
        if FeatureOfScreen==[1,0,0,1]:
          Featurewise_Slots_Dict['3D'].append(SlotName)
        elif FeatureOfScreen==[1,0,1,0]:
          Featurewise_Slots_Dict['IMAX'].append(SlotName)
        elif FeatureOfScreen==[1,1,0,0]:
          Featurewise_Slots_Dict['Atmos'].append(SlotName)
        else:
          Featurewise_Slots_Dict['2D'].append(SlotName)
        
      Featurewise_Movies_Dict={'2D': [], 'Atmos': [], 'IMAX': [], '3D': []}
      #Format
      #{'2D': List of 2D movies, 'Atmos' : List of Atmos Movies, 'IMAX': List of IMAX Movies, '3D': List of 3D Movies}
      #{'2D': ['Gargi', 'Vikram'], 'Atmos' : ['Top Gun Maverick', 'Legend'], 'IMAX': ['Thor'], '3D': ['Minions']}


      for MovieName in MovieVals:
        FeatureOfMovie = MovieVals[MovieName]
        if FeatureOfMovie==[1,0,0,1]:
          Featurewise_Movies_Dict['3D'].append(MovieName)
        elif FeatureOfMovie==[1,0,1,0]:
          Featurewise_Movies_Dict['IMAX'].append(MovieName)
        elif FeatureOfMovie==[1,1,0,0]:
          Featurewise_Movies_Dict['Atmos'].append(MovieName)
        else:
          Featurewise_Movies_Dict['2D'].append(MovieName)


      return Featurewise_Slots_Dict, Featurewise_Movies_Dict






    FullSlot_Score = GenerateSlots(Screens) 
    #Input is Screens - {'Scr01':[1,0,0,0,1,1,0,0], 'Scr02':[1,1,0,0,1,0,0,1]}
    #Output is {'Scr01_08:00am': 8, 'Scr01_12:00pm':17}

    #print(FullSlot_Score)




    MovieVals={} #Format {'Mov_1':[1,0,0,0], 'Mov_2':[1,1,0,0]}
    for i in Movies:
      MovieVals[i] = Movies[i][0]

    MovieNames = list(Movies.keys())     # List of MovieNames
    RelDate = [Movies[i][1] for i in Movies]   #List of Reldates corresponding to movie names  ['2022-07-07', '2022-08-08']
    Lng = [Movies[i][2] for i in Movies]       #List of Languages corresponding to movie names ['Tamil', 'Hindi']
    Bdg = [Movies[i][3] for i in Movies]       #List of Budgets corrresponding to movie names  [1000000, 20000000]
    Aud = [Movies[i][4] for i in Movies]       #List of AudienceType corresponding to movie names ['A', 'U/A']

    HighestBdg = max(Bdg) #Integer quantity


    MovieScore={}
    for i in range(len(MovieNames)):
      MovieScore[MovieNames[i]]=TotalScore(MovieNames[i], RelDate[i], Lng[i], Bdg[i], Aud[i], IntScore[i], HighestBdg)
    #MovieScore = {'Gargi': 9, 'Thor': 5}



    Featurewise_Slots_Dict, Featurewise_Movies_Dict = ClassifyScreensAndMovies(Screens, FullSlot_Score, MovieVals, MovieNames)
    #Input parameters
    #Screens is {'Scr01':[1,0,0,0,1,1,0,0], 'Scr02': [1,1,0,0,1,1,0,0]}
    #FullSlot_Score is {'Scr01_08:00am': 8, 'Scr01_12:00pm': 10, 'Scr02_04:00pm':13, 'Scr02_09:00pm': 12...}
    #MovieVals is {'Gargi':[1,0,0,0], 'Vikram':[1,0,0,0], 'TopGun':[1,1,0,0], 'Legend':[1,1,0,0], 'Thor':[1,0,1,0] 'Minions':[1,0,0,1]}
    #MovieNames is ['Gargi', 'Vikram', 'TopGun', 'Legend', 'Minions']


    #Output
    #Featureswise_Slots_Dict Structure 
    #{'2D': List of 2D slots, 'Atmos' : List of Atmos Slots, 'IMAX': List of IMAX slots, '3D': List of 3D slots}
    #{'2D': ['Scr01_08:00am', 'Scr01_12:00pm'], 'Atmos' : ['Scr02_04:00pm', 'Scr02_09:00pm'], 'IMAX': ['Scr03_09:00pm'], '3D': ['Scr04_04:00pm']}

    #Featurewise_Movies_Dict Structure
    #{'2D': List of 2D movies, 'Atmos' : List of Atmos Movies, 'IMAX': List of IMAX Movies, '3D': List of 3D Movies}
    #that is, say Gargi and Vikram are 2D movies, TopGun and Legend are Atmos movies, Thor is an IMAX movie and Minions is a 3D movie
    #{'2D': ['Gargi', 'Vikram'], 'Atmos' : ['Top Gun Maverick', 'Legend'], 'IMAX': ['Thor'], '3D': ['Minions']}





    Featurewise_Moviewise_MovieScore_Dict={'2D': [], 'Atmos': [], 'IMAX': [], '3D': []}
    #format of above dct
    #{'2D':[Score of Gargi, Score of Vikram], 'Atmos': [Score of TopGun, Score of Legend], 'IMAX':[Score of Thor], '3D': [Score of Minions]}
    #['2D':[9,10], 'Atmos':[5,6], 'IMAX':[5], '3D':[2]}
    for i in MovieNames: #i is a MovieName
      if i in Featurewise_Movies_Dict['3D']:   #if i is in the list of 3D movies
        Featurewise_Moviewise_MovieScore_Dict['3D'].append(MovieScore[i])  #append score of i to the list of 3d moviescores (that list is the value for the key '3D')
      elif i in Featurewise_Movies_Dict['IMAX']:  # if i is in the list of IMAX movies
        Featurewise_Moviewise_MovieScore_Dict['IMAX'].append(MovieScore[i])#append score of i to the list of IMAX moviescores (that list is the value for the key 'IMAX')
      elif i in Featurewise_Movies_Dict['Atmos']:  #if i is in the list of Atmos Movies
        Featurewise_Moviewise_MovieScore_Dict['Atmos'].append(MovieScore[i]) #append score of i to the list of Atmos moviescores (that list is the value for the key 'Atmos')
      else:
        Featurewise_Moviewise_MovieScore_Dict['2D'].append(MovieScore[i]) #append score of i to the list of 2D moviescores (that list is the value for the key 'IMAX')


      

    TotalScreens_2D = len(Featurewise_Slots_Dict['2D']) #Number of 2D slots
    TotalScreens_Atmos = len(Featurewise_Slots_Dict['Atmos']) #Number of Atmos slots
    TotalScreens_IMAX = len(Featurewise_Slots_Dict['IMAX']) #Number of IMAX slots
    TotalScreens_3D = len(Featurewise_Slots_Dict['3D']) #Number of 3D slots

    Featurewise_Moviewise_MaxNoOfShows = {'2D': [], 'Atmos':[], 'IMAX': [], '3D': []}

    if len(Featurewise_Movies_Dict['2D'])!=0:
      Featurewise_Moviewise_MaxNoOfShows['2D'] = TotalNoOfShows(Featurewise_Movies_Dict['2D'], Featurewise_Moviewise_MovieScore_Dict['2D'], TotalScreens_2D)
                                              #parameters     #List of 2D MovieNames=['Gargi', 'Vikram'], Corresponding MovieScores=[8,9], TotalnumberofScreenings of that type=4

    if len(Featurewise_Movies_Dict['Atmos'])!=0:
      Featurewise_Moviewise_MaxNoOfShows['Atmos'] = TotalNoOfShows(Featurewise_Movies_Dict['Atmos'], Featurewise_Moviewise_MovieScore_Dict['Atmos'], TotalScreens_Atmos)
                                                  #parameters     #List of MovieNames=['TopGun', 'Legend'], Corresponding MovieScores=[6,7], TotalnumberofScreenings of that type=3

    if len(Featurewise_Movies_Dict['IMAX'])!=0:
      Featurewise_Moviewise_MaxNoOfShows['IMAX'] = TotalNoOfShows(Featurewise_Movies_Dict['IMAX'], Featurewise_Moviewise_MovieScore_Dict['IMAX'], TotalScreens_IMAX)
                                                  #parameters     #List of MovieNames=['Thor'], Corresponding MovieScores=[5], TotalnumberofScreeningsof that type=3

    if len(Featurewise_Movies_Dict['3D'])!=0:
      Featurewise_Moviewise_MaxNoOfShows['3D'] = TotalNoOfShows(Featurewise_Movies_Dict['3D'], Featurewise_Moviewise_MovieScore_Dict['3D'], TotalScreens_3D)
                                              #parameters     #List of MovieNames=['Minions'], Corresponding MovieScores=[3], TotalnumberofScreeningsof that type=1

    #Featurewise_Moviewise_MaxNoOfShows structure
    #format {'2D': [MaxNoOfShows of Gargi, MaxNoOfShows of Vikram], 'Atmos':[MaxNoOfShows of TopGun, MaxNoOfShows of Legend], ...}
    #Featurewise_Moviewise_MaxNoOfShows = #{'2D': [1,2], 'Atmos': [1,1]...}





    TimeTables_2D= TimeTables_Atmos = TimeTables_IMAX = TimeTables_3D = {}
    BestTT_2D= BestTT_Atmos = BestTT_IMAX = BestTT_3D = {}
    BestTT={}

    #Run BruteTimeTables and Maximization module for each type of feature only if there is at least one movie with that feature
    if len(Featurewise_Movies_Dict['2D'])!=0: 
      TimeTables_2D = NewBruteTimeTables(Featurewise_Slots_Dict['2D'], Featurewise_Movies_Dict['2D'], Featurewise_Moviewise_MaxNoOfShows['2D'])
      #Timetables_2D = [{'Scr01_08:00am':'Gargi', 'Scr01_12:00pm': 'Vikram'},
      #                  {Scr01_08:00am': 'Vikram, 'Scr01_12:00pm': 'Gargi'}]


      #k=[i for i in Featurewise_Slots_Dict['2D']]   i.e list of 2D slot names
      #v=[FullSlot_Score[i] for i in Featurewise_Slots_Dict['2D']] i.e list of corresponding scores of those slots
      #creating {k:v}
      parameter2 = {k:v for(k,v) in zip([i for i in Featurewise_Slots_Dict['2D']],[FullSlot_Score[i] for i in Featurewise_Slots_Dict['2D']])}
      #parameter2 is a dict - {'Scr01_08:00am':8, 'Scr01_12:00pm':9...just the 2D slots and their corresp slotscores}

      #k=[i for i in Featurewise_Movies_Dict['2D']]  i.e list of 2D movienames
      #v=[MovieScore[i] for i in Featurewise_Movies_Dict['2D']] i.e list of corresponding scores of those movies
      #creating {k:v}
      parameter3 = {k:v for(k,v) in zip([i for i in Featurewise_Movies_Dict['2D']], [MovieScore[i] for i in Featurewise_Movies_Dict['2D']])}
      #parameter3 is a dict - {'Gargi': 7, 'Vikram':7,...just the 2D movies and their corresp scores}


      BestTT_2D = Maximisation(TimeTables_2D, parameter2, parameter3) #BestTT_2D={'Scr01_08:00am':'Gargi', 'Scr01_12:00pm': 'Vikram'}

    if len(Featurewise_Movies_Dict['Atmos'])!=0:
      TimeTables_Atmos = NewBruteTimeTables(Featurewise_Slots_Dict['Atmos'], Featurewise_Movies_Dict['Atmos'], Featurewise_Moviewise_MaxNoOfShows['Atmos'])
        #Timetables_Atmos = [{'Scr02_04:00pm':'TopGun', 'Scr02_09:00pm': 'Legend'},
          #                  {Scr02_04:00pm': 'Legend', 'Scr02_09:00pm': 'TopGun'}]


      parameter2 = {k:v for(k,v) in zip([i for i in Featurewise_Slots_Dict['Atmos']],[FullSlot_Score[i] for i in Featurewise_Slots_Dict['Atmos']])}
      #parameter2 : {'Scr02_04:00pm': 13, 'Scr02_09:00pm':8...just the Atmos slots and their corresp slotscores}
      parameter3 = {k:v for(k,v) in zip([i for i in Featurewise_Movies_Dict['Atmos']], [MovieScore[i] for i in Featurewise_Movies_Dict['Atmos']])}
      #parameter3 : {'TopGun': 7, 'Legend': 3......just the Atmos movies and their corresp moviescores}


      BestTT_Atmos = Maximisation(TimeTables_Atmos, parameter2, parameter3) #BestTT_Atmos = {'Scr02_04:00pm':'TopGun', 'Scr02_09:00pm': 'Legend'}

    if len(Featurewise_Movies_Dict['IMAX'])!=0:
      TimeTables_IMAX = NewBruteTimeTables(Featurewise_Slots_Dict['IMAX'], Featurewise_Movies_Dict['IMAX'], Featurewise_Moviewise_MaxNoOfShows['IMAX'])

      parameter2 = {k:v for(k,v) in zip([i for i in Featurewise_Slots_Dict['IMAX']],[FullSlot_Score[i] for i in Featurewise_Slots_Dict['IMAX']])}
      parameter3 = {k:v for(k,v) in zip([i for i in Featurewise_Movies_Dict['IMAX']], [MovieScore[i] for i in Featurewise_Movies_Dict['IMAX']])}
      BestTT_IMAX = Maximisation(TimeTables_IMAX, parameter2, parameter3)

    if len(Featurewise_Movies_Dict['3D'])!=0:
      TimeTables_3D = NewBruteTimeTables(Featurewise_Slots_Dict['3D'], Featurewise_Movies_Dict['3D'], Featurewise_Moviewise_MaxNoOfShows['3D'])

      parameter2 = {k:v for(k,v) in zip([i for i in Featurewise_Slots_Dict['3D']],[FullSlot_Score[i] for i in Featurewise_Slots_Dict['3D']])}
      parameter3 = {k:v for(k,v) in zip([i for i in Featurewise_Movies_Dict['3D']], [MovieScore[i] for i in Featurewise_Movies_Dict['3D']])}
      BestTT_3D = Maximisation(TimeTables_3D, parameter2, parameter3)

    BestTT.update(BestTT_2D)
    BestTT.update(BestTT_Atmos)
    BestTT.update(BestTT_IMAX)
    BestTT.update(BestTT_3D)

    return BestTT

def TrendsScore(MovieNames):
    pytrend = TrendReq()
    Scores={}
    i=0
    for i in MovieNames:
      kw_list =[i]
      
      pytrend.build_payload(kw_list, timeframe='2022-08-17 2022-08-24',geo='IN-TN')
      df=pytrend.interest_over_time()
      for i in kw_list:
        Scores[i]=df[i].mean()
    print("Interest_Score:",Scores)

    return(Scores)



"""
#########INPUTS TO THE BACKEND#########
Screens = {'Scr01': [1,0,0,0,1,1,1,1], 'Scr02': [1,1,0,0,0,1,1,1], 'Scr03': [1,0,1,0,1,1,1,0], 'Scr04': [1,0,0,1,0,0,1,0]}  
#Screens Format
#{'Scr01': [1,0,0,0,1,1,0,0] --First 4 elements for features. Second 4 elements- for Timings 8am 12 pm 4pm 9pm}

Movies={"Gargi":[[1,0,0,0],'2022-07-01','Tamil',40000000,'U'],"Vikram":[[1,0,0,0],'2022-06-20','Tamil',20000000,'U/A'], "Top Gun Maverick":[[1,1,0,0],'2022-07-07','English',10000000,'U/A'], "Legend": [[1,1,0,0], '2022-08-01', 'Tamil', 10000000, 'U'], "Thor":[[1,0,1,0],'2022-06-20','English',30000000,'U'],  "Minions": [[1,0,0,1], '2022-07-20', 'English', 12000000, 'U']}
#IntScore = [10, 14, 29, 21, 15, 17]
MovieNames=list(Movies.keys())
IntScore=list(TrendsScore(MovieNames).values())
#######################################

BestTT= ScreensAndMoviesToBestTT(Screens, Movies, IntScore)
print(BestTT)
"""
