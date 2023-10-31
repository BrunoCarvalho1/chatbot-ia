import my_chatbot
import chatbot_service
import my_telegram_bot


def main():
    # Remover os comentários para extrair os dados do csv e formar no txt
    # chatbot_service.import_data_from_dataset()

    # Remover o comentário para treinar o bot
    # my_chatbot.start_training()

    # Instância do bot do telegram
    my_telegram_bot.my_bot_instance()


if __name__ == "__main__":
    main()
