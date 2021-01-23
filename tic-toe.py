def draw_grid(cells):
    print("""
---------
| {0} {1} {2} |
| {3} {4} {5} |
| {6} {7} {8} |
---------
""".format(*cells).replace('_', ' '))


def is_contains_integers(cells):
    moves = [int(x) for x in cells if x.isdigit()]
    if len(moves) == 2:
        return True
    else:
        return False


def is_valid_sequence(cells):
    moves = [int(x) for x in cells if x.isdigit()]
    if moves[0] <= 3 and moves[1] <= 3:
        return True
    else:
        return False


def can_make_move_here(part_cell, idx):
    return part_cell[idx] == '_'


def make_move(cells, chosen_horizontal, chosen_cell):
    first_horizontal = cells[0:3]
    second_horizontal = cells[3:6]
    third_horizontal = cells[6:9]

    if chosen_horizontal == 1:
        if can_make_move_here(first_horizontal, chosen_cell) is True:
            first_horizontal[chosen_cell] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            return validate_game(cells, handle_user_input(input()))
    elif chosen_horizontal == 2:
        if can_make_move_here(second_horizontal, chosen_cell) is True:
            second_horizontal[chosen_cell] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            return validate_game(cells, handle_user_input(input()))
    else:
        if can_make_move_here(third_horizontal, chosen_cell) is True:
            third_horizontal[chosen_cell] = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            return validate_game(cells, handle_user_input(input()))
    return first_horizontal + second_horizontal + third_horizontal


def handle_user_input(user_data):
    print(user_data)
    print(is_contains_integers(user_data))
    if is_contains_integers(user_data) is True:
        if is_valid_sequence(user_data) is True:
            # TODO make a call to make_move function
            return [int(x) for x in user_data if x.isdigit()]
        else:
            print("Coordinates should be from 1 to 3!")
            return handle_user_input(input())
    else:
        print("You should enter numbers!")
        return handle_user_input(input())


def validate_game(cells, user_cells):
    return make_move(cells, user_cells[0], user_cells[1] - 1)


# init the game
def initialize(cells):
    draw_grid(cells)
    new_grid = validate_game(cells, handle_user_input(input()))
    draw_grid(new_grid)


initialize(list(input()))
