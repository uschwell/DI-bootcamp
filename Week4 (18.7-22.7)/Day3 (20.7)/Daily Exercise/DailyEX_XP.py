######################EX1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict={};
# for x,y in enumerate(keys):
#     print(keys[x]);
#     print(values[x]);
#     dict[keys[x]]=values[x];
# # print(dict);




######################EX2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total=0;
# for name in family:
#     # print(name);
#     # print(family[name]);
#     if(3<=family[name])and(family[name]<=12):
#         total+=10;
#     elif(12<family[name]):
#         total+=15;

# print("your total is: ",+total);





######################EX3

brand={
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color':{
    'France': 'blue', 
    'Spain': 'red', 
    'US': ['pink', 'green']
    }
}
# print(brand);

brand['number_stores']=2;
temp=brand['major_color'];
temp2=[];
for names in temp:
    temp2.append(names);
print("Zaras clients include people from countries all over the world. Including: "+str(temp2))
#step 6
brand['country_creation']='Spain';
#step 7
if(brand['international_competitors']):
    brand['international_competitors'].append('Desigual');

#step 8
del brand['creation_date']

#step 9
length= len(brand['international_competitors'])
print(brand['international_competitors'][length-1])

#step 10
