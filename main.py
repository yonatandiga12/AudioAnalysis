import os
import re

import nltk
from nltk import word_tokenize

from AddToDB import addTextToDB, saveWordDictInDB, word_count_from_file
from AnalyzeAudioFile import analyzeAudio
from DownloadFromYoutube import downloadFromYoutube
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

#nltk.download('punkt_tab')
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')  # Open Multilingual WordNet

PATH_AUDIO = './AudioFiles/'
PATH_TEXT = 'C:\\Fun projects\\audioAnalysis\\Text Files\\'


def HandlingSentence(text):
    #Removing stop words

    stop_words = set(stopwords.words('english'))
    stemmer = SnowballStemmer("english")
    word_tokens = word_tokenize(text)
    # converts the words in word_tokens to lower case and then checks whether
    # they are present in stop_words or not
    filtered_sentence = [w.lower() for w in word_tokens if not w.lower() in stop_words]

    #Removing punctuations
    nonPunct = re.compile('.*[A-Za-z0-9].*')  # must contain a letter or digit
    filtered = [w for w in filtered_sentence if nonPunct.match(w)]


    #Lemminaizing
    textSplited = filtered
    lemmatizer = WordNetLemmatizer()

    resDict = {}
    for currWord in textSplited:
        lemminizedWord = lemmatizer.lemmatize(currWord)
        #print(f'{currWord} : {lemminizedWord}')
        if lemminizedWord in resDict.keys():
            resDict[lemminizedWord] += 1
        else:
            resDict[lemminizedWord] = 1

    #Prints sorted by Value (Number of Occurrence)
    for key, value in sorted(resDict.items(), key=lambda x: x[1], reverse=True):
        print("{} : {}".format(key, value))

    return resDict


def readTextFiles():

    # Change the directory
    os.chdir(PATH_TEXT)

    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{PATH_TEXT}{file}"

            with open(file_path, 'r') as f:
                text = f.read()

                wordsDict = HandlingSentence(text)
                dateStr = file.split('-')[0].strip()
                saveWordDictInDB(wordsDict, dateStr)







if __name__ == '__main__':

    #downloadFromYoutube()
    # nameOfFile = '8.10'
    # nameOfWAV = nameOfFile + '.wav'
    # text = analyzeAudio(PATH_AUDIO + nameOfWAV)
    # addTextToDB(text, PATH_TEXT, nameOfFile)

    #After the text is being saved convert it to english and let the lemminaizer have it.


    #readTextFiles()
    word_count_from_file(PATH_TEXT)


