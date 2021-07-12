from pymongo import MongoClient
#import pymongo
import urllib.parse

def get_database(dbname):
	username = urllib.parse.quote_plus('admin')
	password = urllib.parse.quote_plus('16551655')

	#CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"
#	CONNECTION_STRING = 'mongodb://root:1655@localhost:27017'	# строка подключения к БД
	CONNECTION_STRING = 'mongodb://%s:%s@127.0.0.1:27017'%(username, password)

	client = MongoClient(CONNECTION_STRING)				# создание подключения к БД
#	for dbase in client.list_databases(): print(dbase)

#	print(CONNECTION_STRING)
	db = client[dbname]						# подключение к БД

	return db

if __name__ == "__main__":

	dbname = 'nl'
	db = get_database(dbname)						# подключение БД 'nl'
	#print(dbclient)
	
	posts = db[dbname]							# связка с данными в БД
	#print(posts)
	post_data = {
		'title': 'Python and MongoDB',
		'content': 'PyMongo is fun, you guys',
		'author': 'Scott'
	}
	#print(post_data)
	result = posts.insert_one(post_data)
	print('One post: {0}'.format(result.inserted_id))
#	bills_post = posts.find_one({})
#	print(bills_post)
