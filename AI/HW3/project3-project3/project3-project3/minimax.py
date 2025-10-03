from board import Board
from utils import raiseNotDefined

def minimax(board, depth, maximizing_player, player_color, use_pruning=True, alpha=-float('inf'), beta=float('inf')):

   
    if  depth == 0 or board.is_full(): 
        return ((None,None),evaluate_board(board,player_color))  


    valid_moves =board.get_valid_moves(player_color)
    if not valid_moves:
        return ((None,None),evaluate_board(board, player_color))  


    next_color = 'W' if player_color == 'B' else 'B'
    best_move = None
    best_score = float('-inf') if maximizing_player else float('inf')  

    for row,col in valid_moves:
      
        new_board =copy_board(board) 
        new_board.place_disc(row,col,player_color)

        __,score = minimax(new_board,depth - 1,not maximizing_player,next_color,use_pruning,alpha,beta)

        if maximizing_player:
             if score > best_score:
                 best_score =score
                 best_move = (row,col)
             if use_pruning:
                 alpha = max(alpha,best_score)
                 if beta <= alpha:  
                     break  

        else:
            if score < best_score:
                best_score = score
                best_move =(row,col)
            if use_pruning:
                beta = min(beta,best_score)
                if beta <= alpha:  
                    break 

    return (best_move,best_score)



def evaluate_board(board : Board, player_color):

    #improve the evaluation function 

    scores =board.get_score()
    player_score =scores[0] if player_color == 'B' else scores[1]
    opponent_score =scores[1] if player_color == 'B' else scores[0]

    score_diff =player_score - opponent_score


    corners = [(0,0),(0,board.size-1), (board.size-1,0), (board.size-1,board.size-1)]
    

    corner_control = 0
    
    for (i, j) in corners:
        
         
        if board.board[i][j] == player_color:
            corner_control += 1
      
        elif board.board[i][j] != '.':
            corner_control -= 1

    return score_diff +5* corner_control



def copy_board(board):
    """
    Creates a deep copy of the current board to simulate future moves without altering the original.

    Args:
        board (Board): The current game board to be copied.

    Returns:
        Board: A new Board object with the same state as the original.
    """
    new_board = Board(board.size)
    new_board.board = [row[:] for row in board.board]
    return new_board