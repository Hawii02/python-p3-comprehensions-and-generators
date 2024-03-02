#!/usr/bin/env python3

def return_evens(num_list):
    even_num = [n for n in num_list if n % 2 == 0]
    return even_num
print(return_evens([0,1,2,3,4]))
    
def make_exclamation(sentence_list):
    sentence = [i + '!' for i in sentence_list]
    return sentence
print(make_exclamation("Hello there," "miss"))
