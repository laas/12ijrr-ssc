pid=2853
success = parseLineInLog (prefix='INFO:/home/florent/devel/hpp/src/hpp-constrained/src/config-projector.cc:151: Projection succeeded.', pid=pid)
fails = parseLineInLog (prefix='INFO:/home/florent/devel/hpp/src/hpp-constrained/src/config-projector.cc:148: Projection failed', pid=pid)
p = 'INFO:/home/florent/devel/hpp/src/hpp-constrained/src/config-projector.cc:136: '
cumulative = []
cumulative.append (parseLineInLog (prefix = p + '0.1', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.27', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.406', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.5148', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.60184', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.671472', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.727178', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.771742', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.807394', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.835915', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.858732', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.876986', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.891588', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.903271', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.912617', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.920093', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.926075', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.93086', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.934688', pid=pid))
cumulative.append (parseLineInLog (prefix = p + '0.93775', pid=pid))

cumulative.append (0)
iteration = map (lambda x : x[0] - x [1], zip (cumulative, cumulative [1:]))

# Average number of iterations of projection.
sum (map (lambda x: x[0]*x[1], zip (iteration, range (1, len(iteration)+1))))/(sum(iteration)*1.)

# Time computation
pid=8044
times = dict ()
times ['plan'] = parseTimeInBenchmark (prefix = 'BENCHMARK:/home/florent/devel/hpp/stable/build/path/hpp-core/work.florent-laptop/hpp-core-2.5/src/problem.cc:460: planPath: ', pid=pid)
times ['goal'] = parseTimeInBenchmark (prefix = 'BENCHMARK:/home/florent/devel/hpp/src/hpp-constrained-planner/src/planner.cc:383: generateGoalConfig: ', pid=pid)
times ['optimize'] = parseTimeInBenchmark (prefix = 'BENCHMARK:/home/florent/devel/hpp/stable/build/path/hpp-core/work.florent-laptop/hpp-core-2.5/src/problem.cc:503: optimizePath: ', pid=pid)

totalTime = dict ()
for (key, timeList) in times.iteritems ():
    totalTime [key]  = reduce (lambda x, y: x+y, timeList, datetime.timedelta (0))

# Times by problem among 20
planTimes = []
for i in range (0,len(times ['plan']),3):
    planTimes.append (times ['plan'][i] +
                      times ['plan'][i+1] +
                      times ['plan'][i+2])

goalTimes = []
for i in range (0,len(times ['goal']),2):
    goalTimes.append (times ['goal'][i] +
                      times ['goal'][i+1])

optimizeTimes = []
for i in range (0,len(times ['optimize']),3):
    optimizeTimes.append (times ['optimize'][i] +
                          times ['optimize'][i+1] +
                          times ['optimize'][i+2])
