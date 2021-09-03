def Season1():
    return "Spring"
def Season2():
    return "Summer"
def Season3():
    return "Fall"
def Season4():
    return "Winter"
def Default():
    return "Invalid Season"
seasondict = {
    1: Season1,
    2: Season2,
    3: Season3,
    4: Season4
}

def getSeason(season):
    """
    将season映射为字符串
    :param season:
    :return:
    """
    fun = seasondict.get(season, Default)
    return fun()

print(getSeason(2))
