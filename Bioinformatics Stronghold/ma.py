import sys

def transcribe(string):

    return string.replace('T', 'U')

if __name__ == "__main__":

    DNA_seq = sys.stdin.read().splitlines()[0]
    print(transcribe(DNA_seq))