import csv

#############################################################################33
# PART A
#############################################################################33


total_distance = 0
list_a = []
list_b = []

with open("1.csv") as f:
    reader = csv.reader(f, delimiter=" ")
    #Fucked up and pasted with triple spaces lol.
    for i in reader:
        list_a.append(int(i[0])) 
        list_b.append(int(i[-1]))

list_a.sort() #Sorty sort sort
list_b.sort() #Sorty sort sort

frequency_dict = {}
for a,b in zip(list_a,list_b):
    total_distance += abs(a-b)
    frequency_dict[b] = frequency_dict.get(b,0) +1
print (total_distance)


similarity_score = 0
for a in list_a:
     similarity_score += a * frequency_dict.get(a,0)
print(f"{similarity_score =}")
print(f"{total_distance =}")