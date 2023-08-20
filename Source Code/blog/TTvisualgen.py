
def VisualTT(timetable,screens,slots):
    FormattedTT={}
    for i in screens:
        FormattedTT[i]=['-','-','-','-']
        for j in range(len(slots)):
            name=i+'_'+slots[j]
            if name in timetable:
                FormattedTT[i][j]=timetable[name]
    return FormattedTT


""""
TT={'Scr01_12:00pm': 'Sita Ramam', 'Scr01_04:00pm': 'Viruman', 'Scr01_09:00pm': 'Sita Ramam', 'Scr02_08:00am': 'Sita Ramam', 'Scr02_12:00pm': 'Viruman', 'Scr02_04:00pm': 'Viruman', 'Scr05_08:00am': 'Thiruchitrambalam', 'Scr05_12:00pm': 'Thiruchitrambalam', 'Scr05_04:00pm': 'Thiruchitrambalam', 'Scr05_09:00pm': 'Thiruchitrambalam', 'Scr04_04:00pm': 'Liger', 'Scr04_09:00pm': 'Liger', 'Scr03_04:00pm': 'Dragon Ball Super:Super Hero', 'Scr03_09:00pm': 'Dragon Ball Super:Super Hero'}
Screen_Facilities={'Scr01': [1, 0, 0, 0, 0, 1, 1, 1], 'Scr02': [1, 0, 0, 0, 1, 1, 1, 0], 'Scr03': [1, 0, 0, 1, 0, 0, 1, 1], 'Scr04': [1, 0, 1, 0, 0, 0, 1, 1], 'Scr05': [1, 1, 0, 0, 1, 1, 1, 1]}
Slots = ['08:00am', '12:00am', '04:00pm', '09:00pm']
Screens=list(Screen_Facilities.keys())
print(VisualTT(TT,Screens,Slots))
"""

