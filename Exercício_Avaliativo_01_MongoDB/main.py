from database import Database
from writeAJson import writeAJson
from MotoristaDAO import motoristaModel
from MotoristaCLI import motoristaCLI

db = Database(database="Exercicio_Avaliativo_01_MongoDB", collection="Motoristas")
MotoristaDAO = motoristaModel(database=db)

motoristaAUX = motoristaCLI(MotoristaDAO)
motoristaAUX.run()
