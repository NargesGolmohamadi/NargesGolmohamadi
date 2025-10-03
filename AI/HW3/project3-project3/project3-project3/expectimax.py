from board import Board
from utils import raiseNotDefined
import random

def expectimax(board, depth, maximizing_player, player_color):

    if depth == 0 or board.is_full():
        return (None,evaluate_board(board,player_color))

    valid_moves =board.get_valid_moves(player_color)
    if not valid_moves:
        return (None,evaluate_board(board,player_color))

    next_color ='W' if player_color =='B' else 'B'
    best_move =None
    best_score = float('-inf') if maximizing_player else float('inf')

    score_sum = 0 

    for row,col in valid_moves:
        new_board =copy_board(board)
        new_board.place_disc(row,col,player_color)

        __,score =expectimax(new_board,depth-1,not maximizing_player,next_color)


        if maximizing_player:
            if score > best_score:
                best_score =score
                best_move =(row,col)
        else:
            score_sum += score


    if not maximizing_player:
        best_score = score_sum / len(valid_moves)

    return (best_move, best_score)

def evaluate_board(board, player_color):
    B_score, W_score = board.get_score()
    return W_score - B_score if player_color == 'W' else B_score - W_score

def copy_board(board):
    new_board = Board(board.size)
    new_board.board = [row[:] for row in board.board]
    return new_board
