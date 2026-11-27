# part 1 member 
name = input("name")
club = input("club name")

# part 2 club details
membernumber = 11
isactive = True
print("member number:" ,membernumber,"type:",type(membernumber))
print("isactive:" ,isactive, "type:",type(isactive))

# part 3badge code
frist = name [0:3]
last = name [-1]
code = frist + last
print("frist three letters of name:", frist)
print("last letters of name:",last)
print("club badge: ",code)