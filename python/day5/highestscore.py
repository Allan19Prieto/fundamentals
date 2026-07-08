student_scores = [78, 56, 92, 87, 65]

total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score

print(sum)

# Max function
print(max(student_scores))

# make the same but with a for loop
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)


