import ast
import csv
import translator


def get_all_genres():
    training_array = mount_array_4_training()
    questions = []
    final = []

    for row in training_array:
        if row.startswith("Me"):
            if "Claro! Aqui está um filme de" in row:
                continue

            questions.append(row)

    for row in questions:
        row = row.split('Me recomende um filme de ')[1]

        if " e " in row:
            row = row.split(" e ")[1]
            final.append(row)

    final = set(final)

    return sorted(final)


def mount_array_4_training():
    training_array = []
    with open('training_file.txt') as training_file:
        for row in training_file:
            training_array.append(row.strip())
    
    return training_array


def import_data_from_dataset():
    with open('movies_metadata.csv') as csvfile:
        for row in csv.DictReader(csvfile):
            # Array que será utilizado para armazenar os gêneros de cada filme
            genres = []

            for genre in ast.literal_eval(row['genres']):
                translated_genre = translator.translate_text_to_portuguese(genre['name'])
                genres.append(translated_genre)

            # Variável para saber se é o último elemento do array
            temp = 1

            # Variável que irá construir a pergunta
            question = "Me recomende um filme de "
            response_genres = ""
            for genre in genres:
                if temp == len(genres):
                    question += f" e {genre}\n"
                    response_genres += f" e {genre}"
                    continue

                if temp == 1:
                    question += f"{genre}"
                    response_genres += f"{genre}"
                    temp += 1
                    continue

                question += f", {genre}"
                response_genres += f", {genre}"
                temp += 1

            description = translator.translate_text_to_portuguese(row['overview'])
            response = "Claro! Aqui está um filme de " + response_genres + f"! Nome do filme: {row['title']}. Descrição: {description} Data de lançamento: {row['release_date']}\n"

            with open('training_file.txt', 'a') as training_file:
                training_file.write(question)
                training_file.write(response)

