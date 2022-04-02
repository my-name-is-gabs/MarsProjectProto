import arrow


# mars = MarsRecognition()

# def setTimer(timeValue):
#     '''
#     setTimer(timeValue: string)

#     The timer method takes minutes and seconds only.
#     It returns minutes and seconds format in a string.

#     return "minutes:seconds"
        
#     '''
#     try:
#         minute_position = timeValue.find('minute') or timeValue.find('minutes')
#         seconds_position = timeValue.find('second') or timeValue.find('seconds')

#         if seconds_position == -1:
#             addminute = timeValue[0: minute_position]
#             addseconds = 0

#         elif minute_position == -1:
#             addminute = 0
#             addseconds = timeValue[0: seconds_position]

#         else:
#             addminute = timeValue[0: minute_position]
#             addseconds = timeValue[minute_position + len("minutes"): seconds_position]

#         startMinutes = arrow.now().format('m')
#         startSeconds = arrow.now().format('s')

#         newMinutes = int(startMinutes) + int(addminute)
#         newSeconds = int(startSeconds) + int(addseconds)

#         expire = str(newMinutes) + ':' + str(newSeconds)

#         while True:
#             timenow = arrow.now().format('m:s')
#             if expire == timenow:
#                 mars.speak("Your time is up")
#                 break
        

#     except:
#         mars.speak("something went wrong in marsDateTime module")
#         exit()

def getFullDate():
    year = arrow.now().format('YYYY')
    month = arrow.now().format('MMMM')
    day = arrow.now().format('DD')
    
    return f'{month} {day}, {year}'
    
def getDay():
    return arrow.now().format('dddd')
    
def getTime():
    return arrow.now().format('HH:m A')


if __name__ == "__main__":
    print("This is from the marsDateTimeUtil module")
    getFullDate()
        
