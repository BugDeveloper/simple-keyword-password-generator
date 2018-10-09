class PassGenerator:
    words = []
    words_count = 0

    def __init__(self, words, words_count):
        self.words = words
        self.words_count = words_count

    def _generate(self, res, iter=0):
        if iter == self.words_count:
            return res
        if iter == 0:
            res = {}
            buff = self.words
        else:
            buff = res[iter - 1]

        res[iter] = []

        for word_one in buff:
            for word_two in self.words:
                if word_two not in word_one:
                    res[iter].append(word_one + word_two)

        return self._generate(res, iter + 1)

    def generate(self):
        res_array = []
        res = self._generate(None)
        for iter, word_set in res.items():
            for word in word_set:
                res_array.append(word)
        return res_array
