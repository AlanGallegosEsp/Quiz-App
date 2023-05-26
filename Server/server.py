"""
    @Author: AlanGallegosEsp
    @Author: PauAM10
    @Date: 5/23/2023
    @last update: 5/23/2023 10:24 PM
"""

from flask import Flask
from flask_cors import CORS
from mongoController import getQuestion, createUser, verifyUser
from flask import request
from flask import jsonify
from flask import Response
from datetime import datetime
import random


app = Flask(__name__)
CORS(app)


@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        id = int(request.json['id'])
        questionJSON = getQuestion(id)
        return jsonify(questionJSON)

@app.route('/api/getQuestions', methods=['POST'])
def getQuestions():
    numQuestions = int(request.json['numQuestions']) 
    randomList = random.sample(range(1, 4), numQuestions)
    questions = []
    if numQuestions ==  1:
        questions.append(getQuestion(1))
        return jsonify(questions)
    else:
        for i in randomList:
            questions.append(getQuestion(i))
        return jsonify(questions)

@app.route('/api/users', methods=['POST'])
def create_user():
    user = {"Username": request.json['username'], "Number_of_questions": request.json['numQuestions'], "Time": datetime.now()}
    res = verifyUser(user["Username"])
    if res == None:
        createUser(user)
        print("User created")
        return "User created", 201
    else:
        print("User already exists")
        return "User already exists", 409

    #createUser(user)

    
        

if __name__ == '__main__':
    app.run(debug=True)