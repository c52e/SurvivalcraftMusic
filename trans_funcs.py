def transCore(source, shift):
    def tuneToDigit(tune):
        return {'1':0, 'a':1, '2':2, 'b':3, '3':4, '4':5, 'd':6, '5':7, 'e':8, '6':9, 'f':10, '7':11}[tune]
    pitch = []
    octave = []
    oct = 12
    for tune in source:
        if tune in ' \t\r\n':
            continue
        elif tune == '^':
            oct = 48
        elif tune == '*':
            oct = 36
        elif tune == '+':
            oct = 24
        elif tune == '-':
            oct = 0
        elif tune == '_':
            oct = -12
        elif tune == '.':
            oct = -24
        else:
            if tune == '0':
                pitch.append('F')
                octave.append('F')
            else:
                p = oct + tuneToDigit(tune) + shift
                if p < 0:
                    raise Exception('Lower Bound Exceeded')
                elif p > 48: #一共4个八度加上一个do（49种频率）
                    raise Exception('Upper Bound Exceeded')
                # octave=3 pitch=c 为最后一个do
                pitch.append('0123456789ABCDE'[p%12 if p<36 else p-36])
                octave.append(str(p//12 if p<36 else 3))
            oct = 12
    pitch = ''.join(pitch)
    octave = ''.join(octave)
    return pitch, octave

# split('0123456798', 1, 3) -> ['012', '345', '678', '9']
# split('0123456798', 2, 3) -> ['024', '135', '68', '79']
def split(string, turn_num=1, single_length=256):
    length = len(string)
    group_total_length = turn_num * single_length
    group_num = (length + group_total_length - 1) // group_total_length
    res = ['' for i in range(group_num * turn_num)]
    for i, c in enumerate(string):
        group_index = i // group_total_length
        group_inner_index = i % turn_num
        res[group_index * turn_num + group_inner_index] += c
    return res

def transToSurvivalCraft(source, shift=0, turn_num=1):
    pitch, octave = transCore(source, shift)
    pitch = split(pitch, turn_num)
    octave = split(octave, turn_num)
    for i in range(len(pitch)):
        print((pitch[i], octave[i], len(pitch[i])))

if __name__ == "__main__":
    print(split('0123456789', 2, 3))