import pymongo
from datetime import date, datetime, timedelta

conn = pymongo.MongoClient('mongodb+srv://bang:bang@cluster0-uiqcf.mongodb.net/test?retryWrites=true')
db = conn.get_database('bluevisor')

date = datetime.now().strftime('%Y-%m-%d')

standard_date = datetime.today() - timedelta(3)
def store():
    # test_table 테이블 선택
    collection = db.get_collection('posts')

    file = open('output.txt', 'r')
    lines = file.readlines()
    name = ''
    for line in lines:
        line = line.strip()
        tdl = line.split("*}(")     # title, date, link
        if len(tdl) == 1:
            name = tdl[0]
        else:
            post = {
                "name": name,
                "title": tdl[0],
                "start_date": tdl[1],
                "end_date": tdl[2],
                "link": tdl[3],
                "save_date": date
            }
            collection.insert_one(post)
    file.close()


def check_point_save(name, title):
    collection = db.get_collection('check_point')
    post = {
        "name": name,
        "title": title,
        "save_date": date
    }
    collection.update({"name": name},post,upsert=True)


def post_save(name, title, link, sdate, edate):
    collection = db.get_collection('posts')
    post = {
        "name": name,
        "title": title,
        "link": link,
        "start_date": sdate,
        "end_date": edate,
        "save_date": date
    }
    collection.insert_one(post)


def check_point_read(name):
    collection = db.get_collection('check_point')
    return collection.find_one({"name": name})
    # return collection.find({"date": date})


def is_saved(title):
    collection = db.get_collection('posts')
    return collection.find_one({"title": title})


def close():
    conn.close()


def result():
    file = open('output.txt', 'r')
    lines = file.readlines()

    file2 = open('result.txt', 'a')

    name = ''

    for line in lines:
        line = line.strip()
        tdl = line.split("*}(")     # title, link, date
        if len(tdl) == 1:
            name = tdl[0]
        else:
            file2.write('이름 : ' + name + '\n제목 : ' + tdl[0] + '\n시작 날짜 : ' + tdl[1] + '\n마감 날짜 : ' + tdl[2] + '\n링크 : ' + tdl[3] + '\n\n')
    file.close()
    file2.close()
