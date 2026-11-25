import json
import os

from ortools.linear_solver import pywraplp

# Lendo os dados do arquivo JSON (que fica na mesma pasta deste arquivo)
caminho_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados_cenario2.json")
with open(caminho_json, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

adm = dados["departamentos"]["administrativo"]
fin = dados["departamentos"]["financeiro"]
des = dados["departamentos"]["desenvolvimento"]

pc_a = dados["computadores"]["A"]
pc_b = dados["computadores"]["B"]
pc_c = dados["computadores"]["C"]

limites = dados["limites"]

solver = pywraplp.Solver.CreateSolver("SAT")

# Adicionando as variaveis de desições
a_fin = solver.IntVar(0, fin["quantidade"], "a_fin")
b_fin = solver.IntVar(0, fin["quantidade"], "b_fin")
c_fin = solver.IntVar(0, fin["quantidade"], "c_fin")

a_des = solver.IntVar(0, des["quantidade"], 'a_des')
b_des = solver.IntVar(0, des["quantidade"], 'b_des')
c_des = solver.IntVar(0, des["quantidade"], 'c_des')

a_adm = solver.IntVar(0, adm["quantidade"], 'a_adm')
b_adm = solver.IntVar(0, adm["quantidade"], 'b_adm')
c_adm = solver.IntVar(0, adm["quantidade"], 'c_adm')

# adicionando os computadores no geral
computador_a = a_adm + a_fin + a_des
computador_b = b_adm + b_fin + b_des
computador_c = c_adm + c_fin + c_des

# Restricões de desempenho por Departamento
solver.Add(pc_a["desempenho"] * a_adm + pc_b["desempenho"] * b_adm + pc_c["desempenho"] * c_adm >= adm["score"])
solver.Add(pc_a["desempenho"] * a_fin + pc_b["desempenho"] * b_fin + pc_c["desempenho"] * c_fin >= fin["score"])
solver.Add(pc_a["desempenho"] * a_des + pc_b["desempenho"] * b_des + pc_c["desempenho"] * c_des >= des["score"])

# Restrição de quantidade máxima de máquinas por departamento
solver.Add(a_adm + b_adm + c_adm == adm["quantidade"])
solver.Add(a_fin + b_fin + c_fin == fin["quantidade"])
solver.Add(a_des + b_des + c_des == des["quantidade"])

# Restrição de Consumo por energia
solver.Add(pc_a["energia"] * computador_a + pc_b["energia"] * computador_b + pc_c["energia"] * computador_c <= limites["energia"])

# Restrição de manutenção dos computadores
solver.Add(pc_a["manutencao"] * computador_a + pc_b["manutencao"] * computador_b + pc_c["manutencao"] * computador_c <= limites["manutencao"])


# Restrição do Administrativo
solver.Add(a_adm <= adm["max_a"])
solver.Add(c_adm >= adm["min_c"])

# Restrição do Financeiro
solver.Add(a_fin <= fin["max_a"])
solver.Add(c_fin >= fin["min_c"])

# Restrição Desenvolvimento
solver.Add(a_des <= des["max_a"])
solver.Add(c_des >= des["min_c"])


# Orçamento máximo de compra
custo = pc_a["custo"] * computador_a + pc_b["custo"] * computador_b + pc_c["custo"] * computador_c

# Limitando o orcamento maximo de compra
solver.Add(custo <= limites["orcamento"])


# Função Objetivo minimizando o custo da compra
solver.Minimize(custo)

# Para resolver nossas restrições
status = solver.Solve()

# Só imprime os resultados se o solver encontrou a solução ótima
if status == pywraplp.Solver.OPTIMAL:
    print("\n")
    print(f"O custo ótimo = R$ {solver.Objective().Value():.2f}")

    print('\nPara o Departamento Financeiro:')
    print(f"A quantidade de computadores A no departamento de Financeiro: {(a_fin.solution_value())}")
    print(f"A quantidade de computadores B no departamento de Financeiro: {(b_fin.solution_value())}")
    print(f"A quantidade de computadores C no departamento de Financeiro: {(c_fin.solution_value())}")

    print('\nPara o Departamento Administrativo:')
    print(f"a quantidade de computadores A no departamento Administrativo: {(a_adm.solution_value())} ")
    print(f"a quantidade de computadores B no departamento Administrativo: {(b_adm.solution_value())} ")
    print(f"a quantidade de computadores C no departamento Administrativo: {(c_adm.solution_value())} ")

    print('\nPara o Departamento Desenvolvimento:')
    print(f"a quantidade de computadores A no departamento Desenvolvimento: {(a_des.solution_value())} ")
    print(f"a quantidade de computadores B no departamento Desenvolvimento: {(b_des.solution_value())} ")
    print(f"a quantidade de computadores C no departamento Desenvolvimento: {(c_des.solution_value())} ")

    print(f"Total dos computadores A = {(computador_a.solution_value())}")
    print(f"Total dos computadores B = {(computador_b.solution_value())}")
    print(f"Total dos computadores C = {(computador_c.solution_value())}")
else:
    print("Não foi encontrada uma solução ótima para o problema (verifique as restrições).")
