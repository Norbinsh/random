""" Given a square matrix of size N X N, calculate the absolute difference between the sums of its diagonals. """



a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

main_diagonal = 0
sec_diagonal = 0
i = 0
f = -1
for line_list in a:
    main_diagonal += line_list[i]
    i += 1
    sec_diagonal += line_list[f]
    f -= 1
print(main_diagonal)
print(sec_diagonal)
print(abs(main_diagonal - sec_diagonal))


