

def main():
    regex = ''
    with open('rosalind_gbk.txt', 'r') as f:
        for line in f:
            if 'regular expression' in line:
                next(f)
                while True:
                    line = f.readline()
                    if '-' not in line:
                        regex += line.rstrip()
                    else:
                        break
    with open('rosalind_meme.txt', 'w') as outfile:
        outfile.write(regex)
    print('Regular expression =', regex)

if __name__ == '__main__':
    main()