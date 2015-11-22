#TimeCrunch

''' 
As there is only so much time in the day, we have to fit our workouts in somehow.  TimeCrunch looks at the calendar on your phone and suggests workouts, 
big and small, that appear to fit your schedule.  

TimeCrunch is for those trying to develop good fitness habits, rather than more experienced and dedicated individuals who already have established workout 
plans.  The latter folks make time to get fit.  TimeCrunch is for those who perpetually complain about lack of time to work out.  If your calendar is accurate,
then TimeCrunch will find time for you to develop good habits.  
'''

#   create a week of calendar events; do not try to pull from an actual calendar, create one in the program
#   each day will be set up as 1440 minutes, from 12am to 11:59pm 
#   Time blocks for minutes in a day; 7am = minute 420, 8am(480), 9am(540), 10am(600), 11am(660), 12pm(720), 1pm(780), 2pm(840), 3pm(900), 4pm(960), 5pm(1020), 6pm(1080), 
#       7pm(1140), 8pm(1200), 9pm(1260), 10pm(1320)
#   Automatically ignore times between 10pm and 7am
calendar = { 'Monday': [range(480, 600), range(700, 750), range(900, 1200)]
             'Tuesday': [range(490, 610), range(550, 575), range(700, 750)]
             'Wednesday': [range(496, 610), range(550, 585), range(706, 756)]
             'Thursday': [range(444, 610), range(550, 575), range(700, 750)]
             'Friday': [range(490, 600), range(550, 599), range(701, 750)]
             'Saturday': [range(490, 610), range(550, 575), range(700, 750)]
             'Sunday':   [range(490, 610), range(550, 575), range(723, 751)]          

            }
#   check out date/time module

#   create a list of basic workouts, with their duration; sorting depends on the duration of a single set; time will need to be converted
    #   standing leg curls are timed for 10 reps for *both legs*, so half the number for just one leg
workout = {'chair squats': [.30], 'pushups': [.17], 'full squats': [.20], 'crunches': [.14], 'standing leg curl': [.24], 'arm circles': [.12]}
#
