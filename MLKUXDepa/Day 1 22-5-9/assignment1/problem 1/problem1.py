score = int(input())
if ((score % 3) == 0)  and (score % 5 == 0):
    print("Three and Five!")
elif ((score % 3) == 0):
    print("Three!")
elif ((score % 5) == 0 ):
    print("Five!")