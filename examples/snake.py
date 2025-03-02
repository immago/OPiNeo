#Snake Effect (LEDs light up in a snake-like motion)
import time
from opineo import OPiNeo

def snake_effect(neo, color, delay=0.05, snake_length=3):
    while True:
        for i in range(neo.num_leds + snake_length):
            neo.fill_strip(0, 0, 0)  # Clear the strip
            for j in range(snake_length):
                if i - j >= 0 and i - j < neo.num_leds:
                    neo.set_led_color(i - j, *color)
            neo.update_strip()
            time.sleep(delay)

# Initialize OPiNeo with 10 LEDs
neo = OPiNeo('/dev/spidev1.1', 10, 800)

# Green snake effect
snake_effect(neo, (0, 255, 0))
