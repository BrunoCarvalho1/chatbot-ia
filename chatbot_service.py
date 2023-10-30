import ast
import csv
import translator


def mount_array_4_training():
    training_array = []
    with open('training_file.txt') as training_file:
        for row in training_file:
            training_array.append(row.strip())
    
    return training_array


def import_data_from_dataset():
    with open('movies_metadata.csv') as csvfile:
        for row in csv.DictReader(csvfile):
            for genre in ast.literal_eval(row['genres']):
                question = "Me recomende um filme de "
                response = "Claro! Aqui está um filme de "

                question += f"{genre['name']}\n"
                response += f"{genre['name']}. Nome do filme: {row['title']}. Descrição do filme: {row['overview']}. Data de lançamento: {row['release_date']}"

                with open('training_file.txt', 'a') as training_file:
                    training_file.write(translator.translate_text(question).replace("recomendo", "recomende") + "\n")
                    training_file.write(translator.translate_text(response).replace("recomendo", "recomende") + "\n")
