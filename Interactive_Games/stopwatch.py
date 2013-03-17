# NOTE: In order to actually run the code, you will need to go to http://www.codeskulptor.org/#user4-4sIsXxd339LDmzG.py

# template for "Stopwatch: The Game"

import simplegui

# define global variables
tenth_seconds = 0 
seconds = 0 
minutes = 0 
scores = 0
total_stops = 0
timer_run = False

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(mins, secs, tensecs):
    global tenth_seconds, seconds, minutes
    seconds_f = str(seconds)
    if seconds <= 9:
        seconds_f = "0" + str(seconds)
    format_time = str(minutes) + ":" + seconds_f + "." + str(tenth_seconds)
    return format_time

# define event handlers for buttons; "Start", "Stop", "Reset"
def draw(canvas):
    global tenth_seconds, seconds, minutes
    canvas.draw_text(format(minutes, seconds, tenth_seconds), [120,260], 70, "White")
    canvas.draw_text((str(scores) + "/" + str(total_stops)), [40,70], 45, "Red")
    
def start():
    '''	Start button '''
    global timer_run
    timer.start()
    timer_run = True
    
def stop():
    ''' Stop button '''
    global timer_run, tenth_seconds, seconds, minutes, scores, total_stops
    timer.stop()
    if timer_run:
        total_stops += 1
        if tenth_seconds == 0:
            scores += 1   
    timer_run = False
     
def reset():
    ''' Reset button '''
    global timer_run, tenth_seconds, seconds, minutes, scores, total_stops
    timer.stop()
    timer_run = False
    tenth_seconds, seconds, minutes, scores, total_stops = 0, 0, 0, 0, 0

# define event handler for timer with 0.1 sec interval
def tick():
    global tenth_seconds, seconds, minutes
    if tenth_seconds < 9:
        tenth_seconds += 1
    elif tenth_seconds == 9:
        if seconds < 59:
            seconds += 1	
            tenth_seconds = 0
        elif seconds == 59:
            minutes += 1
            seconds = 0
            tenth_seconds = 0
       
# create frame
frame = simplegui.create_frame("Stopwatch", 500, 500)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
start_button = frame.add_button("Start", start, 150)
stop_button = frame.add_button("Stop", stop, 150)
reset_button = frame.add_button("Reset", reset, 150)

# start timer and frame
frame.start()

