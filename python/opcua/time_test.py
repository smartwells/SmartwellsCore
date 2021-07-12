import sched, time

s = sched.scheduler(time.time, time.sleep)

def print_time():
    print ("From print_time", time.time())
#    time.sleep(.5)

def print_some_times():
#    print ( time.time() )
    for i in range( 10 ):
        s.enter(i, 1, print_time, () )
    s.run()
#    print ( time.time() )

print_some_times()
