#1. Create all the variables

import random
import os

NUM_ROWS=6
NUM_COLS=7

board=[]

PLAYER_NAMES=["X","O","V","H","M"]

def clear():
	os.system("clear")

#2. Number of Players
while True:
	P=input("How many players (2-5)? ").strip()
	if P.isdigit():
		n=int(P)
		if 2<=n<=5:
			break
	print("Enter a number between 2 and 5: ")
PLAYERS=n
CHECKERS=PLAYER_NAMES[:PLAYERS]

turn=random.randint(0,PLAYERS-1)

#3. Create board with labelled columns

board=[]

for row in range(NUM_ROWS):
	row_list = []
	for col in range(NUM_COLS):
		row_list.append(" ")
	board.append(row_list)


print("  ", end="")
for col in range(NUM_COLS):
	print(' ' + chr(col+65)+ "  ", end="")
print("\n +" + "---+" * NUM_COLS)


for row in range(NUM_ROWS):
	print(" |", end=" ")
	for col in range(NUM_COLS):
		print(board[row][col]+ " | ", end="")
	print("\n +"+"---+"*NUM_COLS)


turn=random.randrange(PLAYERS)
game_over=False

#4. Main game loop

while not game_over:
	clear()

	print("  ", end="")
	for col in range(NUM_COLS):
		print(' ' + chr(col+65)+ "  ", end="")
	print("\n +" + "---+" * NUM_COLS)


	for row in range(NUM_ROWS):
		print(" |", end=" ")
		for col in range(NUM_COLS):
			print(board[row][col]+ " | ", end="")
		print("\n +"+"---+"*NUM_COLS)

	print(f"Player {CHECKERS[turn]}'s turn")

	#5. Conditions for column input
	while True:
		ans = input("Choose a column letter: ").strip()
		if len(ans)!=1:
			print("Invalid. Enter exactly 1 letter.")
			continue
		char=ans.upper()
		valid=chr(ord("A")+NUM_COLS-1)
		if not ("A"<= char <= valid):
			print("Invalid. Letter must be between A and G.")
			continue
		break

	index=ord(char)-ord("A")

	placed=False
	last_r=None

	r=NUM_ROWS-1
	while r>=0:
		if board[r][index]==" ":
			board[r][index]= CHECKERS[turn]
			placed=True
			last_r=r
			break
		r-=1

	if not placed:
		print("Coloumn is taken.")

		turn=(turn+1)%PLAYERS
		input("Press enter bar to continue.")
		continue

	last_c=index
	me=CHECKERS[turn]

	#6. Check for a win
	#6.1 Horizontal

	count=1

	#6.1.1 left
	rr=last_r
	cc=last_c-1
	while cc>=0 and board[rr][cc]==me:
		count+=1
		cc-=1

	#6.1.2 right
	rr=last_r
	cc=last_c+1
	while cc<NUM_COLS and board[rr][cc]==me:
		count+=1
		cc+=1
	if count>=4:
		clear()

		#reprint board
		print("  ", end="")
		for col in range(NUM_COLS):
			print(' ' + chr(col+65)+ "  ", end="")
		print("\n +" + "---+" * NUM_COLS)


		for row in range(NUM_ROWS):
			print(" |", end=" ")
			for col in range(NUM_COLS):
				print(board[row][col]+ " | ", end="")
			print("\n +"+"---+"*NUM_COLS)

		print(f"Player {me} wins!")
		break

	#6.2 Vertical
	count=1

	#6.2.1 down
	rr=last_r+1
	cc=last_c
	while rr<NUM_ROWS and board[rr][cc]==me:
		count+=1
		rr+=1

	#6.2.2 up
	rr=last_r-1
	cc=last_c
	while rr>=0 and board[rr][cc]==me:
		count+=1
		rr-=1
	if count>=4:
		clear()

		print("  ", end="")
		for col in range(NUM_COLS):
			print(' ' + chr(col+65)+ "  ", end="")
		print("\n +" + "---+" * NUM_COLS)


		for row in range(NUM_ROWS):
			print(" |", end=" ")
			for col in range(NUM_COLS):
				print(board[row][col]+ " | ", end="")
			print("\n +"+"---+"*NUM_COLS)

		print(f"Player {me} wins!")
		break

	#6.3 Diagonal \ (down-right+up-left)
	count=1

	#6.3.1 down-right
	rr=last_r+1
	cc=last_c+1
	while rr< NUM_ROWS and cc < NUM_COLS and board[rr][cc]==me:
		count+=1
		rr+=1
		cc+=1

	#6.3.2 up-left
	rr=last_r-1
	cc=last_c-1
	while rr>=0 and cc>=0 and board[rr][cc]==me:
		count+=1
		rr-=1
		cc-=1
	if count>=4:
		clear()
		print("  ", end="")
		for col in range(NUM_COLS):
			print(' ' + chr(col+65)+ "  ", end="")
		print("\n +" + "---+" * NUM_COLS)


		for row in range(NUM_ROWS):
			print(" |", end=" ")
			for col in range(NUM_COLS):
				print(board[row][col]+ " | ", end="")
			print("\n +"+"---+"*NUM_COLS)

		print(f"Player {me} wins!")
		break

	#6.4 Diagonal / (up-right + down-left)
	count=1

	#6.4.1 up-right
	rr=last_r-1
	cc=last_c+1
	while rr>=0 and cc<NUM_COLS and board[rr][cc]==me:
		count+=1
		rr-=1
		cc+=1

	#6.4.2 down-left
	rr=last_r+1
	cc=last_c-1
	while rr<NUM_ROWS and cc>=0 and board[rr][cc]==me:
		count+=1
		rr+=1
		cc-=1
	if count>=4:
		clear()
		print("  ", end="")
		for col in range(NUM_COLS):
			print(' ' + chr(col+65)+ "  ", end="")
		print("\n +" + "---+" * NUM_COLS)


		for row in range(NUM_ROWS):
			print(" |", end=" ")
			for col in range(NUM_COLS):
				print(board[row][col]+ " | ", end="")
			print("\n +"+"---+"*NUM_COLS)

		print(f"Player {me} wins!")
		break

	#7. Check for draws
	space=False
	r=0
	while r<NUM_ROWS:
		c=0
		while c< NUM_COLS:
			if board[r][c]==" ":
				space=True
				break
			c+=1
		if space:
			break
		r+=1

	if not space:
		clear()
		print("  ", end="")
		for col in range(NUM_COLS):
			print(' ' + chr(col+65)+ "  ", end="")
		print("\n +" + "---+" * NUM_COLS)


		for row in range(NUM_ROWS):
			print(" |", end=" ")
			for col in range(NUM_COLS):
				print(board[row][col]+ " | ", end="")
			print("\n +"+"---+"*NUM_COLS)

		print("Draw!")
		break

	#Switch players
	turn=(turn+1)%PLAYERS

print("Game over")
	