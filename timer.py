import time

#Input Time In Seconds
seconds=input("Enter The Time In Seconds: ")

#Define The Countdown Timer Function
def countdown_timer(seconds):
    while seconds >0:
         mins=int(seconds/60)
         secs=int(seconds%60)

         timer= f'{mins}:{secs}'
         print(timer,end="\r")
         time.sleep(1)
         seconds -=1

   

         
         

    print("Time Up")





#Function Call
countdown_timer(int(seconds))


    