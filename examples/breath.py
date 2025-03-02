#Breathing Effect for a Single LED (LED slowly fades in and out)
import time
from opineo import OPiNeo

def breathing_led(neo, led_index, color, steps=50, delay=0.05):
    for i in range(steps):
        intensity = int(255 * (i / steps))  # Gradually increase intensity
        neo.set_led_color(led_index, *(intensity if c > 0 else 0 for c in color))  # Adjust brightness
        neo.update_strip()
        time.sleep(delay)
    for i in range(steps, 0, -1):
        intensity = int(255 * (i / steps))  # Gradually decrease intensity
        neo.set_led_color(led_index, *(intensity if c > 0 else 0 for c in color))
        neo.update_strip()
        time.sleep(delay)

# Initialize OPiNeo with 10 LEDs
neo = OPiNeo('/dev/spidev1.1', 10, 800)

# Breathing effect on 1st LED with red color
breathing_led(neo, 0, (255, 0, 0))
