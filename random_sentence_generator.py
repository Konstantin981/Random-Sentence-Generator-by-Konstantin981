import random

def random_word(words):
    return random.choice(words)

names = ["Peter", "Michell", "Jane", "Steve", "George", "John", "Anne", "Rose"]
places = ["Sofia", "London", "New York", "Tokyo", "Berlin", "Amsterdam", "Paris", "Cape Town"]
verbs = ["eats", "holds", "sees", "plays with", "brings", "takes", "gives"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly", "carefully", "happily"]
nouns = ["stones", "cake", "apple", "laptop", "bikes", "toy", "phones"]
details = ["near the river", "at home", "in the park", "at the mall", "at school", "in the cinema", "near the city center"]

print("This is your first random generated sentence:")
while True:
    random_name = random_word(names)
    random_place = random_word(places)
    random_verb = random_word(verbs)
    random_adverb = random_word(adverbs)
    random_noun = random_word(nouns)
    random_detail = random_word(details)
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} the {random_noun} {random_detail}.")
    print()
    input("Press 'Enter' for to generate a new random sentence.")