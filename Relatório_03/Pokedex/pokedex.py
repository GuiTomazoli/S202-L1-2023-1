from database import Database

class Pokedex:
    def __init__(self):
        self.db = Database(database="pokedex", collection="pokemons")

    def fraquezanum(self, num):  
        return self.db.collection.find({"weaknesses": {"$size": num}}) #pokemons que tem duas fraqueza.

    def tipofraquezas(self, num):
        fraquezas = ["Water", "Grass"]
        return self.db.collection.find({"weaknesses": {"$all": fraquezas}}) #pokemons fracos contra água e grama.

    def fogoevolucao(self, num):
        tipo = ["Fire"]
        return self.db.collection.find({ "type": {"$in": tipo}, "next_evolution": {"$exists": True} }) #pokemons do tipo fogo que tem evoluções.

    def psiquicos(self, num):
        return self.db.collection.find({"$or": [{"type":"Psychic"},{"weaknesses": "Psychic"}]})#pokemons psiquicos ou fracos contra psiquicos.

    def fraquezacontralutador(self, num):
        return self.db.collection.find({"weaknesses": "Fighting"}) #pokemons fracos contra o tipo lutador    


