# Libraries for preprocessing function
import re


def processData(message):
    review = re.sub('\W', ' ', message)
    review = review.lower()
    return review