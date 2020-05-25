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
        db = database.Database()
        ###parse data to know what table to insert into
        #####implement code to insert messageDict into database
        if postType == 'createuser':  #insert user
            email = messageDict['email']
            password = messageDict['password']
            num = db.createUserAccount(email, password)
            if num == 1:
                response['success'] = True
            else:
                response['success'] = False
        elif postType == 'updateuser':
            pass
        elif postType == 'interest':    #insert interest
            pass


        # send the response, current just sends back what was received
        self._set_headers()
        self.wfile.write(str.encode(json.dumps(messageDict)))



httpd = HTTPServer(('localhost', 8000), ServerHandler)
httpd.serve_forever()
