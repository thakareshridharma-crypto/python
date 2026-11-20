# part one agent details
name = input("enter your real name,agent: ")
gadet = input("enter your favourite gadet: ")

# part two store agent details
agentNumber = 7
speedRating = 9.5
missionCount = 12
hight = 6.5
active = True

# part three print each details with data type
print("name: ", name, "type: ", type(name))
print("gadet: ", "type: ", type(gadet)) 
print("agentNumber: ", "type: ", type(agentNumber))
print("speedRating: ", "type: ", type(speedRating))
print("missionCount: ", "type: ", type(missionCount))
print("hight: ", "type: ", type(hight))
print("active: ", "type: ", type(active))

# part four type cast
agentNumberText = str(agentNumber)
speedRatingText = str(speedRating)

print("agent number as text: ",agentNumberText ,"type:" ,type(agentNumberText))

# part 5 slicing
frist = name [0:3]
last = name [-1:]
code = frist + last
print("frist three letters of name: ",frist)
print("last letter of name:",last)
print("secret code:", code)

















