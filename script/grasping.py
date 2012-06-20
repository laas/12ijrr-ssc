import sys, os
import hpp.corbaserver
import hpp.corbaserver.constrained
from hpp_corbaserver.hpp import Configuration
from tools import parseConfigInLog, parseTimeInBenchmark, parseLineInLog

cl = hpp.corbaserver.Client(['robot', 'obstacle', 'problem'])
clw = hpp.corbaserver.constrained.client.Client()

def setHand (right, alpha, lock):
    if right:
        rank = 28
    else:
        rank = 40
    q = cl.robot.getCurrentConfig (0)
    q[rank:rank+6] = [alpha, -alpha, alpha, -alpha, alpha, -alpha]
    cl.robot.setCurrentConfig (0,q)
    if lock:
        for dof in range (rank, rank+6):
            cl.robot.setDofLocked (0, dof, True, q [dof])

def openHand (right, lock):
    setHand (right, .75, lock)

def closeHand (right, lock):
    setHand (right, .38, lock)

env_dir = os.getenv('HOME')+'/devel/hpp/src/hpp-environment-data/share/hpp-environment/2012ijrr-shelves'

def playPath (robot, path):
    length = cl.problem.pathLength (robot, path)
    for i in range (201):
        l = i*length/200.
        cfg = cl.problem.configAtDistance (robot, path, l)
        cl.robot.setCurrentConfig (robot, cfg)

cl.robot.loadHrp2Model(.05)
half_sitting = cl.robot.getCurrentConfig(0)
cl.problem.initializeProblem()
cl.problem.parseFile(env_dir + "/env.kxml")

nodes = []
edges = []
for i in range (20):
    # Reaching motion starting from half-sitting
    # Set right hand locked open
    openHand (True, True)
    # Set left hand lock closed
    closeHand (False, True)
    q = cl.robot.getCurrentConfig (0)
    q_init = q [::]
    cl.problem.setInitialConfig(0, q)
    if clw.problem.setTarget (0.62, 0.07, 1.02) != 0:
        raise RuntimeError ("Failed to set target.")
    clw.problem.generateGoalConfigurations (0, 8)
    if cl.problem.solve () != 0:
        raise RuntimeError ("Failed to reach the object")
    pathId = 1+6*i
    #if clw.problem.writeSeqPlayFile (0, pathId, "/home/florent/devel/ros/data/seqplay/reaching") != 0: raise RuntimeError ("Failed to write reaching path in seqplay files")

    # Transfer motion
    cl.obstacle.moveObstacleConfig ("Sphere",
                                    Configuration (trs = (0.62, -0.16, 0.),
                                                   rot = (1, 0, 0,
                                                          0, 1, 0,
                                                          0, 0, 1)))
    closeHand (True, True)
    length = cl.problem.pathLength (0, pathId)
    q = cl.problem.configAtDistance (0, pathId, length)
    cl.problem.resetGoalConfig (0)
    if clw.problem.setTarget (0.62, -0.16, 1.34) != 0:
        raise RuntimeError ("Failed to set target.")
    cl.problem.setInitialConfig(0, q)
    clw.problem.generateGoalConfigurations (0, 8)
    if cl.problem.solve () != 0:
        raise RuntimeError ("Failed to transfer the object")
    
    pathId = 3+6*i
    #if clw.problem.writeSeqPlayFile (0, pathId, "/home/florent/devel/ros/data/seqplay/transfer") != 0: raise RuntimeError ("Failed to write reaching path in seqplay files")

    # Return motion
    openHand (True, True)
    cl.obstacle.moveObstacleConfig ("Sphere",
                                    Configuration (trs = (0.62, -0.16, 1.34),
                                                   rot = (1, 0, 0,
                                                          0, 1, 0,
                                                          0, 0, 1)))
    length = cl.problem.pathLength (0, pathId)
    q = cl.problem.configAtDistance (0, pathId, length)
    cl.problem.resetGoalConfig (0)
    cl.problem.setInitialConfig(0, q)
    cl.problem.addGoalConfig (0, q_init)
    cl.problem.setPathOptimizer (0, "random", 50)
    if cl.problem.solve () != 0:
        raise RuntimeError ("Failed to return to initial configuration")

    pathId = 5+6*i
    #if clw.problem.writeSeqPlayFile (0, pathId, "/home/florent/devel/ros/data/seqplay/return") != 0:raise RuntimeError ("Failed to write reaching path in seqplay files")
    
    cl.obstacle.moveObstacleConfig ("Sphere",
                                    Configuration (trs = (0.62, 0.078, 1.),
                                                   rot = (1, 0, 0,
                                                          0, 1, 0,
                                                          0, 0, 1)))
    node = cl.problem.countNodes (0)
    edge = cl.problem.countEdges (0)
    nodes.append (node)
    edges.append (edge)
    print ("Number of nodes :   {0}".format (node))
    print ("Number of edges :   {0}".format (edge))
    cl.problem.clearRoadmaps ()
    cl.problem.setInitialConfig (0, q_init)
    cl.robot.setCurrentConfig (0, q_init)
