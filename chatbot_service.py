import ast
import csv

def import_data_from_dataset():
    with open('movies_metadata.csv') as csvfile:
        for row in csv.DictReader(csvfile):
            for genre in ast.literal_eval(row['genres']):
                question = "Me recomende um filme de "
                response = "Claro! Aqui está um filme de "

                question += f"{genre['name']}\n"
                response += f"{genre['name']}. Nome do filme: {row['title']}. Descrição do filme: {row['overview']}. Data de lançamento: {row['release_date']}"

                with open('training_file.txt', 'a') as training_file:
                    training_file.write(question)
                    training_file.write(response)
