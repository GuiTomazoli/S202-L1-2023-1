
class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name, id):
        query = "CREATE (:Player {name: $name, id: $id})"
        parameters = {"name": name, "id": id}
        self.db.execute_query(query, parameters)

    def create_match(self, name, id, list, result):
        query = "CREATE (:Match {name: $name, id: $id, list: $list, result: $result})"
        parameters = {"name": name, "id": id, "list": list, "result": result}
        self.db.execute_query(query, parameters)

    def create_game(self, name, player_name):
        query = "MATCH (p:Player {name: $player_name}) CREATE (:Game {name: $name})<-[:JOGA]-(p)"
        parameters = {"name": name, "player_name": player_name}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_games(self):
        query = "MATCH (m:Game)<-[:JOGA]-(p:Player) RETURN m.name AS name, p.name AS player_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["player_name"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def update_match(self, old_name, new_name):
        query = "MATCH (m:Match {name: $old_name}) SET m.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def insert_match_game(self, match_name, game_name):
        query = "MATCH (m:Match {name: $match_name}) MATCH (b:Game {name: $game_name}) CREATE (m)-[:TEM]->(b)"
        parameters = {"match_name": match_name, "game_name": game_name}
        self.db.execute_query(query, parameters)

    def insert_player_game(self, player_name, game_name):
        query = "MATCH (m:Player {name: $player_name}) MATCH (b:Game {name: $game_name}) CREATE (m)-[:JOGA]->(b)"
        parameters = {"player_name": player_name, "game_name": game_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_match(self, name):
        query = "MATCH (m:Match {name: $name}) DETACH DELETE m"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_game(self, name):
        query = "MATCH (m:Match {name: $name})<-[:JOGA]-(p:Player) DETACH DELETE m"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)