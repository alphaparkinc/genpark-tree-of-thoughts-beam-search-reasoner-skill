from client import TreeOfThoughtsReasoner

tot = TreeOfThoughtsReasoner(beam_width=2, max_depth=2)

def expand(state, depth):
    return [f"{state}->option_A", f"{state}->option_B"]

def evaluate(state):
    # Favor option_B on step 1, option_A on step 2
    score = 0.0
    if "option_B" in state: score += 1.0
    if "option_A" in state: score += 0.5
    return score

best_state, score = tot.search("root", expand, evaluate)
print(f"Optimal reasoning trajectory: {best_state} (Heuristic Score: {score:.2f})")
