"""Lab 7: Forward and backward chaining with simple propositional rules."""


# Each rule is (conditions, conclusion).
RULES = [
    (("A", "B"), "C"),
    (("C",), "D"),
    (("D",), "E"),
]


def forward_chaining(initial_facts, rules):
    facts = set(initial_facts)
    changed = True

    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(condition in facts for condition in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    print(f"Inferred {conclusion} from {conditions}")
                    changed = True
    return facts


def backward_chaining(goal, facts, rules, seen=None):
    """Return True if the goal can be proved from facts and rules."""
    if goal in facts:
        return True
    if seen is None:
        seen = set()
    if goal in seen:
        return False
    seen.add(goal)

    for conditions, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining(condition, facts, rules, seen.copy())
                   for condition in conditions):
                return True
    return False


def main():
    facts = {"A", "B"}
    print("Initial facts:", sorted(facts))

    print("\nForward chaining:")
    derived_facts = forward_chaining(facts, RULES)
    print("All known facts:", sorted(derived_facts))

    print("\nBackward chaining:")
    goal = "E"
    can_prove = backward_chaining(goal, facts, RULES)
    print(f"Can we prove {goal}? {'Yes' if can_prove else 'No'}")


if __name__ == "__main__":
    main()
