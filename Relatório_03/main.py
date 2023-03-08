from database import Database
from Pokedex.pokedex import Pokedex
from helper.writeAJson import writeAJson

pokemons = Pokedex()

writeAJson(pokemons.fraquezanum(2), "numdeFraq")
writeAJson(pokemons.tipofraquezas(2), "tipodeFraq")
writeAJson(pokemons.fogoevolucao(1), "evolucaotipoFogo")
writeAJson(pokemons.psiquicos(2), "pokemonspsychicFraq")
writeAJson(pokemons.fraquezacontralutador(1), "fracocontraLutador")

