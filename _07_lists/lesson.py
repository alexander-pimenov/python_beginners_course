from pydantic.v1.datetime_parse import parse_time

people = ['Rin', 'Christian', 'Samuel', 'Elizabeth', 'James', 'Naomi']
people3 = ['Samuel', 'Elizabeth', 'James', 'Naomi']
print(people)
people.append("qwerty")
print(people)

last_el = people.pop()
print(last_el)
print(people)
people.extend(people3)
# print(people)


print(len(people))
people2 = list(
    "ytt"
)
print(people2)
print("Naomi" in people)
print("Sarah" in people)


mlist1 = [1,2,3]
mlist2 = [1,3,2]
mlist3 = [1,2,3,7,0,4,3,8]
mlist4 = mlist1 + mlist2 + mlist3
print(mlist3)
mlist3.sort()
print(mlist3) #[0, 1, 2, 3, 3, 4, 7, 8]
mlist3.sort(reverse=True) #[8, 7, 4, 3, 3, 2, 1, 0]
print(mlist3)

# print(mlist4)
# print(mlist1 == mlist2)
# print(mlist1 == mlist3)
# print(sum(mlist1) == sum(mlist2))
# mlist4.append(99)
# print(mlist4)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


str1 = 'my name is rin'
str2 = str1.split(' ')
print(str2) #['my', 'name', 'is', 'rin']
str3 = '+-+'.join(str2)
print(str3) #my+-+name+-+is+-+rin