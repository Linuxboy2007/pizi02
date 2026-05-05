#Репина задача 16 изменена
matrix = [[1,2,3],
         [4,5,6],
         [7,8,9]]
diagonal = [matrix[i][i] for i in range (len(matrix))]
trace = sum(diagonal)
value = trace / len(matrix)
for i in range(len(matrix)):
    if i % 2 == 0:
        matrix[i] = [x / value for x in matrix[i]]

print('Диагональные элементы:', diagonal)
print('Сумма диаг эл', trace)
print('Преобразованная матрица')
for row in matrix:
    print(row)
