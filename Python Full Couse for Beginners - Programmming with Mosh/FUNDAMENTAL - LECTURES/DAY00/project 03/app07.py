course = 'Python for Beginners'
print(len(course))


#len = length
#Python for Beginners
#01234567890123456789

print(course.upper())

#method course.*
#method course.upper() : capitalize

print(course.find('o'))
print(course.find('O'))
print(course.find('Beginners'))
#.find is case sensitive


print(course.replace('Beginners',"Absolute Beginner"))
print(course.replace('beginners',"Absolute Beginner"))

##################

print('Python' in course)  #True
print('python' in course)  #False
