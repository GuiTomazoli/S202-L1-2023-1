from database import Database
from ProductAnalyzer import Mercado
from writeAJson import writeAJson

compras = Mercado()

writeAJson(compras.totalvendas(1), "Total de vendas por dia")
writeAJson(compras.produtomaisvendido(1), "Produto mais vendido em todas as compras")
writeAJson(compras.gastouunicacompra(1), "Cliente que mais gastou em uma única compra")
writeAJson(compras.quantidadeacimadeum(1), "Todos os produtos que tiveram uma quantidade vendida acima de uma unidades.")
