def count_grades_while(grade_list, average):
    count = 0
    index = 0
    while index < len(grade_list):
        if grade_list[index] >= average:
            count += 1
        index += 1
    return count

def count_grades_range(grade_list, average):
    count = 0
    for index in range(len(grade_list)):
        if grade_list[index] >= average:
            count += 1
    return count

def count_grades_for(grade_list, average):
    count = 0
    for grade in grade_list:
        if grade >= average:
            count += 1
    return count

def main():
    grades = [65, 70, 85, 90, 55, 76]
    average = sum(grades) / len(grades)
    result = count_grades_while(grades, average)
    print(f'Number of grades greater than average {average} are {result} grades')
   # print(result)

main()