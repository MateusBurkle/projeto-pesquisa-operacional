from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SAT")

# Adicionando as variaveis de desições
a_fin = solver.IntVar(0, 6, "a_fin")
b_fin = solver.IntVar(0, 6, "b_fin")
c_fin = solver.IntVar(0, 6, "c_fin")

a_des = solver.IntVar(0,10, 'a_des')
b_des = solver.IntVar(0,10, 'b_des')
c_des = solver.IntVar(0,10, 'c_des')

a_adm = solver.IntVar(0,8, 'a_adm')
b_adm = solver.IntVar(0,8, 'b_adm')
c_adm = solver.IntVar(0,8, 'c_adm')

# adicionando os computadores no geral
computador_a = a_adm + a_fin + a_des
computador_b = b_adm + b_fin + b_des
computador_c = c_adm + c_fin + c_des
# Adicionando as variaveis de score
administrativo_score = 420
financeiro_score = 450
desenvolvimento_score = 720

# Restricões de desempenho por Departamento
solver.Add(70 * a_adm + 110 * b_adm + 140 * c_adm >= administrativo_score)
solver.Add(70 * a_fin + 110 * b_fin + 140 * c_fin >= financeiro_score)
solver.Add(70 * a_des + 110 * b_des + 140 * c_des >= desenvolvimento_score)

# Restrição de quantidade máxima de máquinas por departamento 
solver.Add(a_adm + b_adm + c_adm == 8)
solver.Add(a_fin + b_fin + c_fin == 6)
solver.Add(a_des + b_des + c_des == 12)

# Restrição de Consumo por energia
solver.Add(5 * computador_a + 8 * computador_b + 10 * computador_c <= 205)

# Restrição de manutenção dos computadores
solver.Add(400 * computador_a + 300 * computador_b + 250 * computador_c <= 8500)


# Restrição do Administrativo 
solver.Add(a_adm <= 3)
solver.Add(c_adm >= 2)

# Restrição do Financeiro
solver.Add(a_fin <= 2)
solver.Add(c_fin >= 2)

# Restrição Desenvolvimento
solver.Add(a_des <= 3)
solver.Add(c_des >= 6)


# Orçamento máximo de compra 
custo = 3300 * computador_a + 5000 * computador_b + 6500 * computador_c

# Limitando o orcamento maximo de compra
solver.Add(custo <= 200000) 


# Função Obejtivo minimizando o custo da compra
solver.Minimize(custo)

# Para resolver nossas restrições
solver.Solve()

print("\n")
print(f"O custo ótimo = R$ {solver.Objective().Value():.2f}")

print('\nPara o Departamento Financeiro:')
print(f"A quantidade de computadores A no departamento de Financeiro: {int(a_fin.solution_value())}")
print(f"A quantidade de computadores B no departamento de Financeiro: {int(b_fin.solution_value())}")
print(f"A quantidade de computadores C no departamento de Financeiro: {int(c_fin.solution_value())}")

print('\nPara o Departamento Administrativo:')
print(f"a quantidade de computadores A no departamento Administrativo: {int(a_adm.solution_value())} ")
print(f"a quantidade de computadores B no departamento Administrativo: {int(b_adm.solution_value())} ")
print(f"a quantidade de computadores C no departamento Administrativo: {int(c_adm.solution_value())} ")

print('\nPara o Departamento Desenvolvimento:')
print(f"a quantidade de computadores A no departamento Desenvolvimento: {int(a_des.solution_value())} ")
print(f"a quantidade de computadores B no departamento Desenvolvimento: {int(b_des.solution_value())} ")
print(f"a quantidade de computadores C no departamento Desenvolvimento: {int(c_des.solution_value())} ")

print(f"Total dos computadores a = {int(computador_a.solution_value())}")
print(f"Total dos computadores b = {int(computador_b.solution_value())}")
print(f"Total dos computadores c = {int(computador_c.solution_value())}")