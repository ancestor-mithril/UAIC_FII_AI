from functions import get_initial_state
from improved_ai import mini_max, alpha_beta


if __name__ == "__main__":
    mini_max(get_initial_state(), level=4)
    alpha_beta(get_initial_state(), level=4)
