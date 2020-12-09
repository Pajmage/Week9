'''
MSc Digital and Technology Solutions
CETM65 Software Engineering Principles
Author: Paul Jones
Date: 08/12/2020

Week 9 - ePortfolio Task 2    

Functions for clalculating required DB fields
'''

def Km_To_Miles(length):
    Miles = int(length) / 1.6
    return Miles


def Rating(length, rapids):
    if length < 5:
        lengthScore = 1
    elif length >= 6 and length <=10:
        lengthScore = 2
    elif length > 11:
        lengthScore = 3

    RiverScore = lengthScore + rapids
    return RiverScore

def River_Grade(RiverScore):
    if RiverScore >= 2 and RiverScore <= 3:
        RiverRating = "Easy"
    elif RiverScore >= 4 and RiverScore <= 6:
        RiverRating = "Medium"
    elif RiverScore >= 7 and RiverScore <= 8:
        RiverRating = "Hard"
    else:
        RiverRating = "Extreme"
    
    return RiverRating 
