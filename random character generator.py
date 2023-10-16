# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:34:19 2023

@author: Don Jeffrey
"""

from tkinter import*
import random

root = Tk()
root.title("LUCKEY FRIEND")
root.geometry ("500x500")

alpha_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

random_word = Label(root,text="RANDOM WORD : ")

def gen_luck():
    rand_letter1 = random.randint(0, 25)
    rand_letter2 = random.randint(0, 25)
    rand_letter3 = random.randint(0, 25)
    rand_letter4 = random.randint(0, 25)
    rand_letter5 = random.randint(0, 25)
    rand_letter6 = random.randint(0, 25)
    
    word_convert1 = alpha_list[rand_letter1]
    word_convert2 = alpha_list[rand_letter2]
    word_convert3 = alpha_list[rand_letter3]
    word_convert4 = alpha_list[rand_letter4]
    word_convert5 = alpha_list[rand_letter5]
    word_convert6 = alpha_list[rand_letter6]
    
    
    
    Rand_word_var = str(word_convert1)+str(word_convert2)+str(word_convert3)+str(word_convert4)+str(word_convert5)+str(word_convert6)
    
    random_word["text"]=Rand_word_var

luckey_generate = Button(root,text="GENERATE",command=gen_luck)
luckey_generate.place(relx=0.5,rely=0.5,anchor=CENTER)
random_word.place(relx=0.5,rely=0.3,anchor=CENTER)


root.mainloop()