import random
import matplotlib.pyplot as plt

from monopoly import MonopolyGame

games = 10000
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
p7 = 0
p8 = 0
def run_test_game(seed=42):
    game = MonopolyGame(
        num_players=8,
        seed=seed,
        verbose=False,
    )
    winner = None

    initial_state = game.reset()
    observation_size = len(initial_state)

    decisions = 0

    while not game.is_game_over():
        # Roll dice and process automatic events until someone must decide.
        game.advance_until_decision()

        if game.is_game_over():
            break

        valid_actions = game.get_valid_actions()

        if not valid_actions:
            raise RuntimeError(
                "The game stopped without any valid actions. "
                f"Pending decision: {game.pending_decision}"
            )

        action = random.choice(valid_actions)
        game.apply_action(action)

        state = game.get_observation(agent_id=0)

        assert len(state) == observation_size, (
            f"Observation changed from {observation_size} "
            f"to {len(state)}"
        )

        assert all(
            isinstance(value, (int, float))
            for value in state
        )

        decisions += 1

    print("Game finished")
    print("Decisions:", decisions)
    print("Turns:", game.turn_count)
    winner = game.get_winner()
    print("Winner:", winner)
    return winner


if __name__ == "__main__":
    for i in range(games):
        winner = run_test_game(seed=i)

        if winner is None:
            continue
        elif winner == 0:
            p1 += 1
        elif winner == 1:
            p2 += 1
        elif winner == 2:
            p3 += 1
        elif winner == 3:
            p4 += 1
        elif winner == 4:
            p5 += 1
        elif winner == 5:
            p6 += 1
        elif winner == 6:
            p7 += 1
        elif winner == 7:
            p8 += 1
        sizes = [p1, p2, p3, p4, p5, p6, p7, p8]

    print(f"P1 wins: {p1}")
    print(f"P2 wins: {p2}")
    print(f"P3 wins: {p3}")
    print(f"P4 wins: {p4}")
    print(f"P5 wins: {p5}")
    print(f"P6 wins: {p6}")
    print(f"P7 wins: {p7}")
    print(f"P8 wins: {p8}")

    if sum(sizes) == 0:
        print("No games produced a winner.")
    else:
        fig, ax = plt.subplots()
        ax.pie(
            sizes,
            labels=["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
            startangle=90,
            autopct="%1.1f%%",
        )
        ax.set_title(f"Random Results Across {games} Games")
        plt.show()
