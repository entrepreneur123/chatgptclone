
from flask import Flask, jsonify,render_template, request
from flask_pymongo import PyMongo
import openai


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://username:password@cluster0.vqpxwji.mongodb.net/";
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats = myChats)

@app.route("/api",methods=["GET","POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat  = mongo.db.chats.find_one({"question":question})
        print(chat)
        if chat:
            data={"question":question, "answer":f"{chat['answer']}"}
            return jsonify(data)
        else:
            response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=question,
                    temperature=0.7,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
            )
            print(response)
            data = {"question":question, "answer":response["choices"][0]["text"]}
            mongo.db.chats.insert_one({"question":"question", "answer":response["choices"][0]["text"]})
            return jsonify(data)
       
    data={"request":"Thank you yarr"}
    return jsonify(data)


app.run(debug=True)