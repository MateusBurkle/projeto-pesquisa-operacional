# Otimização da compra de computadores para uma empresa (versão com dados em JSON)

## Contexto

A empresa tem R$ 132.000 para renovar computadores dos departamentos Administrativo, Desenvolvimento e Financeiro.
A manutenção por ano é de até R$ 8.500 e o consumo total de energia por mês é de até 205 kWh.

Precisa renovar 26 máquinas no total: 8 computadores no Administrativo, 6 no Financeiro e 12 no Desenvolvimento. Além disso, cada departamento tem um desempenho mínimo definido pela tabela abaixo:

| Departamento    | Desempenho mínimo | Quantidade de máquinas |
| --------------- | ----------------: | ---------------------: |
| Administrativo  |    **420 pontos** |                      8 |
| Financeiro      |    **450 pontos** |                      6 |
| Desenvolvimento |    **720 pontos** |                     12 |

Existem três modelos de computador:

| Computador | Preço por unidade | Desempenho | Consumo mensal por máquina | Manutenção anual por máquina |
| ---------- | ----------------: | ---------: | -------------------------: | ---------------------------: |
| A          |          R$ 3.300 |  70 pontos |                      5 kWh |                       R$ 400 |
| B          |          R$ 5.000 | 110 pontos |                      8 kWh |                       R$ 300 |
| C          |          R$ 6.500 | 140 pontos |                     10 kWh |                       R$ 250 |

## Exigências específicas de cada departamento

- **Desenvolvimento:** o gerente de infraestrutura de T.I. determinou no mínimo 6 computadores C, devido ao alto poder computacional exigido pelas tarefas do setor. Para não concentrar a compra em máquinas de alto custo, ficou definido também um teto de 3 computadores A.
- **Administrativo e Financeiro:** o setor de Patrimônio e T.I., pensando no ciclo de vida do parque de máquinas (TCO), pediu uma base mínima de 2 computadores C em cada um, por terem vida útil mais longa e reduzirem o custo total de posse a médio prazo. Pediu também um teto de 3 computadores A no Administrativo e de 2 no Financeiro, evitando concentrar a compra em máquinas que precisariam ser trocadas de novo em pouco tempo.

## Novidade: os dados agora ficam no arquivo `dados.json`

Nesta versão do projeto, **nenhum número do problema fica escrito no código**. Todos os valores (orçamento, limites, scores, preços, desempenho, consumo, manutenção, máximos de A e mínimos de C) são lidos do arquivo [dados.json](dados.json). **Qualquer mudança no cenário deve ser feita nesse arquivo**, e o `main_n2.py` não deve ser alterado para isso.

### Estrutura do `dados.json`

```json
{
  "departamentos": {
    "administrativo":  { "quantidade": 8,  "score": 420, "max_a": 3, "min_c": 2 },
    "financeiro":      { "quantidade": 6,  "score": 450, "max_a": 2, "min_c": 2 },
    "desenvolvimento": { "quantidade": 12, "score": 720, "max_a": 3, "min_c": 6 }
  },
  "computadores": {
    "A": { "desempenho": 70,  "energia": 5,  "manutencao": 400, "custo": 3300 },
    "B": { "desempenho": 110, "energia": 8,  "manutencao": 300, "custo": 5000 },
    "C": { "desempenho": 140, "energia": 10, "manutencao": 250, "custo": 6500 }
  },
  "limites": {
    "energia": 205,
    "manutencao": 8500,
    "orcamento": 132000
  }
}
```

| Campo | O que representa |
| ----- | ---------------- |
| `quantidade` | Número exato de máquinas que o departamento precisa receber |
| `score` | Desempenho mínimo exigido do departamento |
| `max_a` | Máximo de computadores A no departamento |
| `min_c` | Mínimo de computadores C no departamento |
| `desempenho`, `energia`, `manutencao`, `custo` | Características de cada modelo (por unidade) |
| `limites.energia` | Consumo mensal máximo, em kWh |
| `limites.manutencao` | Manutenção anual máxima, em R$ |
| `limites.orcamento` | Orçamento máximo de compra, em R$ |

