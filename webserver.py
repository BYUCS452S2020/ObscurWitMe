from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
import database

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
        elif getType == 'interest': #get a interest
            pass

        #####
        #write dictionary to json to send to client
        self.wfile.write(str.encode(json.dumps(tmpDict)))


    #this is for inserting into the database
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        postType = self.headers.get('type')

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
        if postType == 'createuser':  #insert user
            response['success'] = self.create_user(messageDict)
        elif postType == 'updateuser':
            response['success'] = self.update_user(messageDict)
        elif postType == 'createinterest':    #insert interest
            response['success'] = self.create_interest(messageDict)
        elif postType == 'createmessage':
            response['success'] = self.create_message(messageDict)
        elif postType == 'addinterest':
            response['success'] = self.add_interest(messageDict)
        elif postType == 'addinterestcategory':
            response['success'] = self.add_interest_category(messageDict)

        # send the response, current just sends back what was received
        self._set_headers()
        self.wfile.write(str.encode(json.dumps(response)))

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
        id = messageDict['id']
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
