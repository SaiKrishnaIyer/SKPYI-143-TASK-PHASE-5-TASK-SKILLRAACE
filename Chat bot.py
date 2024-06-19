import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you.",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, so I don't have an age.",]
    ],
    [
        r"what (.*) want?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created?",
        ["You did, using NLTK.",]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm in the cloud, floating around.",]
    ],
    [
        r"how is the weather in (.*)?",
        ["I don't have access to weather information right now.",]
    ],
    [
        r"(.*)raining in (.*)?",
        ["I don't know if it's raining in %2",]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I don't have health issues.",]
    ],
    [
        r"(.*) (sports|game)?",
        ["I'm a big fan of computer games.",]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["I love Keanu Reeves.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. Bye :)"]
    ],
]

def chatbot():
    print("Hi, I'm the chatbot you built. Start a conversation with me by typing something.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
