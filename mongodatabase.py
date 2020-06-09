import pymongo
from bson import ObjectId

class MongoDatabase():
    def __init__(self):
        self.connection = None

    def __del__(self):
        if self.connection != None:
            self.connection.close()

    def getConnection(self):
        if self.connection == None:
            self.connection = pymongo.MongoClient('mongodb://localhost')
        return self.connection.obscurwitme

    # This selects all categories for a specified InterestID
    def getAllCategoriesForInterest(self, interestID):
        db = self.getConnection()
        query = {"interestID": ObjectId(interestID)}
        cursor = db.interestcategory.find(query)
        query = {"$or": []}
        for c in cursor:
            query["$or"].append({"_id": c["categoryID"]})
        cursor = db.category.find(query)
        return cursor

    # This selects all interests for a specified categoryID
    def getAllInterestForCategory(self, categoryID):
        db = self.getConnection()
        query = {"categoryID": ObjectId(categoryID)}
        cursor = db.interestcategory.find(query)
        query = {"$or": []}
        for c in cursor:
            query["$or"].append({"_id": c["interestID"]})
        cursor = db.interest.find(query)
        return cursor

    # This selects all users for a specified interestID
    def getAllUsersForInterest(self, interestID):
        db = self.getConnection()
        query = {"interestID": ObjectId(interestID)}
        cursor = db.userinterest.find(query)
        query = {"$or": []}
        for c in cursor:
            query["$or"].append({"_id": c["userID"]})
        cursor = db.user.find(query)
        return cursor

    # This selects all interests for a specified userID
    def getAllInterestsForUser(self, userID):
        db = self.getConnection()
        query = {"userID": ObjectId(userID)}
        cursor = db.userinterest.find(query)
        query = {"$or": []}
        for c in cursor:
            query["$or"].append({"_id": c["interestID"]})
        cursor = db.interest.find(query)
        return cursor

    # Creates an entry in the UserInterest table that links the specified userID and interestID together
    def createUserInterest(self, userID, interestID):
        db = self.getConnection()
        doc = {"userID": userID, "interestID": interestID}
        x = db.userinterest.insert_one(doc)
        return x.inserted_id

    # Creates an entry in the InterestCategory table that links the specified interestID and categoryID together
    def createInterestCategory(self, interestID, categoryID):
        db = self.getConnection()
        doc = {"interestID": interestID, "categoryID": categoryID}
        x = db.interestcategory.insert_one(doc)
        return x.inserted_id

    # On an update, the only required parameter is which user we are updating, blank parameters will not be updated to blank,
    # but skipped.
    def updateUserAccount(self, userID, email='', password='', firstName='', lastName='', age='', location=''):
        db = self.getConnection()
        update = {"$set": {}}
        if (email != ''):
            update["$set"]['email'] = email
        if (password != ''):
            update["$set"]['password'] = password
        if (firstName != ''):
            update["$set"]['firstName'] = firstName
        if (lastName != ''):
            update["$set"]['lastName'] = lastName
        if (age != ''):
            update["$set"]['age'] = age
        if (location != ''):
            update["$set"]['location'] = location

        filter = {"_id": userID}
        cursor = db.user.update_one(filter, update)
        return cursor.matched_count

    # Every user needs an email and a password in order to create an account, returns id of document
    def createUserAccount(self, email, password):
        db = self.getConnection()
        doc = {"email": email, "password": password}
        x = db.user.insert_one(doc)
        return x.inserted_id

    # This creates an interest page with the given name and description
    def createInterest(self, name, description):
        db = self.getConnection()
        doc = {"name": name, "description": description}
        x = db.interest.insert_one(doc)
        return x.inserted_id

    # This creates a category page with the given name and description
    def createCategory(self, name, description):
        db = self.getConnection()
        doc = {"name": name, "description": description}
        x = db.category.insert_one(doc)
        return x.inserted_id

    # This creates a message from fromUserID to toUserID with the given body
    def createMessage(self, fromUserID, toUserID, body):
        db = self.getConnection()
        doc = {"fromUserID": fromUserID, "toUserID": toUserID, "body": body}
        x = db.message.insert_one(doc)
        return x.inserted_id

    # This selects all messages with the specified user as the sender.
    def getSentMessages(self, userID):
        db = self.getConnection()
        query = {"fromUserID": userID}
        cursor = db.message.find(query)
        return cursor

    # This selects all messages with the specified user as the recipient.
    def getReceivedMessages(self, userID):
        db = self.getConnection()
        query = {"toUserID": userID}
        cursor = db.message.find(query)
        return cursor

    # This selects all categories from the Category collection
    def getAllCategories(self):
        db = self.getConnection()
        cursor = db.category.find()
        return cursor

    # This selects all interests from the Interest collection
    def getAllInterest(self):
        db = self.getConnection()
        cursor = db.interest.find()
        return cursor

    def getUserByEmail(self, email):
        db = self.getConnection()
        query = {"email": email}
        cursor = db.user.find(query)
        return cursor

    def login(self, email, password):
        db = self.getConnection()
        query = {"email": email, "password": password}
        cursor = db.user.find(query)
        return cursor