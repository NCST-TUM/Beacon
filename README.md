# Beacon
This repository contains information and some tools that can help you receive and decode Beacon messages from TUMnanoSAT nanosatellite.

The tools presented here are far from being perfect and for sure can be improved to make them more stable and reliable.

# Beacon Parsing
To extract the useful information from a message received and decoded you can use the telemetry.py script. 
You simply start the script and give it the message in HEX. It expects it in HEX because this is the format SatNOGS prints the data and it was adapted for it to be easy to use.

Keep in mind that the script was brutally extracted from our main communication platform and was adapted to work as a standalone unit, which is why it is very ugly, unoptimized and surely not very pythonic. Don't judge me for that. :) 
