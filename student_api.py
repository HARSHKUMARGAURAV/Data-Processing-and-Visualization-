from flask import Flask,jsonify
app=Flask(__name__)

students= [
    {"name":"rahul","score":85},
    {"name":"priya","score":90},
    {"name":"Amit","score":75},
    {"name":"Sneha","score":95},
    {"name":"Rohit","score":80}
]

@app.route("/students",methods=["GET"])
def get_students():
    return jsonify(students)

if __name__=="__main__":
    app.run(debug=True,port=5000)
