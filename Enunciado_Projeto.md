# Otimização da compra de computadores para uma empresa

## A empresa tem R$ 132.000 para renovar computadores dos departamento Administrativo, Desemvolvimento e Financeiro.
## A manutenção por ano e até e R$ 8.500, consumo de total de energia por mês 205 KHW

## Precisa renovar 26 máquinas no total, sendo 8 computadores no Administrativo, 6 computadores no Financeiro  e computadores no 12 Desenvolvimento. E também para cada departamento tem um valor de desempenho mínimimo definido pela a tabela abaixo:

##
| Departamento    | Desempenho mínimo | Máximo de máquinas |
| --------------- | ----------------: | -----------------: |
| Administrativo  |    **420 pontos** |                  8 |
| Financeiro      |    **450 pontos** |                  6 |
| Desenvolvimento |    **720 pontos** |                 12 |

## Existem três modelos:

| Computador | Preço por unidade | Desempenho | Consumo mensal por notebook | Manutenção anual por notebook |
| ---------- | ----------------: | ---------: | ---------------------------: | ----------------------------: |
| A          |          R$ 3.300 |  70 pontos |                        5 kWh |                        R$ 400 |
| B          |          R$ 5.000 | 110 pontos |                        8 kWh |                        R$ 300 |
| C          |          R$ 7.000 | 140 pontos |                       10 kWh |                        R$ 250 |

# Porém falando com o gerente de infraestrutura de T.I ele determinou que o departamento de Desenvolvimento deve ter no mínimo 6 computadores C, devido ao alto poder computacional exigido pelas tarefas do setor. Para não concentrar a compra em máquinas de alto custo, ficou definido também um teto de 3 computadores A nesse mesmo departamento.

# Já o setor de Patrimônio e T.I., pensando no ciclo de vida do parque de máquinas (TCO), pediu que o Administrativo e o Financeiro também garantam uma base mínima de 2 computadores do modelo C cada, por terem vida útil mais longa e reduzirem o custo total de posse a médio prazo, e um teto de 3 e 2 computadores do modelo A, evitando concentrar a compra em máquinas que precisariam ser trocadas de novo em pouco tempo.

# Diante desse cenário, qual a quantidade de cada modelo de computador (A, B ou C) que cada departamento deve comprar, de forma a minimizar o custo total da compra, respeitando o desempenho mínimo exigido, o limite de consumo de energia, a manutenção anual e as exigências específicas de cada departamento?