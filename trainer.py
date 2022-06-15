from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
     "./knowledge/emotion.yml",
     "./knowledge/logic.yml",
)

def brain(user_input):
    response = chatbot.get_response(user_input)
    return response