#Knight Rider / Cylon Effect (A scanning LED light that moves back and forth)
import time
from opineo import OPiNeo

def knight_rider(neo, color, delay=0.05):
    num_leds = neo.num_leds
    while True:
        # Forward pass
        for i in range(num_leds):
            neo.fill_strip(0, 0, 0)  # Clear the strip
            neo.set_led_color(i, *color)  # Set the current LED to the color
            neo.update_strip()
            time.sleep(delay)
        # Backward pass
        for i in range(num_leds - 1, -1, -1):
            neo.fill_strip(0, 0, 0)  # Clear the strip
            neo.set_led_color(i, *color)  # Set the current LED to the color
            neo.update_strip()
            time.sleep(delay)

# Initialize OPiNeo with 10 LEDs
neo = OPiNeo('/dev/spidev1.1', 10, 800)

# Knight Rider effect with red color
knight_rider(neo, (255, 0, 0))
