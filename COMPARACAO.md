# Para o Cenário 1 (usando os dados.json):

O custo ótimo = R$ 131400.00

Para o Departamento Financeiro:
A quantidade de computadores A no departamento de Financeiro: 2.0
A quantidade de computadores B no departamento de Financeiro: 2.0
A quantidade de computadores C no departamento de Financeiro: 2.0

Para o Departamento Administrativo:
a quantidade de computadores A no departamento Administrativo: 3.0 
a quantidade de computadores B no departamento Administrativo: 3.0 
a quantidade de computadores C no departamento Administrativo: 2.0 

Para o Departamento Desenvolvimento:
a quantidade de computadores A no departamento Desenvolvimento: 3.0 
a quantidade de computadores B no departamento Desenvolvimento: 3.0 
a quantidade de computadores C no departamento Desenvolvimento: 6.0 
Total dos computadores A = 8.0
Total dos computadores B = 8.0
Total dos computadores C = 10.0


# Para o Cenário 2 (usando os dados_cenario2.json):
O custo ótimo = R$ 144500.00

Para o Departamento Financeiro:
A quantidade de computadores A no departamento de Financeiro: 3.0
A quantidade de computadores B no departamento de Financeiro: 2.0
A quantidade de computadores C no departamento de Financeiro: 1.0

Para o Departamento Administrativo:
a quantidade de computadores A no departamento Administrativo: 3.0 
a quantidade de computadores B no departamento Administrativo: 3.0 
a quantidade de computadores C no departamento Administrativo: 2.0 

Para o Departamento Desenvolvimento:
a quantidade de computadores A no departamento Desenvolvimento: 0.0 
a quantidade de computadores B no departamento Desenvolvimento: 4.0 
a quantidade de computadores C no departamento Desenvolvimento: 8.0 
Total dos computadores A = 6.0
Total dos computadores B = 9.0
Total dos computadores C = 11.0

---

# Tabela comparativa dos resultados

## Compras por departamento (quantidade de A / B / C)

| Departamento    | Cenário 1 (A / B / C) | Cenário 2 (A / B / C) |
| --------------- | :-------------------: | :-------------------: |
| Administrativo  |      3 / 3 / 2        |      3 / 3 / 2        |
| Financeiro      |      2 / 2 / 2        |      3 / 2 / 1        |
| Desenvolvimento |      3 / 3 / 6        |      0 / 4 / 8        |

## Totais

| Indicador                     | Cenário 1     | Cenário 2     | Diferença (2 − 1) |
| ----------------------------- | ------------: | ------------: | ----------------: |
| Total de computadores A       |             8 |             6 |                −2 |
| Total de computadores B       |             8 |             9 |                +1 |
| Total de computadores C       |            10 |            11 |                +1 |
| Total de máquinas             |            26 |            26 |                 0 |
| **Custo ótimo (R$)**          | **131.400,00** | **144.500,00** |       **+13.100,00** |
| Consumo de energia (kWh/mês)* |           204 |           259 |               +55 |
| Manutenção anual (R$)*        |         8.100 |         7.560 |              −540 |

\* Calculados a partir das quantidades totais e dos valores de cada `dados*.json`.

## Observações

- O **Administrativo** comprou exatamente o mesmo conjunto nos dois cenários (3 A, 3 B, 2 C), mesmo com o desempenho mínimo subindo de 420 para 640.
- O **Financeiro** trocou 1 computador C por 1 A (mínimo de C caiu de 2 para 1 e o máximo de A subiu de 2 para 3).
- O **Desenvolvimento** mudou mais: sem nenhum A (`max_a = 0`) e com mínimo de 8 C, passou a comprar 4 B e 8 C.
- O custo subiu cerca de **10%** (R$ 13.100), principalmente por causa dos 8 computadores C obrigatórios no Desenvolvimento, que agora custam R$ 7.600 cada.
