def goudian(xiaofei):
    ele = 0
    if xiaofei <= 240 * 0.4883:
        ele = xiaofei / 0.4883
    elif (xiaofei - 240 * 0.4883) <= 160 * 0.5383:
        ele += 240
        ele += (xiaofei - 240 * 0.4883) / 0.5383
    else:
        ele += 400
        ele += (xiaofei - 240 * 0.4883 - 160 * 0.5383) / 0.7883
    return ele

x = int(input())
print('%.2f' % goudian(x))