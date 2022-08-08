'''marks using dicitinory datatype'''

tenth = {"Telugu": 9, "English": 5, "Mathematics": 10, "Science": 8, "Social": 7, "Hindi": 8}
inter = [132,148,128,77,54,45,29,26]
#loop to sum all values
dic = 0
lis = 0
for i in inter:
    dic += i

for j in inter:
    lis += i


# using len() to get total keys for mean computation
dic = dic / len(tenth)
lis = sum(inter)/len(inter)


#printing result
print("the anenger marks is : " +str(dic))
print("the avenger marks is : ",lis)

"""
marks = {"eng": 60, "hin": 75, "math": 85, "phy": 65, "che": 65}

count =sum(marks.values())/len(marks)
print("the computed mean : " + str(count))

"""
