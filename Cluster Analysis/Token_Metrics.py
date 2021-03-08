"""
These functions are extremely useful and fast in estimating the similarities between pairs of strings (texts). 
They first divide the texts into shingles or tokens, then compare them and return the similarity 
value using three different string metrics: Jaccard similarity, Sørensen_Dice, and Overlap Coefficient.
"""

from collections import Counter
        

def Jaccard(str_a, str_b):
    
    tok_sent_1 = str_a
    tok_sent_2 = str_b
    shingles = lambda s:[s[i:i+10] for i in range(len(s)-9)]
    intersection = list((Counter(shingles(tok_sent_1)) & Counter(shingles(tok_sent_2))).elements())
    intersection = len(intersection)
    union = list((Counter(shingles(tok_sent_1)) | Counter(shingles(tok_sent_2))).elements())
    union = len(union)
    try:
        Jaccard_distance = intersection / union
        return Jaccard_distance
    except ZeroDivisionError: return Jaccard_distance
        
    

def Sørensen_Dice(str_a, str_b):
    tok_sent_1 = str_a
    tok_sent_2 = str_b
    shingles = lambda s:[s[i:i+10] for i in range(len(s)-9)]
    intersection = list((Counter(shingles(tok_sent_1)) & Counter(shingles(tok_sent_2))).elements())
    intersection = len(intersection)
    sum_of_elements = len(shingles(tok_sent_1)) + len(shingles(tok_sent_2))
    try:
        Sørensen_Dice_distance = intersection *2 / sum_of_elements
        return Sørensen_Dice_distance
    except ZeroDivisionError: return Sørensen_Dice_distance
        


def Overlap_Coefficient(str_a, str_b):
       
    tok_sent_1 = str_a
    tok_sent_2 = str_b
    shingles = lambda s:[s[i:i+10] for i in range(len(s)-9)]
    intersection = list((Counter(shingles(tok_sent_1)) & Counter(shingles(tok_sent_2))).elements())
    intersection = len(intersection)
    smaller_set = min(len(shingles(tok_sent_1)), len(shingles(tok_sent_2)))
    try:
        Overlap_Coefficient_distance = intersection / smaller_set
        return Overlap_Coefficient_distance
    except ZeroDivisionError: return Overlap_Coefficient_distance


