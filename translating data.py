# Importa pandas library for inmporting CSV
import pandas as pd
import csv
# Imports the Google Cloud client library
from googletrans import Translator

# Instantiates a client
translater = Translator()


# Translating the text to specified target language
def translate(word):
    translater = Translator()
    # Target language
    dest = 'en'  # Add here the target language that you want to translate to
    # Translates some text into Xhosa
    translation = translater.translate(
        word,
        target_language=dest)

    return (translation)


# Import data from CSV
def importCSV():
    data = pd.read_csv('raw_data.csv')
    countRows = (len(data))

    # Create a dictionary with translated words
    translatedCSV = {"text": []}  # Change the column names accordingly to your coumns names

    # Translated word one by one from the CSV file and save them to the dictionary
    for index, row in data.iterrows():
        translatedCSV["text"].append(translate(row["text"]))

    # Create a Dataframe from Dictionary
    # Save the DataFrame to a  file
    df = pd.DataFrame(data=translatedCSV)
    df.to_csv("translated_data.csv", sep='\t')


# Call the function
importCSV()