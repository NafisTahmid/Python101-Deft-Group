details = {
    "name":"Jalail Ahmed",
    "id": 18398,
    "cgpa":3.98,
    "department":"CSE",
    "subject":[{
        "Bangla":89,
        "OOP":78,
        "English":97,
        "Maths":94,
        "AI":87,
        }
    ],
}
key_list = list(details["subject"][0].keys())
# Sum
total_score = 0
for subject, score in details["subject"][0].items():
    total_score += score
average_score = total_score/len(details["subject"][0])
# Make a details
print_details = "Hi, name! You are a student of department_name. Department name: department_id, last semester you have complete subject name your average mark is: mark, Your average CGPA is: cgpa. Your letter grade is: letter grade"
print("Hi,", details["name"],"! You are a student of", details["department"],". Department id:", details["id"], ". Last semester you have completed", key_list[0], ",", key_list[1],",", key_list[2], ",", key_list[3], ".Your average CGPA is:", average_score)
# print(f"Hi {details["name"]}. You are a student of {details["depratment"]}. Depratment id: {details["id"]}. Last semeste you have completed, {key_list[0]}, {key_list[1]}, {key_list[2]}, {key_list[3]}. Your average CGPA is: {average_score}")
# print(details["subject"]["Bangla"])
# print("Avg: ",total_score/len(details["subject"][0]))
