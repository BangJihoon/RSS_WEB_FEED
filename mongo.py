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

    for line in lines:
        line = line.strip()
        tld = line.split("*}(")     # title, link, date
        if len(tld) == 1:
            name = tld[0]
        else:
            post = {
                "name": name,
                "title": tld[0],
                "post_date": tld[1],
                "link": tld[2],
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


def post_save(name, title, link, pdate):
    collection = db.get_collection('posts')
    post = {
        "name": name,
        "title": title,
        "link": link,
        "date": pdate,
        "save_date": date
    }
    collection.update({"name": name},post,upsert=True)


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
        tld = line.split("*}(")     # title, link, date
        if len(tld) == 1:
            name = tld[0]
        else:
            if name == 'kstartup':
                file2.write('이름: '+name+'\n제목: '+tld[0]+'\n링크: '+tld[1]+'\n마감일: '+tld[2]+'\n\n')
            else :
                file2.write('이름: ' + name + '\n제목: ' + tld[0] + '\n링크: ' + tld[1] + '\n등록일: ' + tld[2] + '\n\n')
    file.close()
    file2.close()




