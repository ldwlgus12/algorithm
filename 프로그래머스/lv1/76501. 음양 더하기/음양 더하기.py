def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == True:
            pass
        else:
            absolutes[i] = -1 * absolutes[i]

    return sum(absolutes)