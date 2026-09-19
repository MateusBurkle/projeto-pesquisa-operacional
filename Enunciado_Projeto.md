# Otimização da compra de computadores para uma empresa

## A empresa tem R$ 132.000 para renovar computadores dos departamento Administrativo, Desenvolvimento e Financeiro.
## A manutenção por ano e até e R$ 8.500, consumo de total de energia por mês 205 KHW

## Precisa renovar 26 máquinas no total, sendo 8 computadores no Administrativo, 6 computadores no Financeiro  e computadores no 12 Desenvolvimento. E também para cada departamento tem um valor de desempenho mínimo definido pela a tabela abaixo:

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
| C          |          R$ 6.500 | 140 pontos |                       10 kWh |                        R$ 250 |

## Porém falando com o gerente de infraestrutura de T.I ele determinou que o departamento de Desenvolvimento deve ter no mínimo 6 computadores C, devido ao alto poder computacional exigido pelas tarefas do setor. Para não concentrar a compra em máquinas de alto custo, ficou definido também um teto de 3 computadores A nesse mesmo departamento.

## Já o setor de Patrimônio e T.I., pensando no ciclo de vida do parque de máquinas (TCO), pediu que o Administrativo e o Financeiro também garantam uma base mínima de 2 computadores do modelo C cada, por terem vida útil mais longa e reduzirem o custo total de posse a médio prazo, e um teto de 3 e 2 computadores do modelo A, evitando concentrar a compra em máquinas que precisariam ser trocadas de novo em pouco tempo.

## Diante desse cenário, qual a quantidade de cada modelo de computador (A, B ou C) que cada departamento deve comprar, de forma a minimizar o custo total da compra, respeitando o desempenho mínimo exigido, o limite de consumo de energia, a manutenção anual e as exigências específicas de cada departamento?

## Explicação da modelagem

### Variáveis de decisão
Para cada departamento (Administrativo, Financeiro, Desenvolvimento) foi criada uma variável para cada modelo de computador (A, B, C), representando a quantidade que será comprada. Por exemplo, `a_adm` é a quantidade de computadores A comprados para o Administrativo.

### Restrições de desempenho mínimo por departamento
Cada departamento tem uma pontuação mínima de desempenho a atingir (420, 450 e 720 pontos). Essa restrição soma o desempenho dos computadores escolhidos para o departamento e garante que o total não fique abaixo do mínimo exigido, pois máquinas insuficientes prejudicariam o trabalho do setor.

### Restrição de quantidade de máquinas por departamento
Cada departamento precisa renovar um número fixo de máquinas (8 no Administrativo, 6 no Financeiro e 12 no Desenvolvimento). A restrição de igualdade garante que exatamente essa quantidade seja comprada, nem mais nem menos.

### Restrição de consumo de energia
A empresa tem um limite de 205 kWh de consumo mensal. A restrição soma o consumo de todos os computadores comprados, somando os três departamentos, e impede que esse total ultrapasse o limite estabelecido.

### Restrição de manutenção anual
Existe um teto de R$ 8.500 por ano para manutenção. A restrição soma o custo de manutenção anual de todos os computadores comprados e garante que esse total não ultrapasse o orçamento disponível para manutenção.

### Restrições específicas do Administrativo
- Máximo de 3 computadores A: evita concentrar a compra em máquinas mais baratas, porém com vida útil menor.
- Mínimo de 2 computadores C: garante uma base de máquinas com vida útil mais longa, reduzindo o custo total de posse (TCO) a médio prazo.

### Restrições específicas do Financeiro
- Máximo de 2 computadores A e mínimo de 2 computadores C: segue a mesma lógica definida pelo setor de Patrimônio e T.I. para o Administrativo, limitando máquinas de troca rápida e garantindo uma base de máquinas mais duráveis.

### Restrições específicas do Desenvolvimento
- Mínimo de 6 computadores C: atende à exigência do gerente de T.I., já que o setor precisa de alto poder computacional para suas tarefas.
- Máximo de 3 computadores A: evita concentrar a compra em máquinas de baixo desempenho, o que comprometeria as tarefas do setor.

### Restrição de orçamento
A empresa possui R$ 132.000 disponíveis para a compra. Essa restrição garante que o custo total de todos os computadores comprados, somando os três departamentos, não ultrapasse esse valor.

### Função objetivo
O objetivo do modelo é minimizar o custo total da compra. Ou seja, entre todas as combinações de computadores que satisfazem as restrições acima, o modelo busca a combinação de menor custo para a empresa.

### Verificação do status da solução
Antes de exibir os resultados, o código verifica se o solver realmente encontrou uma solução ótima (`status == pywraplp.Solver.OPTIMAL`). Isso é importante porque, se alguma restrição fosse alterada e o problema se tornasse inviável (por exemplo, um orçamento baixo demais para atingir o desempenho mínimo exigido), o solver não teria uma resposta válida. Sem essa verificação, o código imprimiria valores sem sentido; com ela, o programa avisa que não foi possível encontrar uma solução ótima.