import sys
from random import choice

class SimpleMarkovGenerator(object):
    text = ''
    def read_files(self, filenames):
        corpus = open(filenames).read()
        return corpus

    def make_chains(self, corpus):
        """Takes input text as string; returns dictionary of markov chains."""

        self.chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in self.chains:
                self.chains[key] = []

            self.chains[key].append(value)

            # or we could say "chains.setdefault(key, []).append(value)"

        return self.chains


    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(self.chains.keys())
        print "key", key
        words = [key[0], key[1]]
        print words[0][0]
        while words[0][0].isupper() == False:
            print words[0][0]
            key = choice(self.chains.keys())
            words = [key[0], key[1]]
        while key in self.chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(self.chains[key])
            words.append(word)
            key = (key[1], word)
        
        text =  " ".join(words)
        self.text = text
        return text

    # def __init__(self):
    #     input_path = sys.argv[1]
    #     input_text = self.read_files(input_path)

    #     # Get a Markov chain
    #     chains = self.make_chains(input_text)

    #     # Produce random text
    #     random_text = self.make_text(chains)

    #     print random_text
import sys
from random import choice

class SimpleMarkovGenerator(object):
    text = ''
    def read_files(self, filenames):
        corpus = open(filenames).read()
        return corpus

    def make_chains(self, corpus):
        """Takes input text as string; returns dictionary of markov chains."""

        self.chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in self.chains:
                self.chains[key] = []

            self.chains[key].append(value)

            # or we could say "chains.setdefault(key, []).append(value)"

        return self.chains


    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(self.chains.keys())
        words = [key[0], key[1]]
        while key in self.chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(self.chains[key])
            words.append(word)
            key = (key[1], word)
        
        text =  " ".join(words)
        self.text = text
        return text

# class MakeLowercaseMixin(object):
#     def lowercase(self):
#         self.text = self.text.lower()

# class RemovePuncMixin(object):
#     def removepunctuation(self):
#         for char in self.text:
#             if char.isalpha() == False and char != ' ':
#                 self.text = self.text[:self.text.index(char)] + self.text[self.text.index(char)+1:]


class TweetableMarkovGenerator(SimpleMarkovGenerator):
    text = ''
    def make_text(self):
        longstring = super(TweetableMarkovGenerator, self).make_text()
        tweet = ''
        for char in longstring:
            if len(tweet) < 140:
                tweet += char
        
        for char in tweet:

            if tweet[-1] == '?' or tweet[-1] == '!' or tweet[-1] == '.':
                break
            else:
                tweet = tweet[:-1]
        self.text = tweet
        return tweet



if __name__ == "__main__":
    filenames = sys.argv[1]
    sample = TweetableMarkovGenerator()
    input_text = sample.read_files(filenames)
    sample.make_chains(input_text)
    sample.text = sample.make_text()
    print sample.text