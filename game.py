import chess.engine
from utils import *
import datetime
import chess
import time


def game():

    engine = Engine()

    game = GameSaver()
    game.headers['Event'] = 'Example'
    game.headers['Date'] = datetime.datetime.today().strftime(
        '%Y-%m-%d-%H:%M:%S')
    gameplay_time = 10

    # uncomment the following line and comment the line after that to both sides would be AI
    white = Player('white')

    #white = Player('white', engine)

    game.headers['White'] = 'Human'

    black = Player('black')
    game.headers['Black'] = 'AI'

    board = chess.Board()

    white_turn = True

    p1 = 'White'
    p2 = 'Black'
    print(
        f"White: {game.headers['White']}, Black: {game.headers['Black']}")
    if white_turn:
        print('Player1: White')
    else:
        print('Player1: Black')
    print('-- Initial State --')
    print(board, '\n\n')

    start = time.time()
    times_up = False
    while not board.is_game_over():
        elapsed = time.time()

        if white_turn:
            move = white.play(board)
        else:
            move = black.play(board)

        elapsed = time.time() - elapsed

        print(
            f"{game.headers['White'] if white_turn else game.headers['Black']}'s move: {move}")
        print(
            f'Move computed in {datetime.timedelta(seconds=elapsed)} seconds')

        white_turn = not white_turn
        board.push(move)
        game.add_action(move, board, elapsed)

        print(board, '\n\n')
        now = time.time()
        if(now - start > gameplay_time):
            times_up = True
            break

        print(f"{p1 if white_turn else p2}'s turn")

    game.headers["Result"] = board.result()

    if times_up:
        print('Times up!')
    else:
        engine.quit()

    if game.headers["Result"] == '1/2-1/2':
        print('Draw')
    else:
        print(f'The winner is {game.headers["Result"]}')

    game_duration = time.time() - start
    print(f'C:{5}, - took {datetime.timedelta(seconds=game_duration)}')


game()
