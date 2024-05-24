import matplotlib.pyplot as plt
import numpy as np
import bst
import btree
import hash_table_chain as htc


def count_repeats(H):
    repeat = []
    for i in H.bucket:
        for rec in i:
            repeat = repeat + H.bucket[i][rec]
            print(repeat)
            
            
