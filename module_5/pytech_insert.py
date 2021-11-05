""" 
    Title: pytech_insert.py
    Author: Esther Portnoy
    Date: 04 November 2021
    Description: Test program for inserting new documents 
                 into the students collection 
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.r51ca.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

""" three student documents"""
# Student 1 data document 
aaron = {
    "student_id": "1007",
    "first_name": "Aaron",
    "last_name": "Judge",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Boone",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Boone",
                    "grade": "A+"
                }
            ]
        }
    ]
}

# Student 2 data document 
gerrit = {
    "student_id": "1008",
    "first_name": "Gerrit",
    "last_name": "Cole",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Boone",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Boone",
                    "grade": "A+"
                }
            ]
        }
    ]
}

# Student 3 data document
dj = {
    "student_id": "1009",
    "first_name": "DJ",
    "last_name": "LeMahieu",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Boone",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Boone",
                    "grade": "A+"
                }
            ]
        }
    ]
}

# get the students collection
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
aaron_student_id = students.insert_one(aaron).inserted_id
print("  Inserted student record Aaron Judge into the students collection with document_id " + str(aaron_student_id))

gerrit_student_id = students.insert_one(gerrit).inserted_id
print("  Inserted student record Gerrit Cole into the students collection with document_id " + str(gerrit_student_id))

dj_student_id = students.insert_one(dj).inserted_id
print("  Inserted student record DJ LeMahieu into the students collection with document_id " + str(dj_student_id))

input("\n\n  End of program, press any key to exit... ")