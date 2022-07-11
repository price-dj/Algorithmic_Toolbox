import sys

def optimal_weight(W, wt):
    """Find max weight that can fit in knapsack size W."""
    # Create n nested arrays of 0 * (W + 1)
    max_vals = [[0] * (W + 1) for x in range(len(wt))]
    # Set max_vals[0] to wt[0] if wt[0] <= j
    max_vals[0] = [wt[0] if wt[0] <= j else 0 for j in range(W + 1)]
    for i in range(1, len(wt)):
        for j in range(1, W + 1):
            value = max_vals[i - 1][j]  # previous i @ same j
            if wt[i] <= j:
                val = (max_vals[i - 1][j - wt[i]]) + wt[i]
                if value < val:
                    value = val
                    max_vals[i][j] = value
                else:
                    max_vals[i][j] = value

    return max_vals[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *wt = list(map(int, input.split()))
    print(optimal_weight(W, wt))
    
    
    if value < val:
                value = val
                max_vals[i][j] = value
            else:
                max_vals[i][j] = value  # set to [i - 1][j]
        else:
            max_vals[i][j] = value   # set to [i - 1][j]
