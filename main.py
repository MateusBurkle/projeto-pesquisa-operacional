from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SAT")

# Adicionando as variaveis de restricao
computador_a = solver.IntVar(0, solver.infinity(), "computador_a")
computador_b = solver.IntVar(0, solver.infinity(), "computador_b")
computador_c = solver.IntVar(0, solver.infinity(), "computador_c")

# Adicionando as restricoes

# Restricao do Score de desempenho
solver.Add(60 * computador_a + 90 * computador_b + 120 * computador_c <= 100000)
# Restricao de Consumo

solver.Add()

solver.Minimize(3000 * computador_a + 5000 * computador_b + 7000 * computador_c)

solver.Solve()

print(f"O valor otimo:{solver.Objective().Value()}")
print(f"computador_a = {computador_a.solution_value()}")
print(f"computador_b = {computador_b.solution_value()}")
print(f"computador_c = {computador_c.solution_value()}")
