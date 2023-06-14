#!/usr/bin/python3
def weight_average(my_list=[]):
    top = 0
    bot = 0
    if len(my_list) == 0:
        return 0
    for i in my_list:
        top += i[0] * i[1]
        bot += i[1]
    return top/bot