### Cenário: por que mexer no JSON é melhor do que mexer no código

Imagine que o analista financeiro da empresa recebe, em uma reunião, três notícias na mesma semana:

1. A diretoria reduziu o orçamento de compra de R$ 132.000 para R$ 125.000.
2. O fornecedor renegociou o preço do modelo B, que passou de R$ 5.000 para R$ 4.700.
3. O Financeiro ganhou uma vaga e agora precisa de 7 máquinas, e não mais 6.

O analista entende do negócio, mas **não é programador**. Compare as duas formas de simular esses cenários:

| | Alterando o código | Alterando o `dados.json` |
| --- | --- | --- |
| **Onde mexer** | Em várias linhas espalhadas pelo `.py` (variáveis, restrições, função objetivo) | Em um único arquivo, só nos valores |
| **Quem pode fazer** | Quem sabe Python e OR-Tools | Qualquer pessoa que consiga editar um texto |
| **Risco de erro** | Alto: um valor esquecido em uma das restrições deixa o modelo inconsistente (por exemplo, trocar o preço no custo, mas não na função objetivo) | Baixo: cada valor existe em um único lugar e é usado em todas as restrições |
| **Lógica do modelo** | Pode ser quebrada sem querer ao editar o arquivo | Fica intacta: o código não é tocado |
| **Testar vários cenários** | Cada teste exige editar, salvar e conferir o código | Basta manter cópias do JSON (`dados_cenario1.json`, `dados_cenario2.json`...) |
| **Rastreabilidade** | Difícil saber o que mudou entre uma execução e outra | Os dados de cada simulação ficam registrados e podem ser comparados |

Neste cenário, o analista edita apenas estes valores:

```json
"limites": { "energia": 205, "manutencao": 8500, "orcamento": 125000 }
"B": { "desempenho": 110, "energia": 8, "manutencao": 300, "custo": 4700 }
"financeiro": { "quantidade": 7, "score": 450, "max_a": 2, "min_c": 2 }
```

Depois é só rodar o programa de novo. Se a nova combinação não for possível, o solver avisa que não encontrou solução ótima, e o analista descobre na hora que alguma das notícias inviabiliza a compra, sem precisar abrir o código.

> **Observação:** o JSON permite mudar os **valores** do problema, mas não a sua **estrutura**. Acrescentar um quarto modelo de computador (D) ou um quarto departamento ainda exige alterar o código, porque seriam novas variáveis de decisão.

## Pergunta do problema

Diante desse cenário, qual a quantidade de cada modelo de computador (A, B ou C) que cada departamento deve comprar, de forma a minimizar o custo total da compra, respeitando o desempenho mínimo exigido, o limite de consumo de energia, a manutenção anual e as exigências específicas de cada departamento?

## Explicação da modelagem

### Leitura dos dados
Ao iniciar, o programa abre o `dados.json` com o módulo `json` do Python e guarda os valores em variáveis. Todas as restrições e a função objetivo usam essas variáveis, e não números escritos diretamente no código. O caminho do arquivo é montado a partir da pasta do próprio programa, então ele funciona independentemente de onde for executado.

### Variáveis de decisão
Para cada departamento (Administrativo, Financeiro, Desenvolvimento) foi criada uma variável para cada modelo de computador (A, B, C), representando a quantidade que será comprada. Por exemplo, `a_adm` é a quantidade de computadores A comprados para o Administrativo. O limite superior de cada variável é a `quantidade` de máquinas do departamento, lida do JSON.

### Restrições de desempenho mínimo por departamento
Cada departamento tem uma pontuação mínima de desempenho a atingir (`score` no JSON). Essa restrição soma o desempenho dos computadores escolhidos para o departamento e garante que o total não fique abaixo do mínimo exigido, pois máquinas insuficientes prejudicariam o trabalho do setor.

### Restrição de quantidade de máquinas por departamento
Cada departamento precisa renovar um número fixo de máquinas (`quantidade` no JSON). A restrição de igualdade garante que exatamente essa quantidade seja comprada, nem mais nem menos.

