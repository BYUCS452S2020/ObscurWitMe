from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
import mongodatabase
from datetime import datetime


class MongoServerHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
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
        if self.path == '/getallinterests':
            response = self.get_all_interests(db)
        elif self.path == '/getAllCategories':
            response = self.get_all_categories(db)

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
            response = self.get_user(messageDict['email'], db)
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

        # send the response, current just sends back what was received
        self._set_headers()
        self.wfile.write(str.encode(json.dumps(response)))


    def get_user(self, email, db):
        response = {}
        cursor = db.getUserByEmail(email)
        for row in cursor:
            response['userid'] = str(row['_id'])
            response['firstname'] = row['firstName']
            response['lastname'] = row['lastName']
            response['age'] = row['age']
            response['location'] = row['location']
            response['password'] = row['password']
            response['email'] = row['email']
            break
        return response

    def get_all_interests(self, db):
        response = {'interests':[]}
        cursor = db.getAllInterest()
        for row in cursor:
            tmp = {}
            tmp['interestid'] = str(row['_id'])
            tmp['name'] = row['name']
            tmp['description'] = row['description']
            response['interests'].append(tmp)
        return response

    def get_all_categories(self, db):
        response = {'categories':[]}
        cursor = db.getAllCategories()
        for row in cursor:
            tmp = {}
            tmp['categoryid'] = str(row['_id'])
            tmp['name'] = row['name']
            tmp['description'] = row['description']
            response['categories'].append(tmp)
        return response

    def get_sent_messages(self, userID, db):
        response = {'sentmessages':[]}
        cursor = db.getSentMessages(userID)
        for row in cursor:
            tmp = {}
            tmp['messageid'] = str(row['_id'])
            tmp['fromid'] = row['fromUserID']
            tmp['toid'] = row['toUserID']
            tmp['body'] = row['body']
            tmp['time'] = row['_id'].getTimestamp()
            response['sentmessages'].append(tmp)
        return response

    def get_received_messages(self, userID, db):
        response = {'receivedmessages':[]}
        cursor = db.getReceivedMessages(userID)
        for row in cursor:
            tmp = {}
            tmp['messageid'] = str(row['_id'])
            tmp['fromid'] = row['fromUserID']
            tmp['toid'] = row['toUserID']
            tmp['body'] = row['body']
            tmp['time'] = row['_id'].getTimestamp()
            response['receivedmessages'].append(tmp)
        return response

    def get_category_interests(self, categoryID, db):
        response = {'interests':[]}
        cursor = db.getAllInterestForCategory(categoryID)
        for row in cursor:
            tmp = {}
            tmp['interestid'] = str(row['_id'])
            tmp['name'] = row['name']
            tmp['description'] = row['description']
            response['interests'].append(tmp)
        return response

    def get_interest_users(self, interestID, db):
        response = {'users':[]}
        cursor = db.getAllUsersForInterest(interestID)
        for row in cursor:
            tmp = {}
            tmp['userid'] = str(row['_id'])
            tmp['firstname'] = row['firstName']
            tmp['lastname'] = row['lastName']
            tmp['age'] = row['age']
            tmp['location'] = row['location']
            tmp['password'] = row['password']
            tmp['email'] = row['email']
            response['users'].append(tmp)
        return response

    def get_user_interests(self, userID, db):
        response = {'interests':[]}
        cursor = db.getAllInterestsForUser(userID)
        for row in cursor:
            tmp = {}
            tmp['interestid'] = str(row['_id'])
            tmp['name'] = row['name']
            tmp['description'] = row['description']
            response['interests'].append(tmp)
        return response

    def create_user(self, messageDict, db):
        response = {}
        email = messageDict['email']
        password = messageDict['password']
        num = db.createUserAccount(email, password)
        response['userid'] = num

    def update_user(self, messageDict, db):
        response = {}
        id = messageDict['userid']
        email = messageDict['email']
        password = messageDict['password']
        firstName = messageDict['first']
        lastName = messageDict['last']
        age = messageDict['age']
        location = messageDict['location']
        num = db.updateUserAccount(id, email, password, firstName, lastName, age, location)
        response['success'] = num
        return response

    def create_interest(self, messageDict, db):
        response = {}
        name = messageDict['name']
        des = messageDict['description']
        num = db.createInterest(name, des)
        response['interestid'] = num
        return response

    def create_message(self, messageDict, db):
        response = {}
        fromID = messageDict['fromid']
        toID = messageDict['toid']
        body = messageDict['body']
        num = db.createMessage(fromID, toID, body)
        response['messageid'] = num
        return response

    def create_category(self, messageDict, db):
        response = {}
        name = messageDict['name']
        des = messageDict['description']
        num = db.createCategory(name, des)
        response['categoryid'] = num
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


httpd = HTTPServer(('localhost', 8000), MongoServerHandler)
httpd.serve_forever()
