import time


def timer(f):
    def inner(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        print("Time:", end - start)

    return inner


def prefix(pattern):
    m = len(pattern)
    lt = 0
    arr = [0] * m
    i = 1
    while i < m:
        if pattern[i] == pattern[lt]:
            lt += 1
            arr[i] = lt
            i += 1
        else:
            if lt != 0:
                lt = arr[lt-1]
            else:
                arr[i] = 0
                i += 1

    return arr


class PatternFinder:

    def __init__(self, pattern: str, text: str, do_print=True):
        self.pattern = pattern.replace('\n', '')
        self.text = text.rstrip('\n')
        self.line_positions = [pos for pos, char in enumerate(self.text) if char == "\n"]
        self.line_positions = [pos - i for i, pos in enumerate(self.line_positions)]
        self.text = self.text.replace('\n', '')
        self.found_patterns = 0
        if do_print:
            print("Pattern:", self.pattern)
            print("Text:", self.text)
            print("First sign index of every line", self.line_positions)

    def position(self, position):
        for line, line_start in enumerate(self.line_positions):
            if line_start > position:
                return line, position - self.line_positions[line - 1] if line != 0 else position
        else:
            return line+1, position - self.line_positions[line] if line != 0 else position

    def print_pattern(self, position):
        line, position = self.position(position)
        print("Found pattern at L:", str(line) + ',', "P:", position)

    @timer
    def naive(self, do_print=True):
        self.found_patterns = 0
        pattern = self.pattern
        text = self.text

        for pos, char in enumerate(text):
            if pattern == text[pos: pos + len(pattern)]:
                # print("Found pattern at L:", str(line_number)+',', "P:",
                #       pos - self.line_positions[line_number - 1] if line_number != 0 else pos)
                line, position = self.position(pos)
                if do_print: print("Found pattern at L:", str(line)+',', "P:", position)
                self.found_patterns += 1
        print("Found patterns:", self.found_patterns)

    @timer
    def rabin_karp(self, do_print=True):
        self.found_patterns = 0
        pattern = self.pattern
        text = self.text
        d = 128
        q = 27077

        m = len(pattern)
        n = len(text)

        h = d**(m-1) % q

        p = 0
        t = 0
        for i in range(m):
            p = (d*p + ord(pattern[i])) % q
            t = (d*t + ord(text[i])) % q

        for i in range(n-m):
            proposition = text[i:i+m]
            if p == t:
                if pattern == proposition:
                    if do_print: self.print_pattern(i)
                    self.found_patterns += 1
            if i < n-m:
                t1 = (ord(text[i])*h) % q
                if t < t1:
                    t = t+q
                t = (d*(t-t1) + ord(text[i+m])) % q

        print("Found patterns:", self.found_patterns)

    @timer
    def knuth_morris_pratt(self, do_print=True):
        self.found_patterns = 0
        pattern = self.pattern
        m = len(pattern)
        text = self.text
        prefixes = prefix(pattern)
        q = 0
        for i in range(len(text)):
            while q > 0 and pattern[q] != text[i]:
                q = prefixes[q-1]
            if pattern[q] == text[i]:
                q += 1
            if q == m:
                if do_print: self.print_pattern(i - m + 1)
                q = prefixes[q-1]
                self.found_patterns += 1

        print("Found patterns:", self.found_patterns)
