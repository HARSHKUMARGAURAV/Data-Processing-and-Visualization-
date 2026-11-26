import requests
import matplotlib.pyplot as plt

API_URL="http://127.0.0.1:5000/students"

def fetch_student_scores():
    response=requests.get(API_URL,timeout=10)
    response.raise_for_status()
    return response.json()

def calculate_average(students):
    scores = [student["score"] for student in students]
    return sum(scores)/len(scores)

def display_chart(students):
    names=[student["name"]for student in students]
    scores=[student["score"]for student in students]


    plt.bar(names,scores)
    plt.xlabel("students")
    plt.ylabel("scores")
    plt.title("student test score")
    plt.ylim(0,100)
    plt.show()

def main():
    try:
        students=fetch_student_scores()
        print("\nStudent test Score")
        print("--------------------")
        for student in students:
            print(f"{student['name']}:{student['score']}")

            average=calculate_average(students)
            print(f"\nAverage Score:{average:.2f}")
            display_chart(students)
    except(requests.RequestException,ValueError,KeyError,TypeError) as error:
            print("error:",error)

if __name__=="__main__":
     main()