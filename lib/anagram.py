# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        return [candidate for candidate in candidates if self.is_anagram(candidate)]

    def is_anagram(self, candidate):
        candidate = candidate.lower()
        return sorted(candidate) == sorted(self.word) and candidate != self.word
