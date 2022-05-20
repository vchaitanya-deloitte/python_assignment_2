#1
from collections import Counter
numbers = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

for counts in numbers:
    counts1 = dict(Counter(counts))
    duplicates = {key: value for key, value in counts1.items() if value > 1}
    print(duplicates)


#2
list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
string = ""
lst=[]
for i in list1:
    for j in list2:
        string = i+j
        lst.append(string)
print(lst)



#3
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sublist = ["h", "i", "j"]
list1[2][1][2].extend(Sublist)
print(list1)



#4
Keys = ['Ten', 'Twenty', 'Thirty']
Value = [10,20,30]
print(dict(zip(Keys,Value)))



#5
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)


#6
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
newkey= "location"
oldkey= "city"
sampleDict[newkey]=sampleDict[oldkey]
sampleDict.pop(oldkey)
print(sampleDict)



#7
dict= {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
list=[]
for key, val in dict.items():
  list.append([key]+val)
print(list)
