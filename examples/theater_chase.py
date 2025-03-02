#Theater Chase Effect (Classic moving LED chase effect)
import time
from opineo import OPiNeo

def theater_chase(neo, color, delay=0.1):
    while True:
        for offset in range(3):
            for i in range(neo.num_leds):
                if (i % 3) == offset:
                    neo.set_led_color(i, *color)
                else:
                    neo.set_led_color(i, 0, 0, 0)  # Turn off other LEDs
            neo.update_strip()
            time.sleep(delay)

# Initialize OPiNeo with 10 LEDs
neo = OPiNeo('/dev/spidev1.1', 10, 800)

# Blue theater chase
theater_chase(neo, (0, 0, 255))
