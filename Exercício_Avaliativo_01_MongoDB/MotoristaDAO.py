from pymongo import MongoClient
from bson.objectid import ObjectId
from Corrida import Corrida
from Passageiro import Passageiro
from Motorista import Motorista

class motoristaModel:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, Motoristas:Motorista, Corridas:Corrida, Passageiros:Passageiro):
        try:
            res = self.db.collection.insert_one({"nota": Motoristas.nota, "nota": Corridas.nota, "distancia": Corridas.distancia, "valor": Corridas.valor, "nome": Passageiros.nome, "documento": Passageiros.documento})
            print(f"Motorista created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, id: str, Motoristas:Motorista, Corridas:Corrida, Passageiros: Passageiro):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota": Motoristas.nota, "nota": Corridas.nota, "distancia": Corridas.distancia, "valor": Corridas.valor, "nome": Passageiros.nome, "documento": Passageiros.documento}})
            print(f"Motorista updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None