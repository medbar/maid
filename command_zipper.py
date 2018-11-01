
# 0 - левая гусеница
# 1 - правая гусеница
# 2,3,4 - первый-третий[вверх-вниз, ближе-дальше, сжать-разжать] мотор манипулятора
# каждый бит состоит из:
# 0,1 - кодируют состояние мотора ( 00 - стоп
#                                   01 - влево
#                                   10 - вправо
#                                   11 - стоп )
# 2-7 биты - время работы в 10*милисекундах. ( от 0 милисекунд до 640 )

def zip_states(maid_states):
    data=[]
    for state in maid_states:
        time = abs(state)
        turn = 0
        if state < 0:
            turn = 2
        elif state > 0:
            turn = 1
        packed_state = (time << 2) | (turn & 0x03)
        data.append(packed_state)
    return bytes(data)


def unzip_states(zipped_states):
    states = []
    for packed_state in zipped_states:
        time = packed_state >> 2
        turn = packed_state & 0x03
        state = 0
        if turn == 2:
            state = -1
        elif turn == 1:
            state = 1
        states.append(state*time)
    return states