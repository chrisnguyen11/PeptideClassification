# dependencies
import pandas as pd
import numpy as np

def one_hot (sequence):
    aa_alphabet = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
    encoding = [[ 
        1 if seq == aa else (1/20 if seq not in aa_alphabet else 0) # if not in aa_alphabet, impute as the mean 
            for aa in aa_alphabet[:-1] # avoid collinearity trap
                ] for seq in sequence.upper() 
                ] 
    return [aa for postion in encoding for aa in postion] # flatten into a single list

