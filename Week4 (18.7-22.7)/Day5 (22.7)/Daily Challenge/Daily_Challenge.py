print("Please enter a comma-separated sentence")
message=input("")



# inputList = list(message.split(","))
# inputList.sort()
# print(inputList)


inputList=message.split(",")
print(inputList)
final_List=sorted(inputList)
print(final_List)

final_String=[print(x+",",end='') for x in final_List]