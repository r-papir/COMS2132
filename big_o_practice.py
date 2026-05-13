"""
big_o_practice.py — Algorithm Analysis Practice Quiz
Based on COMS W2132 lecture notes (04-algorithm-analysis)
Run with: python3 big_o_practice.py
"""

import random

questions = [
    {
        "cat": "Big-O basics",
        "q": "What is the Big-O classification of 3n + 9?",
        "opts": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        "ans": 2,
        "exp": "3n + 9 <= 4n for all n >= 9, so 3n + 9 is O(n). Constants and lower-order terms are dropped."
    },
    {
        "cat": "Big-O basics",
        "q": "Which statement correctly describes the Big-O definition f(n) <= c * g(n)?",
        "opts": [
            "f(n) is a tighter bound than g(n) for all n",
            "f grows at most as fast as g, up to a constant factor, for sufficiently large n",
            "f(n) equals g(n) for all values of n",
            "f(n) must be less than g(n) for every n >= 1"
        ],
        "ans": 1,
        "exp": "Big-O says f grows no faster than g beyond some threshold n0, ignoring the constant c. It doesn't require equality or strict inequality for all n."
    },
    {
        "cat": "Growth rates",
        "q": "Order these growth rates from slowest to fastest: n log n, 2^n, log n, n^2, n",
        "opts": [
            "log n < n < n log n < n^2 < 2^n",
            "log n < n log n < n < n^2 < 2^n",
            "n < log n < n log n < 2^n < n^2",
            "log n < n < n^2 < n log n < 2^n"
        ],
        "ans": 0,
        "exp": "The correct ordering is: constant < log n < n < n log n < n^2 (polynomial) < 2^n (exponential). This is the standard hierarchy of essential growth functions."
    },
    {
        "cat": "Big-O proofs",
        "q": "To show 2^(n+2) is O(2^n), what constant c works?",
        "opts": ["c = 1", "c = 2", "c = 4", "c = n"],
        "ans": 2,
        "exp": "2^(n+2) = 2^n * 2^2 = 4 * 2^n. So f(n) <= 4 * g(n) for all n >= 1, making c = 4 the natural choice."
    },
    {
        "cat": "Algorithm analysis",
        "q": "What is the worst-case time complexity of find_min on a list of length n?",
        "opts": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        "ans": 2,
        "exp": "find_min iterates through every element exactly once, performing constant-time work per element. Total: c1 + c2*n = O(n)."
    },
    {
        "cat": "Algorithm analysis",
        "q": "Why is worst-case analysis preferred over average-case in this course?",
        "opts": [
            "It always gives a tighter bound",
            "Average-case requires knowing the probability distribution over inputs, which is often hard",
            "Worst-case is always faster to compute",
            "Average-case analysis is inaccurate"
        ],
        "ans": 1,
        "exp": "Average-case analysis requires defining a probability distribution on inputs, which can be hard or impossible to specify correctly. Worst-case gives a reliable upper bound without that assumption."
    },
    {
        "cat": "Prefix average",
        "q": "What is the time complexity of prefix_average1 (the nested loop version)?",
        "opts": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "ans": 2,
        "exp": "The outer loop runs n times; the inner loop runs up to j+1 times. Total work ~= 1 + 2 + ... + n = n(n+1)/2, which is O(n^2)."
    },
    {
        "cat": "Prefix average",
        "q": "What key change makes prefix_average2 run in O(n) instead of O(n^2)?",
        "opts": [
            "It uses binary search to find partial sums",
            "It maintains a running total, avoiding the inner loop",
            "It pre-sorts the list",
            "It uses recursion instead of loops"
        ],
        "ans": 1,
        "exp": "prefix_average2 keeps a running total variable updated in O(1) per iteration, eliminating the inner loop. Total work is O(n)."
    },
    {
        "cat": "Big-Omega / Big-Theta",
        "q": "If f(n) is O(g(n)) AND g(n) is O(f(n)), then:",
        "opts": [
            "f(n) is Omega(g(n))",
            "f(n) is Theta(g(n))",
            "f(n) < g(n) always",
            "g(n) is O(1)"
        ],
        "ans": 1,
        "exp": "Big-Theta means both functions grow at the same rate up to a constant factor: c1*g(n) <= f(n) <= c2*g(n). This is exactly satisfied when each is O of the other."
    },
    {
        "cat": "Big-O examples",
        "q": "What is the correct Big-O for 5n^2 + 3n log n + 2n + 5?",
        "opts": ["O(n log n)", "O(n^2)", "O(n^3)", "O(5n^2)"],
        "ans": 1,
        "exp": "The dominant term is 5n^2. Each lower-order term (3n log n, 2n, 5) is also O(n^2), so the sum is O(n^2). Drop coefficients and lower-order terms."
    },
    {
        "cat": "Logarithms",
        "q": "Binary search runs in O(log n) because:",
        "opts": [
            "It visits every element once",
            "It halves the search space each iteration, giving at most log2(n) iterations",
            "It uses constant-time hashing",
            "log n is always less than n"
        ],
        "ans": 1,
        "exp": "Each iteration discards half the remaining list. Starting from n, after k iterations the remaining size is n/2^k. When that reaches 1, k = log2(n), giving O(log n)."
    },
    {
        "cat": "Empirical analysis",
        "q": "What is a key limitation of the empirical (experimental) approach to algorithm analysis?",
        "opts": [
            "It can only be used for sorting algorithms",
            "Results depend on hardware, OS load, and other non-algorithmic factors",
            "It can't measure running time accurately",
            "It works only for algorithms with polynomial complexity"
        ],
        "ans": 1,
        "exp": "Empirical results vary across machines and with OS scheduling. The same find_min runs longer under CPU load — the method measures the environment as much as the algorithm."
    },
    {
        "cat": "Primitive operations",
        "q": "Which of the following is NOT a primitive (constant-time) operation?",
        "opts": [
            "Assigning a value to a variable",
            "Accessing a single element in a Python list",
            "Sorting a sublist",
            "Comparing two numbers"
        ],
        "ans": 2,
        "exp": "Sorting a sublist takes O(k log k) for a sublist of size k — not a primitive operation. Primitive ops include: assignment, arithmetic, comparison, list element access, function call/return."
    },
    {
        "cat": "Induction",
        "q": "In the Fibonacci induction proof that fib(n) < 2^n, the inductive step uses:",
        "opts": [
            "fib(n) = fib(n-1) + n",
            "fib(n) < 2^(n-2) + 2^(n-1) <= 2^n",
            "fib(n) = 2^(n-1)",
            "fib(n) < n^2"
        ],
        "ans": 1,
        "exp": "By the inductive hypothesis, fib(n-2) < 2^(n-2) and fib(n-1) < 2^(n-1). So fib(n) < 2^(n-2) + 2^(n-1) < 2^(n-1) + 2^(n-1) = 2*2^(n-1) = 2^n."
    },
    {
        "cat": "Loop invariants",
        "q": "For the find() function, the loop invariant L_j states:",
        "opts": [
            "val equals S[j] after j iterations",
            "val is not equal to any of the first j elements of S",
            "j has been incremented j times",
            "The list S has j remaining elements to check"
        ],
        "ans": 1,
        "exp": "L_j: 'val != any of S[0]...S[j-1]'. Trivially holds at j=0, maintained each iteration (return if found, else increment), and at j=n proves val isn't in S at all."
    },
    {
        "cat": "Practical implications",
        "q": "Which time complexity is considered infeasible for large inputs?",
        "opts": ["O(n log n)", "O(n^2)", "O(n^3)", "O(2^n)"],
        "ans": 3,
        "exp": "Exponential time O(2^n) is infeasible. Even for n=60, 2^60 ~= 10^18 operations — far beyond any practical computation."
    },
]


