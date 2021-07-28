import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


jsonObject = json.loads(sampleJson)

temp=(jsonObject['company']['employee']['payable']['salary'])
print(temp)


# or in case you wanted something a 'little' more code-ing
temp1=jsonObject['company']
# print(temp1)
temp2=temp1['employee']
# print(temp2)
temp3=temp2['payable']
# print(temp3)
temp4=temp3['salary']
print(temp4)