from sty import bg, rs, Style, RgbBg

bg.orange = Style(RgbBg(255, 150, 50))
orange_center_sq = [1, 0, 0, 0, 0, 0]
green_center_sq = [0, 1, 0, 0, 0, 0]
red_center_sq = [0, 0, 1, 0, 0, 0]
blue_center_sq = [0, 0, 0, 1, 0, 0]
white_center_sq = [0, 0, 0, 0, 1, 0]
yellow_center_sq = [0, 0, 0, 0, 0, 1]

rubicks_example = [
    # prva strana, narandzasta u sredini
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    # druga strana, zelena u sredini
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    # treca strana, crvena u sredini
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    # cetvrta strana, plava u sredini
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    # peta strana, bela u sredini
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    # sesta strana, zuta u sredini
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1]
]


def print_square(square):
    if square[0] == 1:
        print(bg.orange + "   " + rs.bg, end=" ")
    elif square[1] == 1:
        print(bg.da_green + "   " + rs.bg, end=" ")
    elif square[2] == 1:
        print(bg.red + "   " + rs.bg, end=" ")
    elif square[3] == 1:
        print(bg.blue + "   " + rs.bg, end=" ")
    elif square[4] == 1:
        print(bg.white + "   " + rs.bg, end=" ")
    else:
        print(bg.yellow + "   " + rs.bg, end=" ")


def print_rubicks(rubicks_cube):
    # gornja, bela strana
    print(" "*11, end=" ")
    for i in range(32, 35):
        print_square(rubicks_cube[i])

    print("\n\n" + " "*11, end=" ")

    print_square(rubicks_cube[35])
    print_square(white_center_sq)
    print_square(rubicks_cube[36])

    print("\n\n" + " "*11, end=" ")

    for i in range(37, 40):
        print_square(rubicks_cube[i])

    print('\n')

    # prvi red kocke
    for i in range(0, 3):
        print_square(rubicks_cube[i])

    for i in range(8, 11):
        print_square(rubicks_cube[i])

    for i in range(16, 19):
        print_square(rubicks_cube[i])

    for i in range(24, 27):
        print_square(rubicks_cube[i])

    print('\n')

    # drugi red kocke
    print_square(rubicks_cube[3])
    print_square(orange_center_sq)
    print_square(rubicks_cube[4])

    print_square(rubicks_cube[11])
    print_square(green_center_sq)
    print_square(rubicks_cube[12])

    print_square(rubicks_cube[19])
    print_square(red_center_sq)
    print_square(rubicks_cube[20])

    print_square(rubicks_cube[27])
    print_square(blue_center_sq)
    print_square(rubicks_cube[28])

    print('\n')

    # treci red kocke
    for i in range(5, 8):
        print_square(rubicks_cube[i])

    for i in range(13, 16):
        print_square(rubicks_cube[i])

    for i in range(21, 24):
        print_square(rubicks_cube[i])

    for i in range(29, 32):
        print_square(rubicks_cube[i])

    print('\n')

    # donja, zuta strana
    print(" "*11, end=" ")
    for i in range(40, 43):
        print_square(rubicks_cube[i])

    print("\n\n" + " "*11, end=" ")

    print_square(rubicks_cube[43])
    print_square(yellow_center_sq)
    print_square(rubicks_cube[44])

    print("\n\n" + " "*11, end=" ")

    for i in range(45, 48):
        print_square(rubicks_cube[i])

    print('\n')


if __name__ == '__main__':
    print_rubicks(rubicks_example)
