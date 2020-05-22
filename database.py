import pyodbc
class Database():
    def __init__(self):
        self.connection = None

    def __del__(self):
        if self.connection != None:
            self.connection.close()

    # Need to replace single ' with '' in order to appease SQL. '' counts as a ' literal, so if the user types in words like
    # it's or there's.
    def sqlFormat(self, toBeFormatted):
        toBeFormatted.replace('\'', '\'\'')
        return toBeFormatted


    def getConnection(self):
        if self.connection == None:
            self.connection = pyodbc.connect('Driver={SQL Server}; Server=BATTLESTATION;Database=ObscurWitMe; Trusted_Connection=yes')
        return self.connection

    # This selects all categories for a specified InterestID
    def getAllCategoriesForInterest(self, interestID):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'SELECT * FROM Category WHERE CategoryID IN (SELECT CategoryID FROM InterestCategory WHERE InterestID = ' + str(interestID) + ')'
        cursor.execute(query)
        return cursor

    # This selects all interests for a specified categoryID
    def getAllInterestForCategory(self, categoryID):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'SELECT * FROM Interest WHERE InterestID IN (SELECT InterestID FROM InterestCategory WHERE CategoryID = ' + str(categoryID) + ')'
        cursor.execute(query)
        return cursor

    # This selects all interests for a specified interestID
    def getAllUsersForInterest(self, interestID):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'SELECT * FROM UserAccount WHERE UserID IN (SELECT UserID from UserInterest WHERE InterestID = ' + str(interestID) + ')'
        cursor.execute(query)
        return cursor

    # Creates an entry in the UserInterest table that links the specified userID and interestID together
    def createUserInterest(self, userID, interestID):
        c = self.getConnection()
        cursor = c.cursor()
        cursor.execute('INSERT INTO UserInterest (UserID, InterestID) VALUES (' + str(userID) + ', ' + str(interestID) + ')')
        affectedRows = cursor.rowcount
        if (affectedRows > 0):
            c.commit()
        else:
            c.rollback()
        return affectedRows

    # Creates an entry in the InterestCategory table that links the specified interestID and categoryID together
    def createInterestCategory(self, interestID, categoryID):
        c = self.getConnection()
        cursor = c.cursor()
        cursor.execute('INSERT INTO InterestCategory (InterestID, CategoryID) VALUES (' + str(interestID) + ', ' + str(categoryID) + ')')
        affectedRows = cursor.rowcount
        if (affectedRows > 0):
            c.commit()
        else:
            c.rollback()
        return affectedRows

    # On an update, the only required parameter is which user we are updating, blank parameters will not be updated to blank,
    # but skipped.
    def updateUserAccount(self, userID, email='', password='', firstName='', lastName='', age='', location=''):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'UPDATE UserAccount SET '
        if (email != ''):
            query += 'Email = \'' + self.sqlFormat(email) + '\', '
        if (password != ''):
            query += 'Password = \'' + self.sqlFormat(password) + '\', '
        if (firstName != ''):
            query += 'FirstName = \'' + self.sqlFormat(firstName) + '\', '
        if (lastName != ''):
            query += 'LastName = \'' + self.sqlFormat(lastName) + '\', '
        if (age != ''):
            query += 'Age =  ' + str(age) + ', '
        if (location != ''):
            query += 'Location = \'' + location + '\', '
        # This is needed to remove the comma and space from the end of the query
        query = query[0:len(query) - 2]
        query += ' WHERE UserID = ' + str(userID)
        cursor.execute(query)
        affectedRows = cursor.rowcount
        if (affectedRows > 0):
            c.commit()
        else:
            c.rollback()
        return affectedRows

    # Every user needs an email and a password in order to create an account
    def createUserAccount(self, email, password):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'INSERT INTO UserAccount (Email, Password) VALUES ( \'' + self.sqlFormat(email) + '\',\'' + self.sqlFormat(password) + '\')'
        cursor.execute(query)
        affectedRows = cursor.rowcount
        if (affectedRows > 0):
            c.commit()
        else:
            c.rollback()
        return affectedRows

    # This creates an interest page with the given name and description
    def createInterest(self, name, description):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'INSERT INTO Interest (Name, Description) VALUES ( \'' + self.sqlFormat(name) + '\',\'' + self.sqlFormat(description) + '\')'
        cursor.execute(query)
        affectedRows = cursor.rowcount
        if (affectedRows > 0):
            c.commit()
        else:
            c.rollback()
        return affectedRows

    # This creates a category page with the given name and description
    def createCategory(self, name, description):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'INSERT INTO Category (Name, Description) VALUES ( \'' + self.sqlFormat(name) + '\',\'' + self.sqlFormat(description) + '\')'
        cursor.execute(query)
        affectedRows = cursor.rowcount
        if (affectedRows > 0):
            c.commit()
        else:
            c.rollback()
        return affectedRows

    # This creates a message from fromUserID to toUserID with the given body
    def createMessage(self, fromUserID, toUserID, body):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'INSERT INTO Message (FromUserID, ToUserID, Body, Timestamp) VALUES (' + str(fromUserID) + ', ' + str(toUserID) + ', \'' + self.sqlFormat(body) + '\', CURRENT_TIMESTAMP)'
        cursor.execute(query)
        affectedRows = cursor.rowcount
        if (affectedRows > 0):
            c.commit()
        else:
            c.rollback()
        return affectedRows

    # This selects all messages with the specified user as the sender.
    def getSentMessages(self, userID):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'SELECT * FROM Message WHERE FromUserID = ' + str(userID)
        cursor.execute(query)
        return cursor

    # This selects all messages with the specified user as the recipient.
    def getReceivedMessages(self, userID):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'SELECT * FROM Message WHERE ToUserID = ' + str(userID)
        cursor.execute(query)
        return cursor

    # This selects all categories from the Category table
    def getAllCategories(self):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'SELECT * FROM Category'
        cursor.execute(query)
        return cursor

    # This selects all interests from the Interest table
    def getAllInterest(self):
        c = self.getConnection
        cursor = c.cursor()
        query = 'SELECT * FROM Interest'
        cursor.execute(query)
        return cursor

    def getUserByEmail(self, email):
        c = self.getConnection()
        cursor = c.cursor()
        query = 'SELECT * FROM UserAccount WHERE Email = \'' + self.sqlFormat(email) + '\'' 
        cursor.execute(query)
        return cursor

    # This will execute the given select query (it will execute every query but will not commit changes,
    # So use executeQueryWithCommit for queries that change the database).
    # The cursor object contains all of the results which can be accessed as follows:
    # rows = cursor.fetchall()
    # for row in rows:
    #   print (row.Description, row.Name)
    # And so on. The row object has attributes that match the names of the columns of the table
    # Or at least the columns retrieved.
    def executeQuery(self, query):
        c = self.getConnection()
        cursor = c.cursor()
        cursor.execute(query)
        return cursor

    # This will attempt to execute the given query and commit it. This is needed for
    # both insert and update queries
    # affectedRows will be greater than 0 if the insert was successful
    # affectedRows will be greater than 0 if a row was updated, but 0 if no rows were updated
    # (This includes where the row does not exist and also where the provided information to update
    # was the same as the information already there.)
    def executeQueryWithCommit(self, query):
        c = self.getConnection()
        cursor = c.cursor()
        cursor.execute(query)
        affectedRows = cursor.rowcount
        if (affectedRows > 0):
            c.commit()
        else:
            c.rollback()
        return affectedRows
