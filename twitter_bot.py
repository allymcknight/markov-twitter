import os
import twitter
import markov1
import sys

api = twitter.Api(consumer_key = os.environ["TWITTER_CONSUMER_KEY"],
                    consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"],
                    access_token_key = os.environ["TWITTER_ACCESS_TOKEN_KEY"],
                    access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
)

print api.VerifyCredentials()

# if __name__ == "__main__":
filenames = sys.argv[1]
sample = markov1.TweetableMarkovGenerator()
input_text = sample.read_files(filenames)
sample.make_chains(input_text)
sample.text = sample.make_text()
status = api.PostUpdate(sample.text)