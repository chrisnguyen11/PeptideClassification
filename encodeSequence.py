# dependencies
import pandas as pd
import numpy as np

def one_hot (sequence):
    aa_alphabet = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
    encoding = [[ 
        1 if seq == aa else 0 # Note if seq is not in aa_alphabet returns 0 for all which is V
            for aa in aa_alphabet[:-1] # avoid colinearity, trap
                ] for seq in sequence.upper() 
                ] 
    return [aa for postion in encoding for aa in postion] # flatten 
