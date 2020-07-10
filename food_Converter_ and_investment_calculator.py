#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def food ():
    Cost=input('please tell me cost ')
    Tax=float(Cost)*0.15
    print('Tax :',Tax)
    Tip=float(Cost)*0.0825
    print('Tip :',Tip)
    entirebill=float (Cost)+Tax+Tip
    print (entirebill)
food()


# In[ ]:


def Converter ():
    Inches=input('Please tell me how much inches you need to convert:')
    cm=float(Inches)*2.54
    print('cm :',cm)
    Pounds=input('Please tell me how much pounds you need to convert:')
    kg=float(Pounds)*0.453592
    print('kg :',kg)
    Fahrenheit=input('Please tell me how much fahrenheit you need to convert:')
    Celsius=(float(Fahrenheit) - 32) * 5/9
    print('Celsius :',Celsius)
    celsius=input('Please tell me how much celsius you need to convert:')
    fahrenheit=(float(celsius)/5) * 9+ 32
    print('fahrenheit :', fahrenheit)

Converter()


# In[ ]:


def investment_calculator ():
    principal=input('Please tell me how much principles you need to calculate:')
    Return_rate=input('Please tell me how much retuen rates you need to calculate:')
    Time=input('Please tell me how much time you need to calculate:')
    earning=float(principal)*float(Return_rate)*float(Time)
    print('earning :', earning)
    
investment_calculator ()

