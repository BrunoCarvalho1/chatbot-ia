from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import chatbot_service

chatbot = ChatBot(
    'The sage', 
)

def conversation(text):
    return chatbot.get_response(text)


def start_training():
    # Instância do trainer da lib chatterbot
    trainer = ListTrainer(chatbot)

    # Array para treinamento montado com os valores do training_file (que foi extraído do csv).
    training_array = chatbot_service.mount_array_4_training()

    print('Iniciando treinamento')
    trainer.train(training_array)