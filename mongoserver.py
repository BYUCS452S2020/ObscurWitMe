from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
import mongodatabase
from datetime import datetime


class MongoServerHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    #this is for getting from the database
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response = {}
        db = mongodatabase.MongoDatabase()
        #####implement code here for accessing database and parsing into tmpdict
        #pyodbc code
        #if self.path == '/getuser':   #get a user
        #    pass
#        elif self.path == 'getuserinterests': #get a interest
#            pass
#        elif self.path == 'getcategoryinterests':
#            pass
#        elif self.path == 'getsentmessages':
#            pass
#        elif self.path == 'getreceivedmessages':
#            pass
#        elif self.path == 'getinterestusers':
#            pass
        

        #####
        #write dictionary to json to send to client
        self.wfile.write(str.encode(json.dumps(response)))


    #this is for inserting into the database
    def do_POST(self):

        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        messageDict = json.loads(self.rfile.read(length))
        response = {}
        db = mongodatabase.MongoDatabase()
        ###parse data to know what table to insert into
        #####implement code to insert messageDict into database
        if self.path == '/createuser':  #insert user
            response = self.create_user(messageDict, db)
        elif self.path == '/updateuser':
            response = self.update_user(messageDict, db)
        elif self.path == '/login':
            response = self.login(messageDict, db)
        elif self.path == '/createinterest':    #insert interest
            response = self.create_interest(messageDict, db)
        elif self.path == '/createcategory':
            response = self.create_category(messageDict, db)
        elif self.path == '/createmessage':
            response = self.create_message(messageDict, db)
        elif self.path == '/addinterest':
            response = self.add_interest(messageDict, db)
        elif self.path == '/addinterestcategory':
            response = self.add_interest_category(messageDict, db)
        elif self.path == '/getuser':
            response = self.get_user(messageDict, db)
        elif self.path == '/getinterest':
            response = self.get_interest(messageDict['interestid'], db)
        elif self.path == '/getcategoryinterests':
            response = self.get_category_interests(messageDict['categoryid'], db)
        elif self.path == '/getsentmessages':
            response = self.get_sent_messages(messageDict['userid'], db)
        elif self.path == '/getreceivedmessages':
            response = self.get_received_messages(messageDict['userid'], db)
        elif self.path == '/getinterestusers':
            response = self.get_interest_users(messageDict['interestid'], db)
        elif self.path == '/getuserinterests':
            response = self.get_user_interests(messageDict['userid'], db)
        elif self.path == '/getconnections':
            response = self.get_connections(messageDict['userid'], db)
        elif self.path == '/getallinterests':
            response = self.get_all_interests(db)
        elif self.path == '/getAllCategories':
            response = self.get_all_categories(db)
        

        # send the response, current just sends back what was received
        self._set_headers()
        print(response)
        self.wfile.write(str.encode(json.dumps(response)))


    def get_user(self, messageDict, db):
        if 'email' in messageDict:
            cursor = db.getUserByEmail(messageDict['email'])
        elif 'userid' in messageDict:
            cursor = db.getUserByID(messageDict['userid'])
        results = self.convertCursorToUserObjects(cursor)
        return results[0]
    
    def get_interest(self, interestID, db):
        cursor = db.getInterestByID(interestID)
        results = self.convertCursorToInterestObjects(cursor)
        return results[0]

    def get_all_interests(self, db):
        response = {'interests':[]}
        cursor = db.getAllInterest()
        results = self.convertCursorToInterestObjects(cursor)
        for item in results:
            response['interests'].append(item)
        return response

    def get_all_categories(self, db):
        response = {'categories':[]}
        cursor = db.getAllCategories()
        results = self.convertCursorToCategoryObjects(cursor)
        for item in results:
            response['categories'].append(item)
        return response

    def get_sent_messages(self, userID, db):
        response = {'sentmessages':[]}
        cursor = db.getSentMessages(userID)
        for row in cursor:
            tmp = {}
            tmp['messageid'] = str(row['_id'])
            tmp['fromid'] = str(row['fromUserID'])
            tmp['toid'] = str(row['toUserID'])
            tmp['body'] = row['body']
            tmp['time'] = '' #row['_id'].generation_time
            response['sentmessages'].append(tmp)
        return response

    def get_received_messages(self, userID, db):
        response = {'receivedmessages':[]}
        cursor = db.getReceivedMessages(userID)
        for row in cursor:
            tmp = {}
            tmp['messageid'] = str(row['_id'])
            tmp['fromid'] = str(row['fromUserID'])
            tmp['toid'] = str(row['toUserID'])
            tmp['body'] = row['body']
            tmp['time'] = '' #row['_id'].generation_time
            response['receivedmessages'].append(tmp)
        return response

    def get_category_interests(self, categoryID, db):
        response = {'interests':[]}
        cursor = db.getAllInterestForCategory(categoryID)
        results = self.convertCursorToInterestObjects(cursor)
        for item in results:
            response['interests'].append(item)
        return response

    def get_interest_users(self, interestID, db):
        response = {'users':[]}
        cursor = db.getAllUsersForInterest(interestID)
        results = self.convertCursorToUserObjects(cursor)
        for item in results:
            response['users'].append(item)
        return response

    def get_user_interests(self, userID, db):
        response = {'interests':[]}
        cursor = db.getAllInterestsForUser(userID)
        results = self.convertCursorToInterestObjects(cursor)
        for item in results:
            response['interests'].append(item)
        return response

    def create_user(self, messageDict, db):
        response = {}
        email = messageDict['email']
        password = messageDict['password']
        num = db.createUserAccount(email, password)
        response['userid'] = str(num)
        messageDict['userid'] = str(num)
        self.update_user(messageDict, db)
        return response

    def update_user(self, messageDict, db):
        response = {}
        id = messageDict['userid']
        email = messageDict['email']
        password = messageDict['password']
        firstName = messageDict['firstname']
        lastName = messageDict['lastname']
        age = messageDict['age']
        location = messageDict['location']
        num = db.updateUserAccount(id, email, password, firstName, lastName, age, location)
        response['success'] = str(num)
        return response

    def create_interest(self, messageDict, db):
        response = {}
        name = messageDict['name']
        des = messageDict['description']
        url = messageDict['imageURL']
        categories = messageDict['categories']
        num = db.createInterest(name, des, url, categories)
        response['interestid'] = str(num)
        return response

    def create_message(self, messageDict, db):
        response = {}
        fromID = messageDict['fromid']
        toID = messageDict['toid']
        body = messageDict['body']
        num = db.createMessage(fromID, toID, body)
        response['messageid'] = str(num)
        return response

    def create_category(self, messageDict, db):
        response = {}
        name = messageDict['name']
        des = messageDict['description']
        num = db.createCategory(name, des)
        response['categoryid'] = str(num)
        return response

    def add_interest(self, messageDict, db):
        response = {}
        userID = messageDict['userid']
        interestID = messageDict['interestid']
        num = db.createUserInterest(userID, interestID)
        response['success'] = True
        return response

    def add_interest_category(self, messageDict, db):
        response = {}
        interestID = messageDict['interestid']
        categoryID = messageDict['categoryid']
        num = db.createInterestCategory(interestID, categoryID)
        response['success'] = True
        return response

    def get_connections(self, userID, db):
        response = {'users': []}
        cursor = db.getConnections(userID)
        results = self.convertCursorToUserObjects(cursor)
        for item in results:
            if (str(item['userid']) != str(userID)):
                response['users'].append(item)
        return response

    def login(self, messageDict, db):
        response = {}
        email = messageDict['email']
        password = messageDict['password']
        cursor = db.login(email, password)
        id = ""
        for row in cursor:
            id = str(row['_id'])
            response['success'] = True
        if 'success' not in response:
            response['success'] = False
        response['userid'] = id
        return response

    def convertCursorToInterestObjects(self, cursor):
        result = []
        for row in cursor:
            tmp = {}
            tmp['interestid'] = str(row['_id'])
            tmp['name'] = row['name']
            tmp['description'] = row['description']
            tmp['imageURL'] = row['imageURL']
            catList = []
            for item in row['categories']:
                catList.append(str(item))
            tmp['categories'] = catList
            usList = []
            for item in row['users']:
                usList.append(str(item))
            tmp['users'] = usList
            result.append(tmp)
        return result

    def convertCursorToCategoryObjects(self, cursor):
        result = []
        for row in cursor:
            tmp = {}
            tmp['categoryid'] = str(row['_id'])
            tmp['name'] = row['name']
            tmp['description'] = row['description']
            intList = []
            for item in row['interests']:
                intList.append(str(item))
            tmp['interests'] = intList
            result.append(tmp)
        return result

    def convertCursorToUserObjects(self, cursor):
        result = []
        for row in cursor:
            tmp = {}
            tmp['userid'] = str(row['_id'])
            if ('firstName' in row):
                tmp['firstname'] = row['firstName']
            else:
                tmp['firstname'] = ''
            if ('lastName' in row):
                tmp['lastname'] = row['lastName']
            else:
                tmp['lastname'] = ''
            if ('age' in row):
                tmp['age'] = row['age']
            else:
                tmp['age'] = ''
            if ('location' in row):
                tmp['location'] = row['location']
            else:
                tmp['location'] = ''
            tmp['email'] = row['email']
            intList = []
            for item in row['interests']:
                intList.append(str(item))
            tmp['interests'] = intList
            result.append(tmp)
        return result

httpd = HTTPServer(('localhost', 8000), MongoServerHandler)
httpd.serve_forever()
