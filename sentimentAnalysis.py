# Author : Pratik Padalia

import happy_histogram

def binarySearch(L, target):
    start = 0
    end = len(L) - 1

    while start <= end:
        middle = (start + end)// 2
        midpoint = L[middle][0]
        midpointVal = L[middle][1]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpointVal
    return 0

def main():
    keywords = [] #List
    words = [] #List
    twCntPacific = 0
    scorePacific = 0
    twCntMountain = 0
    scoreMountain = 0
    twCntCentral = 0
    scoreCentral = 0
    twCntEastern = 0
    scoreEastern = 0

    # Read keywords and store in list
    fileNameKeywords = input("Enter the file name for keyword file: ")
    try:
        # fileKeywords = open(fileNameKeywords, "r")
        fileKeywords = open("keywords.txt", "r")
    except IOError as err:
    	# Error reading file. Quit
        print("Error, File not found!")
        quit()

    for line in fileKeywords:
        # print(line)
        line = line.split(",")
        keywords.append([line[0], int(line[1])])

    keywords.sort() #incase the keywords are not sorted

    fileNameTweets = input("Enter the file name for Tweets file: ")
    try:
        # fileTweets = open(fileNameTweets, "r")
        fileTweets = open("tweets.txt", "r")
    except IOError as err:
    	# Error reading file. Quit
        print("Error, File not found!")
        quit()

    for line in fileTweets:
        # print(line)
        lineContent = line.split(" ", 5)
        latitude = (float)(lineContent[0][1:-1])
        longitude = (float)(lineContent[1][:-1])
        # print(latitude)
        # print(longitude)
        words = lineContent[5].strip(".,@!?/\\:#'\"").split()
        # print(words)
        lineVal = 0

        for x in words:
        	lineVal = lineVal + binarySearch(keywords, x)

        lineScore = lineVal/len(words)
        #Select timezone
        #Latitude Range
        if 24.660845 <= latitude <= 49.189787:
            #Longitude Range
            if -125.242264 <= longitude <= -67.444574:
                #Pacific
                if -125.242264 <= longitude < -115.236428:
        			# print("Pacific")
        	        twCntPacific = twCntPacific + 1
        	        scorePacific = scorePacific + lineScore
                elif -115.236428 <=longitude < -101.998892:
                    # print("Mountain")
                    twCntMountain = twCntMountain + 1
                    scoreMountain = scoreMountain + lineScore
                elif -101.998892 <=longitude < -87.518395:
                    # print("Central")
                    twCntCentral = twCntCentral + 1
                    scoreCentral = scoreCentral + lineScore
                elif -87.518395 <=longitude < -67.444574:
                    # print("Eastern")
                    twCntEastern = twCntEastern + 1
                    scoreEastern = scoreEastern + lineScore
    if twCntPacific>0:
    	PacificHappiness = scorePacific*10/twCntPacific
    else:
    	PacificHappiness = 0
    if twCntMountain>0:
    	MountainHappiness = scoreMountain*10/twCntMountain
    else:
    	MountainHappiness = 0
    if twCntCentral>0:
    	CentralHappiness = scoreCentral*10/twCntCentral
    else:
    	CentralHappiness = 0
    if twCntEastern>0:
    	EasternHappiness = scoreEastern*10/twCntEastern
    else:
    	PacificEastern = 0

    print("Happiness rating of Pacific timezone is %.3f out of 10 for %d tweets." %(round(PacificHappiness, 3), twCntPacific))
    print("Happiness rating of Mountain timezone is %.3f out of 10 for %d tweets." %(round(MountainHappiness, 3), twCntMountain))
    print("Happiness rating of Central timezone is %.3f out of 10 for %d tweets." %(round(CentralHappiness, 3), twCntCentral))
    print("Happiness rating of Eastern timezone is %.3f out of 10 for %d tweets." %(round(EasternHappiness, 3), twCntEastern))

    # drawSimpleHistogram(eval,cval,mval,pval) 
    happy_histogram.drawSimpleHistogram(EasternHappiness, CentralHappiness, MountainHappiness, PacificHappiness)
    fileTweets.close()
    fileKeywords.close()

main()