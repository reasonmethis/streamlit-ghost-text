import random

topics = ["cows", "spongecake", "cacti", "muffins vs cupcakes", "durians", "ponies"]
topics += ["the chupacabra", "Bigfoot", "pigeons", "socks with sandals", "fluprgoops"]

transition_phrases = ["And", "Also,", "By the way,", "On another note,", "Oh, and"]

opinion_prompts = [
    "what's your opinion on",
    "what do you think about",
    "how do you feel about",
    "what are your thoughts on",
    "what's your take on",
    "what's your stance on",
    "what's your perspective on",
]


def make_silly_question() -> str:
    topic = random.choice(topics)
    transition = random.choice(transition_phrases)
    opinion_prompt = random.choice(opinion_prompts)
    return f"{transition} {opinion_prompt} {topic}?"


substitutions = {"i": "you", "to you": "to me", "you": "I", "me": "you"}
substitutions |= {"my": "your", "your": "my", "am": "are", "are": "am"}

yes_words = ["Absolutely", "Definitely", "Certainly", "Of course", "Surely"]
yes_words += ["Indeed", "Indubitably", "Without a doubt", "Yes my friend"]


def make_silly_reply(msg: str) -> str:
    words = msg.replace(",", "").lower().rstrip().rstrip(".!?").split()
    words = [substitutions.get(word, word) for word in words]

    if len(words) > 2 and words[0].startswith("wh"):
        if words[2] == "I":
            words[:3] = [words[2], words[1]]
        else:
            del words[:2]

    yes_word = random.choice(yes_words)
    return f"{yes_word}, {' '.join(words)}!"
