from random import choice
def bandyta():
    global ez
    ez = 20
    atack = {
        "dźgnięcie": choice(range(1,3)),
        "uderzenie": choice(range(3,5)),
        "płapka": 5,
        "drapanie po głowie":0,
    }
    a = choice(list(atack))
    return a, atack[a]
