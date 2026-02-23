subs=int(input('how many subjects u got?: '))

if(subs>10):
    print('no way u got more than 10 subjects, tell the truth u goober >:( ')
    subs=int(input('how many subjects u got?: '))

print('ok, type in the grades for ',subs,' subjects in ordeer')

grades=[]
for i in range(0,subs,1):
    grade=float(input('Enter grade for subjects: '))
    grades.append(grade)
    print(grades)


for i in range(0,subs,1):
    print('UR grades are:',grades[i])


avg=float(sum(grades)/subs)
print('ur average is:',avg)

if(avg<5):
    print('ay u wanna sweep the streets with that average?, lock in bro')

if(avg>=5 and avg<9):
    print('good job, keep it up you cna score higher!')

if(avg>=9):
    print('nerd \n\n\n\n jk give mesome tips lol')