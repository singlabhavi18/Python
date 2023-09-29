def speed_caught(speed, bday):
    
    if (bday):
        speed = speed-5
    if speed>80:
        print("Heavy Challan")
    elif (speed>60 & speed<=80):
        print("Small Challan")
    else:
        print("No Challan")
        
speed_caught(81, True)
speed_caught(81, False)
