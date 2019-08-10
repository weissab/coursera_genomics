#!/c/Users/Andrea/Anaconda3/python


import sys
import matplotlib.pyplot as plt
from libs.utils import read_fastq, phred33toQ


# import file from website with ipython
# !wget --no-check http:// ... 


def parse_args(argv):
    filename = argv[1]
    return filename


def N_by_pos(reads):
    N = [0] * 100
    total = [0] * 100
    N_dict = {}
    for read in reads:
        for i in range(len(read)):
            if read[i] == 'N':
                N[i] += 1
            total[i]+= 1
        for i in range(len(N)):
            if total[i]>0:
                N[i] /= float(total[i])
                N_dict[i] = {N[i]}
        return N, N_dict

""" def calc_QS(phred):
    for read in phred:
        QS = [0] * len(read)
        for i in range(len(read)):
            qual = phred33toQ(i)
            QS[i] = qual
    return QS   """


def plot(N):
    plt.plot(range(len(N)), N)
    plt.show()


def main():
    filename = parse_args(sys.argv)
    reads, _ = read_fastq(filename)
    N, N_dict = N_by_pos(reads)
    print(N_dict)
    plot(N)
    #QS = calc_QS(phred)
    

if __name__ == '__main__':
    main()