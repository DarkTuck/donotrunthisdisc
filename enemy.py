from random import choice
def bandyta():
    atack={
        "dźgnięcie": choice(range(1,3)),
        "uderzenie": choice(range(3,5)),
        "płapka": 5,
        "drapanie po głowie":0,
    }
    a=choice(list(atack))
    return a, atack[a]