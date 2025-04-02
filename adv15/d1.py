
counter = 0
enter_basement = -1
input_file = ""

with open('d1input.txt', 'r') as file:
    input_file = file.read()

up = '('
down = ')'

test_input ="(()))("

print(test_input)

floor = 0
basement = False
for t in input_file:
    if t == '(':
        floor = floor + 1
    elif t == ')':
        floor = floor - 1
    else:
        print(f"unrecognized symbol{t}")
        break
    counter = counter + 1
    if basement == False:
        if floor < 0:
            basement = True
            enter_basement = counter

print(f"You are on Floor: {floor}")
print(f"Entered the basement on step {enter_basement}")


