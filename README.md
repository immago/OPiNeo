# OPiNeo

## ⚠️ Notice

This is a fork of of [Pi5Neo](https://github.com/vanshksingh/Pi5Neo) library, adapted to work with the **Orange Pi Zero 3** and similar boards.
The main author of the library is Vansh Kumar Singh. All thanks to him.

---
### Simplifying NeoPixel LED Control on Orange Pi Zero 3 via SPI (PH7 MOSI pin)

OPiNeo is a Python library designed to make controlling **NeoPixel LED strips** super easy and efficient on the **Orange Pi Zero 3** (or equivalent boards). Whether you're creating dazzling light shows, informative displays, or ambient lighting, OPiNeo simplifies the process using the Raspberry Pi’s **SPI interface** for high-performance communication.

## 🌟 Key Features

- **Easy NeoPixel Control**: Send commands to any NeoPixel LED strip connected to the Orange Pi Zero 3’s SPI interface.
- **Smooth Transitions**: Enjoy vibrant color transitions with rainbow effects, loading bars, blinking patterns, and more.
- **Optimized for Performance**: Tailored for the Orange Pi Zero 3, ensuring fast and reliable communication with NeoPixel strips.
- **Minimalistic API**: A simple API lets you focus on creativity without worrying about low-level hardware details.
- **Flexible Configurations**: Control various effects and animations by easily setting colors, durations, and brightness levels.

## 🚀 Installation

You can install OPiNeo via `pip`:

```bash
pip3 install git+https://github.com/immago/OPiNeo.git@main
```

### Requirements
- **Python 3.6+**
- **spidev** (automatically installed with OPiNeo)
- **gcc-aarch64-linux-gnu, python3-dev**

### Hardware
- **Orange Pi Zero 3** (or equivalent with SPI interface)
- **NeoPixel LED Strip** (WS281x family)

## 📚 Usage

OPiNeo makes it straightforward to set up and control your NeoPixel strip. Here's a simple example:

First: Enable SPI for the board:

```sudo nano /boot/armbianEnv.txt```
```
# Add or edit following
overlays=spi-spidev
param_spidev_spi_bus=1
param_spidev_spi_cs=1
```

Then:

```python
from opineo import OPiNeo

# Initialize the OPiNeo class with 10 LEDs and an SPI speed of 800kHz
neo = OPiNeo('/dev/spidev1.1', 10, 800)

# Fill the strip with a red color
neo.fill_strip(255, 0, 0)
neo.update_strip()  # Commit changes to the LEDs

# Set the 5th LED to blue
neo.set_led_color(4, 0, 0, 255)
neo.update_strip()
```

## 🌈 Examples

You can find more advanced examples in the [examples](examples) directory. Here’s a quick showcase of some cool effects you can create with OPiNeo:

### Example 1: Rainbow Cycle
```python
from opineo import OPiNeo
import time

def rainbow_cycle(neo, delay=0.1):
    colors = [
        (255, 0, 0),  # Red
        (255, 127, 0),  # Orange
        (255, 255, 0),  # Yellow
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
        (75, 0, 130),  # Indigo
        (148, 0, 211)  # Violet
    ]
    for color in colors:
        neo.fill_strip(*color)
        neo.update_strip()
        time.sleep(delay)

neo = OPiNeo('/dev/spidev1.1', 10, 800)
rainbow_cycle(neo)
```

### Example 2: Loading Bar Effect
```python
from opineo import OPiNeo
import time

def loading_bar(neo):
    for i in range(neo.num_leds):
        neo.set_led_color(i, 0, 255, 0)  # Green loading bar
        neo.update_strip()
        time.sleep(0.2)
    neo.clear_strip()
    neo.update_strip()

neo = OPiNeo('/dev/spidev1.1', 10, 800)
loading_bar(neo)
```


## ⚙️ Configuration

You can configure OPiNeo by passing in different parameters for the number of LEDs, SPI speed, and more:

```python
OPiNeo('/dev/spidev1.1', num_leds=20, spi_speed_khz=1000)
```

- **`/dev/spidev1.1`**: SPI device path
- **`num_leds`**: Number of LEDs in the NeoPixel strip
- **`spi_speed_khz`**: SPI speed in kHz (default 800)


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



### 🔗 Useful Links
- [Original repo Pi5Neo](https://github.com/vanshksingh/Pi5Neo)

