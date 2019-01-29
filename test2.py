def line_of_3():
	print((('+ '+ '- ') + ('- ' *3))*2 + '+')

def line_vert():
	print(('|' + (' '*9))*2 + '|')

def do_four(f):
	f()
	f()
	f()
	f()


def grid():
	line_of_3()
	do_four(line_vert)
	line_of_3()
	do_four(line_vert)
	line_of_3()

grid()