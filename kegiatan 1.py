# fungsi penjumlahan
def add (x, y):
    return x + y

# fungsi pengurangan
def minus (x, y):
    return x - y

# fungsi perkalian
def mult (x, y):
    return x * y

# fungsi pembagian
def div (x, y):
    return x / y

def tree(node):
    if isinstance(node, (int, float)):
        return node
    elif isinstance(node, tuple) and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return add(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))
        
expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi :", result)