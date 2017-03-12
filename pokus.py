def hi():
	print('Ahoj!')
	print('Ako sa mas?')

hi()

def hi(meno):
	if meno == 'Janka':
		print('Ciao Janka!')
	elif meno == 'Janko':
		print('Ciao Janko!')
	else:
		print ('Ahoj neznama!')


hi('Eva')

def hi(meno):
    print('Ahoj' + meno + '!')

dievcata = ['Katka', 'Lenka', 'Julia', 'Ty']
for meno in dievcata:
	hi (meno)
	print ('Dalsie dievca')