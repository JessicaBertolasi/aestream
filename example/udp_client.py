import datetime
import time

import torch # Torch is needed to import c10 (Core TENsor) context
from aestream import UDPInput

# Start a stream, receiving tensors of shape (640, 480)
# By default, we listen on port 3333 and send the tensors to the CPU
# The variable stream can now be `.read()` whenever a tensor is desired
with UDPInput((640, 480), "cpu", 4301) as stream:

    # In this case, we read() every 500ms
    interval = 0.5 
    t_0 = time.time()

    # Loop forever
    while True:
        # When 500 ms passed...
        if t_0 + interval <= time.time():

            # Grab a tensor of the events arriving during the past 500ms
            frame = stream.read()

            # Reset the time so we're again counting to 500ms
            t_0 = time.time()
            
            # Sum the incoming events and print along the timestamp
            time_string = datetime.datetime.fromtimestamp(t_0).time()
            print(f"Frame at {time_string} with {frame.sum()} events")