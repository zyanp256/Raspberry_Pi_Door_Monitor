import time



cooldowns = {}
#cooldown function, checks if prints/outputs can run based on if available_time has been reached
def can_run(current_function, cooldown_duration):
    now = time.time()
    #the time on a clock (00:00:00) when the funciton can run again
    available_time = cooldowns.get(current_function, 0)

    if now >= available_time:
        cooldowns[current_function] = now + cooldown_duration
        
        return True
    else: 
        return False