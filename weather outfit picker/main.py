tempreature = 8
if tempreature < 15:
    outfit = "jacket"
    print("it is very cold ")
    print("weare up", outfit)
else:
    outfit = "t-shirt"
    print("it is warm")
    print("weare up",outfit)

    # it is raining
raining = input("it is raining (yes/no)")
if raining == "yes":
    print("bring an umbrela")

# ask for wind speed
windspeed = int(input("enter the wind speed "))
if windspeed > 50:
    needwindspeed = "yes"
    print(" it is windy today")
    print("weare a windbreaker",outfit)
else:
    needwindspeed = "no"
    print(" it is not windy today")
    print("no need of windbreaker",outfit)

    # print messeages
print("")
print("weather check")
print("tempreature",tempreature)
print("outfit chossen",outfit)
print("windspeed",windspeed)
print("windbreaker",needwindspeed)
print("raining",raining)