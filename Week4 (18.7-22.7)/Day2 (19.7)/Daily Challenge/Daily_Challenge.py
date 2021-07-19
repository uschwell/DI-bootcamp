birthday=input("What is your birthday? (DD/MM/YY)")

birthday_split=birthday.split('/');
#on the day I programmed this-I figure the persons age around +- july. calculating for days is not worth it (becomes obsolete within 24 hours)
if(int(birthday_split[1])>=7):
    age=(2020-int(birthday_split[2]));
else:
    age=(2021-int(birthday_split[2]));

last_age=(age%10);
#find leap years
if(int(birthday_split[2])%4==0):
    draw=2;
else:
    draw=1;

for leap in range(draw):
    #1st line
    remainder=11-last_age;
    remainder=int(remainder/2);
    print('    ',end='');
    for i in range(remainder):
        print('_',end='');
    for i in range(last_age):
        print('i',end='');
    for i in range(remainder):
        print('_',end='');
    print('');
    #lines 2-6
    print_help=["   |:H:a:p:p:y:|"," __|___________|__","|^^^^^^^^^^^^^^^^^|","|:B:i:r:t:h:d:a:y:|","|                 |","~~~~~~~~~~~~~~~~~~~"];
    for x in print_help:
        print(x);

print("\n");