keys = [email, person1, person2]
mylist = []
for k in keys:
        mylist.append(k)
for i in traits:
        mylist.append(i)

with open('traitify.csv', 'wb') as myfile:
    w = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    w.writerow(mylist)
