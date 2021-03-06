#!/usr/bin/env python
from board import Board, LogicException
import sys

# this needs to be smarter soon
if len(sys.argv) > 1:
    _board = Board(sys.argv[1])
else:
    _board = Board('simple.karelmap')

def _refresh(callback):
    def inner():
        res = callback()
        _board.draw()
        return res
    return inner

move = _refresh(_board.move)
turn_left = _refresh(_board.turn_left)
pick_beeper = _refresh(_board.pick_beeper)
put_beeper = _refresh(_board.put_beeper)
front_is_clear = _board.front_is_clear
right_is_clear = _board.right_is_clear
left_is_clear = _board.left_is_clear
beeper_is_present = _board.beeper_is_present
facing_north = _board.facing_north
facing_south = _board.facing_south
facing_east = _board.facing_east
facing_west = _board.facing_west

def execute(callback):
    try:
        _board.start_screen()
        _board.draw()
        callback()
        return callback
    except LogicException, e:
        _board.draw_exception(e)
    except Exception, e:
        raise e
    finally:
        _board.end_screen()