def run_quiz(shuffle=True):
    q_list = questions[:]
    if shuffle:
        random.shuffle(q_list)

    score = 0
    total = len(q_list)

    print("\n" + "=" * 60)
    print("  Algorithm Analysis Practice Quiz")
    print("  COMS W2132 — 04-algorithm-analysis")
    print("=" * 60)
    print(f"  {total} questions. Enter the number of your answer.\n")

    for i, q in enumerate(q_list, 1):
        print(f"\n[{i}/{total}] ({q['cat']})")
        print(f"Q: {q['q']}\n")
        for j, opt in enumerate(q["opts"]):
            print(f"  {j + 1}. {opt}")

        while True:
            try:
                choice = int(input("\nYour answer (1-4): ").strip()) - 1
                if 0 <= choice <= 3:
                    break
                print("  Please enter a number between 1 and 4.")
            except ValueError:
                print("  Please enter a number between 1 and 4.")

        if choice == q["ans"]:
            print("\n  ✓ Correct!")
            score += 1
        else:
            print(f"\n  ✗ Incorrect. The answer was: {q['opts'][q['ans']]}")

        print(f"  → {q['exp']}")

    pct = round((score / total) * 100)
    print("\n" + "=" * 60)
    print(f"  Final score: {score}/{total} ({pct}%)")
    if pct >= 85:
        print("  Strong work — you've got this material down.")
    elif pct >= 60:
        print("  Solid foundation. Review the questions you missed.")
    else:
        print("  Keep reviewing — try again after going over the notes.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_quiz()
