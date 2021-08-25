import os
import random

def display_row(r1, r2, r3):
	os.system('clear')
	print('*'*80)
	print('\t\t\tWELCOME TO TICK TAC TOE GAME')
	print('*'*80)
	r1 = '	'.join(r1)
	print(f'\n\t\t\t{r1}\n')
	r2 = '	'.join(r2)
	print(f'\t\t\t{r2}\n')
	r3 = '	'.join(r3)
	print(f'\t\t\t{r3}\n')
	print('*'*80)
	player_to_go_first()
				
def update_index1(z):
	if (z in range(1,4)):
		i = z-1
		row1[i] = 'X'
		display_row(row1, row2, row3)
	if (z in range(4,7)):
		i = z-3-1
		row2[i] = 'X'
		display_row(row1, row2, row3)
	if (z in range(7,10)):
		i = z-6-1
		row3[i] = 'X'
		display_row(row1, row2, row3)
def update_index2(z):
	if (z in range(1,4)):
		i = z-1
		row1[i] = 'O'
		display_row(row1, row2, row3)
	if (z in range(4,7)):
		i = z-3-1
		row2[i] = 'O'
		display_row(row1, row2, row3)
	if (z in range(7,10)):
		i = z-6-1
		row3[i] = 'O'
		display_row(row1, row2, row3)

def take_user_input(flag_passed, index_selected):
	while(True):		
		try:
			if(flag_passed == 'A'):
				index = int(input(f"Enter a Position to fill - Player A({player1_marker}) : 	"))
				if (index in range(1, 10) and index not in index_selected):
					return index
				else:
					print("Invalid Position given. Please select correct Values between 1 to 9")				
					continue
			else:
				index = int(input(f"Enter a Position to fill - Player B({player2_marker}) : 	"))
				if (index in range(1, 10) and index not in index_selected):
					return index					
				else:
					print("Invalid Position given. Please select correct Values between 1 to 9")				
					continue
		except ValueError:
			continue

def pass_index_to_matrix(index, m1, m2 ):
	global flag
	global index_selected
	if (flag == 'A' and m1 == 'X'):
		update_index1(index)
		index_selected.append(index)
		flag = 'B'
	elif (flag == 'A' and m1 == 'O'):
		update_index2(index)
		index_selected.append(index)
		flag = 'B'
	elif (flag == 'B' and m2 == 'X'):
		update_index1(index)
		index_selected.append(index)
		flag = 'A'
	elif (flag == 'B' and m2 == 'O'):
		update_index2(index)
		index_selected.append(index)
		flag = 'A'
	
def check_result():
	for i in range(0,3):
			for j in range(0,3):
				for k in range(0,3):
					if (row1[0] == row2[0] == row3[0] == 'X'):
						counter1 = 3
					elif (row1[1] == row2[1] == row3[1] == 'X'):
						counter1 = 3
					elif (row1[2] == row2[2] == row3[2] == 'X'):
						counter1 = 3
					elif (row1[0] == row1[1] == row1[2] == 'X'):
						counter1 = 3
					elif (row2[0] == row2[1] == row2[2] == 'X'):
						counter1 = 3
					elif (row3[0] == row3[1] == row3[2] == 'X'):
						counter1 = 3
					elif (row1[0] == row2[1] == row3[2] == 'X'):
						counter1 = 3
					elif (row1[2] == row2[1] == row3[0] == 'X'):
						counter1 = 3
					else:
						counter1 = 0
					if (counter1 == 3):
						return counter1
	for i in range(0,3):
			for j in range(0,3):
				for k in range(0,3):
					if (row1[0] == row2[0] == row3[0] == 'O'):
						counter2 = 3
					elif (row1[1] == row2[1] == row3[1] == 'O'):
						counter2 = 3
					elif (row1[2] == row2[2] == row3[2] == 'O'):
						counter2 = 3
					elif (row1[0] == row1[1] == row1[2] == 'O'):
						counter2 = 3
					elif (row2[0] == row2[1] == row2[2] == 'O'):
						counter2 = 3
					elif (row3[0] == row3[1] == row3[2] == 'O'):
						counter2 = 3
					elif (row1[0] == row2[1] == row3[2] == 'O'):
						counter2 = 3
					elif (row1[2] == row2[1] == row3[0] == 'O'):
						counter2 = 3
					else:
						counter2 = 0
					if (counter2 == 3):
						return counter2

def check_player():
	temp = ['A' , 'B']
	random.shuffle(temp)
	z = temp[0]
	return z

def player_marker():
	while(True):
		symbol = input('Player A: Please select a symbol (X or O)\n').upper()
		if (symbol == 'X' or symbol == 'O'):
			break
		else:
			print("Incorrect Symbol selected")
			continue
	if(symbol == 'X'):
		sel = ('X', 'O')
	else:
		sel = ('O' , 'X')	
	return sel

def player_to_go_first():
	global temp_flg
	#m = player_marker()
	if (temp_flg == 'A'):
		print('Player A to go first')
	elif (temp_flg == 'B'):
		print('Player B to go first')
	temp_flg = ''	

count = 0
index_selected = []



row1 = [ '*', '*', '*' ]
row2 = [ '*', '*', '*' ]
row3 = [ '*', '*', '*' ]

flag = check_player()
player1_marker, player2_marker = player_marker()
temp_flg = flag
display_row(row1, row2, row3)



while(count < 9):
	input_selected = take_user_input( flag, index_selected )
	pass_index_to_matrix( input_selected , player1_marker, player2_marker )
	matched = check_result()
	if (matched == 3 and flag == 'B'):
		print(f"\t\tThe Winner is : Player A({player1_marker}) ")
		print('*'*80)
		break
	if (matched == 3 and flag == 'A'):
		print(f"\t\tThe Winner is : Player B ({player2_marker}) ")
		print('*'*80)		
		break
	else:
		if (count == 8 and matched != 3):
			print(f"\t\tMatch tied between A ({player1_marker}) and B ({player2_marker})")
			print('*'*80)
			break
	count+=1
	
























