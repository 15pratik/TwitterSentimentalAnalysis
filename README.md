# TwitterSentimentalAnalysis
The “happiness score” for a single tweet is found by looking for certain keywords in a tweet and for each keyword found in that tweet totaling their “sentiment values”. The “happiness score” for each timezone is computed.

# Files
The Python code happy_histogram.py does simple graph plotting using graphics.py. You will need to import happy_histogram.py into the main program sentimentAnalysis.py. It makes a number of assumptions, so make sure to read the comments in the code about the parameters and limitations of the functions. It contains three functions:
- drawSimpleHistogram which will create a histogram of four values in a graphics window; it assumes that the values are in the range of 0-10.
- drawHappyFace which draws a happy face on the histogram as determined by drawSimpleHistogram.
- drawSadFace which draws a sad face on the histogram as determined by drawSimpleHistogram.
