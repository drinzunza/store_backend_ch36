import pymongo
import certifi

con_str = "mongodb+srv://FSDI:Test1234@cluster0.aws7mpm.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database('organika')