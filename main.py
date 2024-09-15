import os
import re

import nltk
from nltk import word_tokenize

from AddToDB import addTextToDB, saveWordDictInDB
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
                saveWordDictInDB(wordsDict)







if __name__ == '__main__':

    #downloadFromYoutube()
    # nameOfFile = '8.10'
    # nameOfWAV = nameOfFile + '.wav'
    # text = analyzeAudio(PATH_AUDIO + nameOfWAV)
    # addTextToDB(text, PATH_TEXT, nameOfFile)

    #After the text is being saved convert it to english and let the lemminaizer have it.

#     text = """
#
# Good evening. Iran has launched unmanned aerial vehicles (UAVs) from its territory toward Israeli territory. We are monitoring the threat in the airspace; it takes several hours for these threats to reach Israeli territory. The IDF and the Air Force are executing the pre-prepared plan that we have been preparing for. As part of this preparation, GPS services will be unavailable in certain areas; this disruption is intentional and according to the plan. If we detect additional threats with a shorter arrival time, we will update you immediately.
#
# You are asked to remain alert and follow Home Front Command instructions. We are familiar with these threats and have dealt with them in the past. If an alert is activated in your area, you must enter a protected space and stay there for at least 10 minutes—no less. We will update you if you need to remain in the protected space for a longer time. I urge you to avoid spreading rumors and unverified reports. Stay updated through official IDF spokesperson messages and Home Front Command guidelines. I will continue to update here on any changes.
#
# Keep acting responsibly and calmly, as you have done so far, and make sure to follow the instructions. The IDF is fully prepared on all its fronts for defense and attack. We have been prepared in advance for a variety of scenarios. We are working in close cooperation with the United States and our regional partners to act against the launches and intercept them. We have multiple layers of security from the Air Force and Navy, along with additional security circles from the U.S. military. We have an excellent aerial defense system, and it is currently fully operational. However, remember that defense is never airtight, so it is crucial to follow the guidelines and listen to the Home Front Command's instructions—they save lives.
#     """

    readTextFiles()


