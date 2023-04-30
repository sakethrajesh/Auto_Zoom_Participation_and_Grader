import requests
import pandas as pd
import sys

# Set up
API_URL = "https://canvas.vt.com/api/v1"
API_TOKEN = ""
course_id = ""

# /api/v1/courses/:course_id/assignments
def submitGrade(assignment_id, student_id, grade):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    # Make the API request to submit the grade
    url = f"{API_URL}/courses/{course_id}/assignments/{assignment_id}/submissions/update_grades?grade_data[{student_id}][posted_grade]={grade}"

    response = requests.post(url, headers=headers)

    # return respose code
    return response.status_code


def gradeFromCSV(csv):
    # Open the CSV file in an iterator, skipping the first row
    csv_iterator = pd.read_csv(csv, iterator=True, chunksize=1, skiprows=1)

    # Loop over the iterator and convert each line to a dictionary
    for chunk in csv_iterator:
        row = chunk.to_dict('records')[0]
        fname = row['First Name']
        lname = row['Last Name']
        student_id = row['Canvas Student ID']
        assignment_id = list(row)[3]
        grade = row[assignment_id]

        # print(row)
        # print(fname)
        # print(lname)
        # print(student_id)
        # print(assignment_id)
        # print(grade)

        status = submitGrade(assignment_id, student_id, grade)

        if status != 200:
            return "submission of " + fname + " " + lname + "'s" + "grade failed\n previous submissions sucsessfull\n proceeding grades not submitted"
    
    
    return "all submissions were sucsessful"

if len(sys.argv) != 2:
    print("invalid arguments")
else:
    csv = sys.argv[1]
    print(gradeFromCSV(csv))
