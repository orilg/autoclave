from flask.ext import mongokit as flask_mongokit
from . import config

class AutoclaveMongoKit(flask_mongokit.MongoKit):
    def connect(self):
        super(AutoclaveMongoKit, self).connect()
        flask_mongokit.ctx_stack.top.mongokit_connection.safe = True

db = AutoclaveMongoKit()

@db.register
class SampleDatabaseObject(flask_mongokit.Document):
    __collection__ = "samples"
    structure = {
        "value" : int,
    }
    default_values = {"value" : 100}

#################################### models ####################################
# @db.register
# class User(flask_mongokit.Document):
#     __collection__ = "users"
#     structure = {
#         "email" : unicode,
#     }
#     indexes = [
#         {
#             "fields" : ["email"],
#             "unique" : True,
#         }
#     ]
