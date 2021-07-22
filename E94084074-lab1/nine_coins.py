#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Nine_Coins:
    """ Nine_Coins is to generate random nine filp coin"""
    def __init__(self,num):                         #it's class init:(num)cna be transform into 
        self.num= "{:09b}".format(num)              ##binary
        self.decimalnum=format(num,"d")                ##decima
        self.randomnum=num                               ##random
    def toss(self):                                 #toss random function to gernerate the number then transform into decimal and binary
        from random import randint                     
        self.randomnum=randint(0,511)
        self.num= "{:09b}".format(self.randomnum) 
        self.decimalnum=format(self.randomnum,"d")
    def __str__(self):
        return f'binary: {self.num}  and  decimal: {self.decimalnum}'  ##print it when use print
    def __repr__(self):                                          ##print it when not use print
        print("Nine_Coins:",end=' ')
        for i in range(9):
            if self.num[i]=='0':
                print('H',end="")
            else:
                print('T',end="")
        return  f"\n"
            


# In[ ]:




