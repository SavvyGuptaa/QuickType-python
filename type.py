from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!= usertest[i]:
                error= error+1
        except :
            error = error+1
    return error

def speed_time(time_start,time_end,userinput):
    time_delay=time_end-time_start
    time_r= round(time_delay,2)
    speed = len(userinput)/time_r
    return round(speed)

if __name__ == '__main__':
    while True:
        ck=input("ready to test? yes/no : ")
        if ck == "yes":
            test = ["he quick brown fox jumps over the lazy dog again and again.",
            "The sun was shining brightly in the clear blue sky on a beautiful day.",
            "The big brown bear climbed up the mountain to find some honey to eat.",
            "The five boxing wizards jump quickly at the quirky brown fox.",
            "How vexingly quick witted zebras jump at the quirky brown fox."]
            test1= r.choice(test)
            print("******Typing speed*****")
            print(test1)
            print()
            print()

            time_1=time()
            testinput=input("Enter : ")
            time_2=time()

            print('Speed: ',speed_time(time_1,time_2,testinput)," w/s")
            print("Error:",mistake(test1,testinput))
        elif ck == "no":
            print("THANKYOU")
            break

        else:
            print("wrong input")



 
