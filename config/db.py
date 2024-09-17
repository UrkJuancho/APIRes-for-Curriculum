import os
from pymongo import MongoClient

# Conexión local por defecto
conn = MongoClient()

# Conexión remota opcional (descomentar cuando sea necesario)
# MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://username:password@cluster.mongodb.net/portfolioCurriculumAPI-deploy")
# conn = MongoClient(MONGO_URI)
