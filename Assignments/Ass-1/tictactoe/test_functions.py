from tictactoe import * 
# Test player()
board1 = initial_state()  
assert player(board1) == X, "X should go first" 
board2 = [[X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]] 
assert player(board2) == O, "O should go after X" 
#Test actions()
board3 = [[X, O, X], [O, X, O], [EMPTY, EMPTY, EMPTY]] 
assert actions(board3) == {(2,0), (2,1), (2,2)} 
# Test winner() 
board_x_wins = [[X, X, X], [O, O, EMPTY], [EMPTY, EMPTY, EMPTY]] 
assert winner(board_x_wins) == X 
# Test terminal() 
assert terminal(board_x_wins) == True
assert terminal(initial_state()) == False
print("All tests passed!")