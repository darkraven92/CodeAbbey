class Problem70(object):
    ''' Most Frequent Word '''

    def __init__(self):
        self.seed = int(input())
        self.a = 445
        self.c = 700001
        self.m = 2097152

    @staticmethod
    def lcg(a, c, m, seed):
        ''' Linear Congruential Generator '''
        x = seed
        while True:
            x = (a * x + c) % m
            yield x

    def gen_words(self):
        ''' Generate Random Words '''
        consonants = 'bcdfghjklmnprstvwxz'
        vowels = 'aeiou'
        lcg = self.lcg(self.a, self.c, self.m, self.seed)
        words = []
        for n in range(900000):
            word = ''
            for i in range(6):
                if i % 2 == 0:
                    word += consonants[next(lcg) % 19]
                else:
                    word += vowels[next(lcg) % 5]
            words.append(word)
        return words

    def solve(self):
        ''' Find Most Frequent Word '''
        words = self.gen_words()
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        most_frequent = ''
        count = 0
        for key in word_dict:
            if word_dict[key] > count:
                count = word_dict[key]
                most_frequent = key
        return most_frequent
            
print(Problem70().solve())