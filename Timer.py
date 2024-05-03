import time

def funcStartTimer():
    global fStartTime
    fStartTime = time.time()
    return fStartTime


def funcStopTimer():
    fEndTime = time.time()
    fFinalTime = fEndTime - fStartTime
    return fFinalTime