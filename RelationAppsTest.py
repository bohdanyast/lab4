import RelationsApp as ra
import numpy as np

matrix = [
	[0,1,1,1,1],
	[0,0,1,1,0],
	[0,1,1,1,1],
	[1,1,1,0,1],
	[1,1,1,1,1]
]
matrix1 = [
	[0,1,1,1,1],
	[0,0,1,1,0],
	[0,1,1,1,1],
	[1,1,1,0,1],
	[1,1,1,1,1]
]
matrix2 = [
	[0,1,1,1,1],
	[0,0,1,1,0],
	[0,1,1,1,1],
	[1,1,1,0,1],
	[1,1,1,1,1]
]
matrix3 = [
	[0,1,1,1,1],
	[0,0,1,1,0],
	[0,1,1,1,1],
	[1,1,1,0,1],
	[1,1,1,1,1]
]
matrix_2_pow = np.reshape(np.dot(np.array(matrix3), np.array(matrix3)), (len(matrix3), len(matrix3)))
matrix_3_pow = np.reshape(np.dot(matrix_2_pow, np.array(matrix3)), (len(matrix3), len(matrix3)))
matrix4 = np.array([
	[0, 1, 1, 1, 1],
	[0, 0, 1, 1, 0],
	[0, 1, 1, 1, 1],
	[1, 1, 1, 0, 1],
	[1, 1, 1, 1, 1]
])

print(f"Задане бінарне відношення:\n{np.reshape(np.array(matrix), (len(matrix), len(matrix)))}\n")
print(f"""Властивості заданого відношення: 
1. {ra.get_reflexivity(matrix)}
2. {ra.get_symmetry(matrix)}
3. {ra.get_transitivity(matrix)}
""")
print(f"""Чи є задане відношення: 
1. Відношенням еквівалентності: {'так' if ra.is_relation_of_equation(matrix) else 'ні'}
2. Відношенням строгого порядку: {'так' if ra.is_relation_of_strict_sequence(matrix) else 'ні'}
3. Відношенням часткового порядку: {'так' if ra.is_relation_of_partial_sequence(matrix) else 'ні'}
""")
print(f"""Замикання за властивостями, якими не володіє: 
1. Замикання за рефлексивністю:
{np.array(ra.get_reflexive_closure(matrix))}
2. Замикання за симетрією:
{np.array(ra.get_symmetrical_closure(matrix1))}
1. Замикання за транзитивністю:
{np.array(ra.get_transitive_closure(matrix2))}
""")
print(f"""2 і 3 степінь заданого відношення: 
1 степінь:
{np.reshape(np.array(matrix3), (len(matrix3), len(matrix3)))}
2 степінь:
{ra.composition(matrix4, matrix4)}
3 степінь:
{ra.composition(ra.composition(matrix4, matrix4), matrix4)}
""")
