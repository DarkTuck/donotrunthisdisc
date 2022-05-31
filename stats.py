from random import  randint
z = randint(1, 10)
x = randint(1, 10)
y = randint(1, 10)
l = 3
def stats():
	global stats_list
	stats_list = [z, x, y, l]

stats()