### Restrição de consumo de energia
A empresa tem um limite de consumo mensal (`limites.energia`). A restrição soma o consumo de todos os computadores comprados, somando os três departamentos, e impede que esse total ultrapasse o limite estabelecido.

### Restrição de manutenção anual
Existe um teto anual para manutenção (`limites.manutencao`). A restrição soma o custo de manutenção anual de todos os computadores comprados e garante que esse total não ultrapasse o orçamento disponível para manutenção.

### Restrições específicas do Administrativo
- Máximo de computadores A (`max_a`): evita concentrar a compra em máquinas mais baratas, porém com vida útil menor.
- Mínimo de computadores C (`min_c`): garante uma base de máquinas com vida útil mais longa, reduzindo o custo total de posse (TCO) a médio prazo.

### Restrições específicas do Financeiro
- Máximo de computadores A e mínimo de computadores C (`max_a` e `min_c`): seguem a mesma lógica definida pelo setor de Patrimônio e T.I. para o Administrativo, limitando máquinas de troca rápida e garantindo uma base de máquinas mais duráveis.

### Restrições específicas do Desenvolvimento
- Mínimo de computadores C (`min_c`): atende à exigência do gerente de T.I., já que o setor precisa de alto poder computacional para suas tarefas.
- Máximo de computadores A (`max_a`): evita concentrar a compra em máquinas de baixo desempenho, o que comprometeria as tarefas do setor.

### Restrição de orçamento
A empresa possui um valor disponível para a compra (`limites.orcamento`). Essa restrição garante que o custo total de todos os computadores comprados, somando os três departamentos, não ultrapasse esse valor.

### Função objetivo
O objetivo do modelo é minimizar o custo total da compra. Ou seja, entre todas as combinações de computadores que satisfazem as restrições acima, o modelo busca a combinação de menor custo para a empresa.

### Verificação do status da solução
Antes de exibir os resultados, o código verifica se o solver realmente encontrou uma solução ótima (`status == pywraplp.Solver.OPTIMAL`). Isso é importante porque, se algum valor do JSON for alterado e o problema se tornar inviável (por exemplo, um orçamento baixo demais para atingir o desempenho mínimo exigido), o solver não terá uma resposta válida. Sem essa verificação, o código imprimiria valores sem sentido; com ela, o programa avisa que não foi possível encontrar uma solução ótima.

## Parte 2 do projeto: entradas do modelo em arquivo JSON

### Objetivo
Na segunda parte do projeto, todas as entradas do modelo foram retiradas do código e passaram a ficar em arquivos JSON. Assim é possível mudar a quantidade de computadores de cada departamento, o desempenho mínimo, as características dos modelos A, B e C e os limites de energia, manutenção e orçamento sem tocar na lógica do programa ([main_n2.py](main_n2.py)).

O motivo dessa mudança é permitir que **um analista altere apenas o arquivo JSON, e não o código do projeto**. Quem edita o código corre o risco de apagar um parêntese, trocar o nome de uma variável ou esquecer um valor em uma das restrições, e com isso gerar um erro de execução e ficar sem a solução procurada. No JSON o analista só mexe nos números. A estrutura do modelo (variáveis, restrições e função objetivo) continua a mesma e já foi testada.

### Cenário 1: `dados.json` (cenário original)
O arquivo [dados.json](dados.json) guarda os mesmos valores do enunciado da primeira parte do projeto:

| Departamento    | Quantidade | Desempenho mínimo | Máximo de A | Mínimo de C |
| --------------- | ---------: | ----------------: | ----------: | ----------: |
| Administrativo  |          8 |               420 |           3 |           2 |
| Financeiro      |          6 |               450 |           2 |           2 |
| Desenvolvimento |         12 |               720 |           3 |           6 |

| Computador | Custo    | Desempenho | Energia (kWh/mês) | Manutenção anual |
| ---------- | -------: | ---------: | ----------------: | ---------------: |
| A          | R$ 3.300 |         70 |                 5 |           R$ 400 |
| B          | R$ 5.000 |        110 |                 8 |           R$ 300 |
| C          | R$ 6.500 |        140 |                10 |           R$ 250 |

