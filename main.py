from AddToDB import addTextToDB
from AnalyzeAudioFile import analyzeAudio
from DownloadFromYoutube import downloadFromYoutube

PATH_AUDIO = './Audio Files/'
PATH_TEXT = './Text Files/'

if __name__ == '__main__':

    downloadFromYoutube()
    nameOfFile = '13.4 - 2'
    nameOfWAV = nameOfFile + '.wav'
    #text = analyzeAudio(PATH_AUDIO + nameOfWAV)
    #addTextToDB(text, PATH_TEXT, nameOfFile)



