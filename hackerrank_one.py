if __name__ == '__main__':
    student_details = {
        'alpha': [20, 30, 40],
        'beta': [30, 50, 70]
    }
    query_name = 'beta'
    
    sum = 0
    count = 0
    for score in student_details[query_name]:
        sum = sum + score
        count += 1
    
    average = sum / count
    rounded = format(average, ".2f")
    print(rounded)