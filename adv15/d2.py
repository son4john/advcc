length = 0
width = 0
height = 0

# test_input = '2x3x4'
# test_input2 =  '1x1x10'

with open('d2input.txt', 'r') as file:
    input_file = file.read()

counter = 0
total_paper = 0
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

    lw_area = length*width
    lh_area = length*height
    wh_area = width*height


    total_area = (2*lw_area) + (2*lh_area) + (2*wh_area)
    # print(total_area)

    if lw_area < lh_area:
        if lw_area < wh_area:
            extra = lw_area
        else:
            extra = wh_area
    else:
        if lh_area < wh_area:
            extra = lh_area
        else:
            extra = wh_area

    final_area = total_area + extra
    total_paper = total_paper + final_area
    # print(final_area)

print(f"the elves will need {total_paper} of wrapping paper.")