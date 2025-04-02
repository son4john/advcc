length = 0
width = 0
height = 0

# test_input = '2x3x4'
# test_input2 =  '1x1x10'

with open('d2input.txt', 'r') as file:
    input_file = file.read()

counter = 0
total_ribbion = 0
split_line = input_file.split('\n')
# print(f"The last element is {split_line[-1]}")
split_line.pop()
for line in split_line:
    # if counter == 3:
    #     break
    # counter = counter + 1
    all_inputs = line.split('x')
    length = int(all_inputs[0])
    width = int(all_inputs[1])
    height = int(all_inputs[2])


    bow = length*width*height
    ribbion = 0
    if length < width:
        if width < height:
            ribbion = length + length + width + width
        else:
            ribbion = length + length + height + height
    else:
        if length < height:
            ribbion = width + width + length + length
        else:
            ribbion = width + width + height + height

    final_area = bow + ribbion
    total_ribbion = total_ribbion + final_area
    # print(final_area)

print(f"the elves will need {total_ribbion} of ribbion.")