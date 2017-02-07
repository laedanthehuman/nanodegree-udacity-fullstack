import webbrowser
import time

QUESTION = "Hey What's your favorite video on youtube?\nPlease tell me the link i'm very dump yet!:"
COUNT_START = 0
COUNT_BREAK = 3
YOUTUBE_VIDEO = input(QUESTION)
print("The program is runing at:", time.ctime())
while COUNT_START < COUNT_BREAK:
    time.sleep(10)
    webbrowser.open(YOUTUBE_VIDEO)
    COUNT_START = COUNT_START +1
