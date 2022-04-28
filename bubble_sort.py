student_scores = input("input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#########################
length = len(student_scores)

while length >1:
  
  switched = True

  for x in range(0, length-1):
    if int(student_scores[x]) > int(student_scores[x+1]):
      student_scores[x], student_scores[x+1] = student_scores[x+1], student_scores[x]
      switched = False

  if switched:
    break

  print(f"order of the set: {student_scores}")
