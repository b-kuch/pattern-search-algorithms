from PatternFinder import PatternFinder

if __name__ == '__main__':

    # pattern = "a\nb"
    # text = "aaa\nab\nabab\naba\n"
    i = 2
    with open("data/pattern"+str(i)+".txt", "r") as f:
        pattern = f.read()
    with open("data/text"+str(i)+".txt", "r") as f:
        text = f.read()

    do_print = False
    x = PatternFinder(pattern, text, do_print=do_print)
    print("\nNaive:")
    x.naive(do_print=do_print)
    print("\nRabin-Karp:")
    x.rabin_karp(do_print=do_print)
    print("\nKnuth-Morris-Pratt:")
    x.knuth_morris_pratt(do_print=do_print)
