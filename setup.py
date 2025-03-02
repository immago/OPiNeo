# setup.py
from setuptools import setup, find_packages

setup(
    name='OPiNeo',
    version='1.0.0',
    description='A NeoPixel LED control library for Orange Pi Zero 3 using SPI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Vansh Kumar Singh, Dmitry Byankin',
    author_email='vsvsasas@gmail.com',
    url='https://github.com/immago/OPiNeo', 
    packages=find_packages(),
    install_requires=[
        'spidev',  # Only include spidev as a requirement
    ],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',  # Specifying Linux for Raspberry Pi
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='orangepizero3, neopixel, spi, led-strip, hardware',  # Keywords to improve searchability
    platforms=['Orange Pi Zero 3', 'Equivalent Orange Pi Zero boards'],
    python_requires='>=3.6',
)
