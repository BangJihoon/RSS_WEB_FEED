from flask import Flask, render_template
import pymongo
app = Flask(__name__)

@app.route('/')
@app.route('/mongo',methods=['POST'])
def mongoTest():
    client = pymongo.MongoClient('mongodb+srv://bang:bang@cluster0-uiqcf.mongodb.net/test?retryWrites=true')
    db = client.get_database('bluevisor')
    collection = db.get_collection('posts')
    results = collection.find()
    client.close()
    return render_template('post.html', data=results)


if __name__ == '__main__':
    app.run()