| Limite                   | Valor      |
| ------------------------ | ---------: |
| Energia (kWh/mês)        |        205 |
| Manutenção anual         |   R$ 8.500 |
| Orçamento de compra      | R$ 132.000 |

### Cenário 2: `dados_cenario2.json` (cenário pedido pelo professor)
O professor pediu para verificar como o modelo se comporta em um cenário diferente. Para isso foi criado o arquivo [dados_cenario2.json](dados_cenario2.json), com a mesma estrutura do `dados.json` e outros valores:

| Departamento    | Quantidade | Desempenho mínimo | Máximo de A | Mínimo de C |
| --------------- | ---------: | ----------------: | ----------: | ----------: |
| Administrativo  |          8 |               640 |           3 |           2 |
| Financeiro      |          6 |               400 |           3 |           1 |
| Desenvolvimento |         12 |              1700 |           0 |           8 |

| Computador | Custo    | Desempenho | Energia (kWh/mês) | Manutenção anual |
| ---------- | -------: | ---------: | ----------------: | ---------------: |
| A          | R$ 2.800 |         60 |                 4 |           R$ 450 |
| B          | R$ 4.900 |        120 |                 9 |           R$ 320 |
| C          | R$ 7.600 |        190 |                14 |           R$ 180 |

| Limite                   | Valor      |
| ------------------------ | ---------: |
| Energia (kWh/mês)        |        330 |
| Manutenção anual         |   R$ 9.000 |
| Orçamento de compra      | R$ 185.000 |

### O que mudou entre os dois cenários
- **Desempenho mínimo:** subiu no Administrativo (420 → 640) e principalmente no Desenvolvimento (720 → 1700). No Financeiro caiu (450 → 400).
- **Exigências específicas:** o Desenvolvimento não pode mais comprar nenhum computador A (máximo 3 → 0) e precisa de pelo menos 8 computadores C (antes eram 6). O Financeiro ficou mais flexível: até 3 computadores A (antes 2) e no mínimo 1 C (antes 2).
- **Computadores:** o modelo A ficou mais barato e mais fraco, o B ficou um pouco mais barato e mais forte, e o C ficou mais caro e mais potente, consumindo mais energia e gastando menos com manutenção.
- **Limites:** energia (205 → 330 kWh), manutenção (R$ 8.500 → R$ 9.000) e orçamento (R$ 132.000 → R$ 185.000) aumentaram.
- **Quantidade de máquinas:** continuou a mesma (8, 6 e 12, total de 26).

### Resultado dos dois cenários
Os dois cenários foram resolvidos pelo mesmo código, mudando apenas o arquivo de entrada. A comparação completa está em [COMPARACAO.md](COMPARACAO.md). Resumo:

| Departamento    | Cenário 1 (A / B / C) | Cenário 2 (A / B / C) |
| --------------- | :-------------------: | :-------------------: |
| Administrativo  |       3 / 3 / 2       |       3 / 3 / 2       |
| Financeiro      |       2 / 2 / 2       |       3 / 2 / 1       |
| Desenvolvimento |       3 / 3 / 6       |       0 / 4 / 8       |
| **Custo ótimo** |   **R$ 131.400,00**   |   **R$ 144.500,00**   |

O custo do cenário 2 ficou R$ 13.100 maior (cerca de 10%), principalmente porque o Desenvolvimento passou a ser obrigado a comprar 8 computadores C, que agora custam R$ 7.600 cada.

### Conclusão da Parte 2
Para testar o cenário pedido pelo professor, nenhuma restrição, variável ou a função objetivo precisou ser reescrita: bastou criar um novo arquivo JSON com os valores desejados. Para escolher qual cenário será executado, o analista só precisa trocar o nome do arquivo na variável `caminho_json` do [main_n2.py](main_n2.py):

```python
caminho_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados_cenario2.json")
```

Basta usar `"dados.json"` para rodar o cenário 1 ou `"dados_cenario2.json"` para rodar o cenário 2. Essa é a única alteração no programa, e o resto do código continua igual. Assim, um analista pode simular quantos cenários quiser criando novos arquivos JSON e trocando só esse nome, sem risco de introduzir um erro no código e ficar sem a solução do problema.
