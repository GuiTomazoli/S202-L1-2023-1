from database import Database
from writeAJson import writeAJson
#from personModel import PersonModel
#from cli import PersonCLI
from bookModel import BookModel
from cli_livros import BookCLI


#db = Database(database="relatorio_05", collection="pessoas")
#personModel = PersonModel(database=db)


#personCLI = PersonCLI(personModel)
#personCLI.run()

db = Database(database="relatorio_05", collection="livros")
bookModel = BookModel(database=db)


bookCLI = BookCLI(bookModel)
bookCLI.run()
