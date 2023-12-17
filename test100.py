def christmas_cheer_cal(cheer,name):
    if cheer < 5:
        print("you dont have enough cheer" , name, "get some more")
    elif cheer ==5:
        print("you have enough" ,name,)
    else:
        print("great christmas cheer" ,name, )

christmas_cheer_cal(2,"Laura")