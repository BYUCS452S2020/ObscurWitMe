from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
import database
from datetime import datetime


class ServerHandler(BaseHTTPRequestHandler):
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
        getType = self.headers.get('type')
        response = {}

        #####implement code here for accessing database and parsing into tmpdict
        #pyodbc code
        if getType == 'getuser':   #get a user
            pass
        elif getType == 'getuserinterests': #get a interest
            pass
        elif getType == 'getcategoryinterests':
            pass
        elif getType == 'getsentmessages':
            pass
        elif getType == 'getreceivedmessages':
            pass
        elif getType == 'getinterestusers':
            pass
        elif getType == 'getallinterests':
            pass
        elif getType == 'getAllCategories':
            pass

        #####
        #write dictionary to json to send to client
        self.wfile.write(str.encode(json.dumps(response)))


    #this is for inserting into the database
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        rType = self.headers.get('type')

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        messageDict = json.loads(self.rfile.read(length))
        response = {}
        ###parse data to know what table to insert into
        #####implement code to insert messageDict into database
        if rType == 'createuser':  #insert user
            response['success'] = self.create_user(messageDict)
        elif rType == 'updateuser':
            response['success'] = self.update_user(messageDict)
        elif rType == 'createinterest':    #insert interest
            response['success'] = self.create_interest(messageDict)
        elif rType == 'createcategory':
            response['success'] = self.create_category(messageDict)
        elif rType == 'createmessage':
            response['success'] = self.create_message(messageDict)
        elif rType == 'addinterest':
            response['success'] = self.add_interest(messageDict)
        elif rType == 'addinterestcategory':
            response['success'] = self.add_interest_category(messageDict)
        elif rType == 'getuser':
            response = self.get_user(messageDict['email'])
        elif rType == 'getallinterests':
            response = self.get_all_interests()
        elif rType == 'getallcategories':
            response = self.get_all_categories()
        elif rType == 'getcategoryinterests':
            response = self.get_category_interests(messageDict['categoryid'])
        elif rType == 'getsentmessages':
            response = self.get_sent_messages(messageDict['userid'])
        elif rType == 'getreceivedmessages':
            response = self.get_received_messages(messageDict['userid'])
        elif rType == 'getinterestusers':
            response = self.get_interest_users(messageDict['interestid'])
        elif rType == 'getuserinterests':
            response = self.get_user_interests(messageDict['userid'])

        # send the response, current just sends back what was received
        self._set_headers()
        self.wfile.write(str.encode(json.dumps(response)))


    def get_user(self, email):
        response = {}
        db = database.Database()
        cursor = db.getUserByEmail(email)
        for row in cursor:
            response['userid'] = row[0]
            response['firstname'] = row[1]
            response['lastname'] = row[2]
            response['age'] = row[3]
            response['location'] = row[4]
            response['password'] = row[5]
            response['email'] = row[6]
            break
        return response

    def get_all_interests(self):
        response = {'interests':[]}
        db = database.Database()
        cursor = db.getAllInterest()
        for row in cursor:
            tmp = {}
            tmp['interestid'] = row[0]
            tmp['name'] = row[1]
            tmp['description'] = row[2]
            response['interests'].append(tmp)
        return response

    def get_all_categories(self):
        response = {'categories':[]}
        db = database.Database()
        cursor = db.getAllCategories()
        for row in cursor:
            tmp = {}
            tmp['categoryid'] = row[2]
            tmp['name'] = row[0]
            tmp['description'] = row[1]
            response['categories'].append(tmp)
        return response

    def get_sent_messages(self, userID):
        response = {'sentmessages':[]}
        db = database.Database()
        cursor = db.getSentMessages(userID)
        for row in cursor:
            tmp = {}
            tmp['messageid'] = row[0]
            tmp['fromid'] = row[1]
            tmp['toid'] = row[2]
            tmp['body'] = row[3]
            tmp['time'] = row[4].strftime("%H:%M:%S")
            response['sentmessages'].append(tmp)
        return response

    def get_received_messages(self, userID):
        response = {'receivedmessages':[]}
        db = database.Database()
        cursor = db.getReceivedMessages(userID)
        for row in cursor:
            tmp = {}
            tmp['messageid'] = row[0]
            tmp['fromid'] = row[1]
            tmp['toid'] = row[2]
            tmp['body'] = row[3]
            tmp['time'] = row[4].strftime("%H:%M:%S")
            response['receivedmessages'].append(tmp)
        return response

    def get_category_interests(self, categoryID):
        response = {'interests':[]}
        db = database.Database()
        cursor = db.getAllInterestForCategory(categoryID)
        for row in cursor:
            tmp = {}
            tmp['interestid'] = row[0]
            tmp['name'] = row[1]
            tmp['description'] = row[2]
            response['interests'].append(tmp)
        return response

    def get_interest_users(self, interestID):
        response = {'users':[]}
        db = database.Database()
        cursor = db.getAllUsersForInterest(interestID)
        for row in cursor:
            tmp = {}
            tmp['userid'] = row[0]
            tmp['firstname'] = row[1]
            tmp['lastname'] = row[2]
            tmp['age'] = row[3]
            tmp['location'] = row[4]
            tmp['password'] = row[5]
            tmp['email'] = row[6]
            response['users'].append(tmp)
        return response

    def get_user_interests(self, userID):
        response = {'interests':[]}
        db = database.Database()
        cursor = db.getAllInterestsForUser(userID)
        for row in cursor:
            tmp = {}
            tmp['interestid'] = row[0]
            tmp['name'] = row[1]
            tmp['description'] = row[2]
            response['interests'].append(tmp)
        return response

    def create_user(self, messageDict):
        db = database.Database()
        email = messageDict['email']
        password = messageDict['password']
        num = db.createUserAccount(email, password)
        if num == 1:
            return True
        else:
            return False

    def update_user(self, messageDict):
        db = database.Database()
        id = messageDict['userid']
        email = messageDict['email']
        password = messageDict['password']
        firstName = messageDict['first']
        lastName = messageDict['last']
        age = messageDict['age']
        location = messageDict['location']
        num = db.updateUserAccount(id, email, password, firstName, lastName, age, location)
        if num == 1:
            return True
        else:
            return False

    def create_interest(self, messageDict):
        db = database.Database()
        name = messageDict['name']
        des = messageDict['description']
        num = db.createInterest(name, des)
        if num == 1:
            return True
        else:
            return False

    def create_message(self, messageDict):
        db = database.Database()
        fromID = messageDict['fromid']
        toID = messageDict['toid']
        body = messageDict['body']
        num = db.createMessage(fromID, toID, body)
        if num == 1:
            return True
        else:
            return False

    def create_category(self, messageDict):
        db = database.Database()
        name = messageDict['name']
        des = messageDict['description']
        num = db.createCategory(name, des)
        if num == 1:
            return True
        else:
            return False

    def add_interest(self, messageDict):
        db = database.Database()
        userID = messageDict['userid']
        interestID = messageDict['interestid']
        num = db.createUserInterest(userID, interestID)
        if num == 1:
            return True
        else:
            return False

    def add_interest_category(self, messageDict):
        db = database.Database()
        interestID = messageDict['interestid']
        categoryID = messageDict['categoryid']
        num = db.createInterestCategory(interestID, categoryID)
        if num == 1:
            return True
        else:
            return False


httpd = HTTPServer(('localhost', 8000), ServerHandler)
httpd.serve_forever()
