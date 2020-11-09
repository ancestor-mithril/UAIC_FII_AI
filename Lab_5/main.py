import functions as f

game_state = f.get_initial_state()
print(f.to_string(game_state))
while True:
    game_over, winner = f.check_final_state(game_state)
    if game_over:
        print("Winner is " + winner)
        break
    try:
        old_coordinates = list(
            map(int, (input("Alegeti piesa pe care doriti sa o mutati prin linie si coloana\n")).split()))
    except Exception as e:
        f.print_error(e)
        continue
    if not f.validate_player_choice(game_state, old_coordinates):
        f.print_error("\nPiesa incorect aleasa\n\n")
        continue
    try:
        new_coordinates = list(map(int, (input("Alegeti unde doriti sa mutati piesa, linie si coloana\n")).split()))
    except Exception as e:
        f.print_error(e)
        continue
    if not f.validate_player_move(game_state, old_coordinates, new_coordinates):
        f.print_error("\nPiesa incorect mutata\n\n")
        continue
    game_state = f.apply_player_move(game_state, old_coordinates, new_coordinates)
    print("mutarea omului")
    print(f.to_string(game_state))
    game_state = f.generate_best_state(game_state)
    print("mutarea calculatorului")
    print(f.to_string(game_state))
