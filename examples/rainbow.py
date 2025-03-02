#Running Rainbow Wave (Rainbow colors move across the strip)
import time
from opineo import OPiNeo

def running_rainbow(neo, delay=0.05):
    colors = [
        (255, 0, 0),   # Red
        (255, 127, 0), # Orange
        (255, 255, 0), # Yellow
        (0, 255, 0),   # Green
        (0, 0, 255),   # Blue
        (75, 0, 130),  # Indigo
        (148, 0, 211)  # Violet
    ]
    
    num_colors = len(colors)
    while True:
        for offset in range(neo.num_leds):
            for i in range(neo.num_leds):
                neo.set_led_color(i, *colors[(i + offset) % num_colors])
            neo.update_strip()
            time.sleep(delay)

# Initialize OPiNeo with 10 LEDs
neo = OPiNeo('/dev/spidev1.1', 10, 800)

# Rainbow wave across the strip
running_rainbow(neo)
