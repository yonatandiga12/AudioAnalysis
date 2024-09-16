import os
from collections import Counter
import csv


CSV_NAME = 'CsvWords.csv'

def addTextToDB(text, path, nameOfFile):
    pathToSave = path + nameOfFile + '.txt'

    with open(pathToSave, "a") as f:
        f.write(text)


def word_count_from_file(file_path):
    csvPath = file_path + CSV_NAME
    with open(csvPath, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = text.split()  # simple split, adjust for more complex tokenization

        #words is all the words from all dates, need to filter it with dates

        return None


def saveWordDictInDB(wordsDict, dateStr):
    # Create or append to the CSV file
    file_exists = os.path.isfile(CSV_NAME)

    with open(CSV_NAME, mode='a', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['date', 'word', 'count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # Write header only if file doesn't exist

        for word, count in wordsDict.items():
            writer.writerow({'date': dateStr, 'word': word, 'count': count})
