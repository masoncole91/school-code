# Name: Mason Blanford
# Course: CS 325 (Algorithms)
# Assignment: 3

def dna_match_topdown(DNA1, DNA2):
    """find the longest, non-continuous length shared by two DNA sequences;
    use a top-down (i.e., whole to subproblem) approach;
    taken from:
    - Exploration 3.3: Dynamic Programming - Longest Common Subsequence Problem"""

    # store past answers
    memo = {}

    def lcs(seq1, seq2, pos1, pos2):
        """dna_match_topdown() helper function;
        taken from:
        - Exploration 3.3: Dynamic Programming - Longest Common Subsequence Problem"""

        # check if sub-problem computed first
        if (pos1, pos2) in memo:
            return memo[(pos1, pos2)]

        # check conditions, return current solution
        if pos1 < 0 or pos2 < 0:
            memo[(pos1, pos2)] = 0
        elif seq1[pos1] == seq2[pos2]:
            memo[(pos1, pos2)] = 1 + lcs(seq1, seq2, pos1 - 1, pos2 - 1)
        else:
            memo[(pos1, pos2)] = max(lcs(seq1, seq2, pos1 - 1, pos2), lcs(seq1, seq2, pos1, pos2 - 1))

        # return for outer function
        return memo[(pos1, pos2)]

    return lcs(DNA1, DNA2, len(DNA1) - 1, len(DNA2) - 1)

def dna_match_bottomup(DNA1, DNA2):
    """find the longest, non-continuous length shared by two DNA sequences;
    use a bottom-up (i.e., subproblem-to-whole) approach;
    taken from:
    - Exploration 3.3: Dynamic Programming - Longest Common Subsequence Problem"""

    # init matrix for tabulation
    y_plot, x_plot = len(DNA1), len(DNA2)
    cache = [[0 for col in range(x_plot + 1)] for row in range(y_plot + 1)]

    # as with top-down, check conditions and return solution
    for col in range(y_plot + 1):
        for row in range(x_plot + 1):
            if col == 0 or row == 0:
                cache[col][row] = 0
            elif DNA1[col - 1] == DNA2[row - 1]:
                cache[col][row] = cache[col - 1][row - 1] + 1
            else:
                cache[col][row] = max(cache[col - 1][row], cache[col][row - 1])

    return cache[y_plot][x_plot]
