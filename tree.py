# draws a tree and says Merry Christmas
i = 4
while i >= -1:
    if i > -1:
        print(" " * i + "*" * (-2 * (i - 4) + 1))
    else:
        print(" " * 4 + "*" * 2)
    i -= 1

print("Merry Christmas!")
