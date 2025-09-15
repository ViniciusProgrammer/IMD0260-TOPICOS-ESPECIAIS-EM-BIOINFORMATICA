import sys

def substr_locs(string, substr):

    match_idx = []
    k = len(substr)
    for i in range(len(string) - k + 1):
        if string[i:i+k] == substr:
            match_idx.append(i + 1)
    return match_idx

if __name__ == "__main__":

    input_lines = sys.stdin.read().splitlines()
    s = input_lines[0]
    t = input_lines[1]
    result = (substr_locs(s, t))
    print(' '.join([str(idx) for idx in result]))