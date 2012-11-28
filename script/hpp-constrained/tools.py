import os
import datetime

def playPath (cl, robot, path):
    length = cl.problem.pathLength (robot, path)
    for i in range (101):
        l = i*length/100.
        cfg = cl.problem.configAtDistance (robot, path, l)
        cl.robot.setCurrentConfig (robot, cfg)

def isfloat (string) :
    try :
        float (string)
    except ValueError as exc :
        return False
    return True
    
def parseConfigInLog (pid, prefix):
    listConfig = []
    devel_dir = os.getenv ('DEVEL_DIR')
    with open (devel_dir + '/stable/var/log/hpp/journal.' + str(pid) + '.log',
               'r') as f:
        for line in f:
            if line[:len(prefix)] == prefix:
                configString = line [len(prefix):].strip(' ')
                config = map (float, filter (isfloat, configString.split (' ')))
                listConfig.append (config)
    return listConfig

def parseLineInLog (pid, prefix):
    nbLines = 0
    devel_dir = os.getenv ('DEVEL_DIR')
    with open (devel_dir + '/stable/var/log/hpp/journal.' + str(pid) + '.log',
               'r') as f:
        for line in f:
            if line[:len(prefix)] == prefix:
                nbLines += 1
    return nbLines

def parseTimeInBenchmark (pid, prefix):
    listTime = []
    devel_dir = os.getenv ('DEVEL_DIR')
    with open (devel_dir + '/stable/var/log/hpp/benchmark.' + str(pid) + '.log',
               'r') as f:
        for line in f:
            if line[:len(prefix)] == prefix:
                timeString = line [len(prefix):].strip (' ')
                t = timeString.split (':')
                listTime.append (datetime.timedelta (hours = int (t [0]),
                                                     minutes = int (t [1]),
                                                     seconds = float (t [2])))
    return listTime
