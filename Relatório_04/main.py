from database import Database
from ProductAnalyzer import Mercado
from writeAJson import writeAJson

compras = Mercado()

writeAJson(compras.totalvendas(), "Total de vendas por dia")
writeAJson(compras.produtomaisvendido(), "Produto mais vendido em todas as compras")
writeAJson(compras.gastouunicacompra(), "Cliente que mais gastou em uma única compra")
writeAJson(compras.quantidadeacimadeum(), "Todos os produtos que tiveram uma quantidade vendida acima de uma unidades.")
