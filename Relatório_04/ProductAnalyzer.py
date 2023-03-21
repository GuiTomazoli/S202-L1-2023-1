from database import Database

class Mercado:
    def __init__(self):
        self.db = Database(database="mercado", collection="compras")

    def totalvendas(self, num): #Lista o total de vendas por dia do mercado.
        return self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": -1}},
])
    def produtomaisvendido(self, num): #Lista o produto mais vendido em todas as compras do mercado.
        return self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra", "produto": "$produtos.descricao"}, "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 6} 
])
    def gastouunicacompra(self, num): #Lista o cliente que mais gastou em uma única compra do mercado.
        return self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente:": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}    
])
    def quantidadeacimadeum(self, num): #Lista todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
        return self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"produto": "$produtos.descricao"}, "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$match": { "total": { "$gt": 1 } } }
])

    
    



