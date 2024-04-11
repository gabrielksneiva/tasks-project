from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['tasksdb']
collection = db['tasks']

def insert_data(data):
    try:
        data = collection.insert_one({'task': data})
        if data != None:
            return {"message": "Data inserted!"}
        else:
            return {"message": "Error to insert data!"}
    except Exception as e:
        raise ValueError(e)


def show_all_data():
    output = []
    for data in collection.find():
        output.append(data)
    return output
    
def get_data(data):
    try:
        data = collection.find_one({'task': data})
        if data != None:
            return data['task']
        else:
            return {"message": "Data not found!"}
    except Exception as e:
        raise ValueError(e)
    

def update_data(filter, data):
    try:
        data = collection.update_one({'task': filter}, {'$set': {'task': data}})
        if data != None:
            return {"message": "Ok"}
        else:
            return {"message": "Error when updating data!"}
    except Exception as e:
        raise ValueError(e)
    
def delete_data(data):
    try:
        data = collection.delete_one({'task': data})
        if data != None:
            return {"message": "Ok"}
        else:
            return {"message": "Error deleting data!"}
    except Exception as e:
        raise ValueError(e)