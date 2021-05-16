# Un 20 % para compra de alimentos, 15% para compra de pasajes, 10% para compra de boletos de cine, 
# 15% para compra de libros y el dinero restante debe ser destinado para el pago del alquiler del lugar donde estás viviendo.

salary = float(input())
expenses = [0.2, 0.15, 0.1, 0.15]

foods = expenses[0]*salary
tickets = expenses[1]*salary
cinema = expenses[2]*salary
books = expenses[3]*salary

cost_expenses = foods+tickets+cinema+books
money_rent = salary-cost_expenses
print(money_rent)