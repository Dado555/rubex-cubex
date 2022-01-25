orange_center_sq = [1, 0, 0, 0, 0, 0]
green_center_sq = [0, 1, 0, 0, 0, 0]
red_center_sq = [0, 0, 1, 0, 0, 0]
blue_center_sq = [0, 0, 0, 1, 0, 0]
white_center_sq = [0, 0, 0, 0, 1, 0]
yellow_center_sq = [0, 0, 0, 0, 0, 1]

colours_dict = {
        'w': white_center_sq,
        'o': orange_center_sq,
        'r': red_center_sq,
        'g': green_center_sq,
        'b': blue_center_sq,
        'y': yellow_center_sq
    }

def conv(array):
    if array[0] == 1:
        return 'o'
    elif array[1] == 1:
        return 'g'
    elif array[2] == 1:
        return 'r'
    elif array[3] == 1:
        return 'b'
    elif array[4] == 1:
        return 'w'
    else:
        return 'y'

def print_cube(state):
    print(
        "    " + conv(state[0:6]) + conv(state[6:12]) + conv(state[12:18]) + "\n" +
        "    " + conv(state[18:24]) + "w" + conv(state[24:30]) + "\n" +
        "    " + conv(state[30:36]) + conv(state[36:42]) + conv(state[42:48]) + "\n\n" +

        conv(state[48:54]) + conv(state[54:60]) + conv(state[60:66]
                                                       ) + " " + conv(state[96:102]) + conv(state[102:108])
        + conv(state[108:114]) + " " + conv(state[144:150]) + conv(state[150:156]) + conv(state[156:162]) + " " + conv(state[192:198]) +
        conv(state[198:204]) + conv(state[204:210]) + "\n" +

        conv(state[66:72]) + "o" + conv(state[72:78]) + " " + conv(state[114:120]) + "g" + conv(state[120:126]) + " " +
        conv(state[162:168]) + "r" + conv(state[168:174]) + " " + conv(state[210:216]) + "b" + conv(state[216:222]) + "\n" +

        conv(state[78:84]) + conv(state[84:90]) + conv(state[90:96]) + " " + conv(state[126:132]) + conv(state[132:138]) +
        conv(state[138:144]) + " " + conv(state[174:180]) + conv(state[180:186]) + conv(state[186:192]) + " " + conv(state[222:228]) +
        conv(state[228:234]) + conv(state[234:240]) + "\n\n" +

        "    " + conv(state[240:246]) + conv(state[246:252]) + conv(state[252:258]) + "\n" +
        "    " + conv(state[258:264]) + "y" + conv(state[264:270]) + "\n" +
        "    " + conv(state[270:276]) +
        conv(state[276:282]) + conv(state[282:288]) + "\n"
    )
