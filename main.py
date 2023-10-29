import chatbot_service

def main():
    # Tirar o comentário para extrair os dados do csv e formar no txt
    # chatbot_service.import_data_from_dataset()

    training_array = chatbot_service.mount_array_4_training()


if __name__ == "__main__":
    main()
