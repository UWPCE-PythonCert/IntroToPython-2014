def front3(str):
    if len(str) >= 3:
        return str[:3] + str[:3] + str[:3]
    else:
        return str + str + str

