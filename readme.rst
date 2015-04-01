LCD Screen Python Class
=======================

This class makes it easy to write messages to your LCD screen via your Raspberry Pi.

For a working example of the class, see example.py_.

.. _example.py: https://github.com/mikestreety/pypi-lcdscreen/blob/master/example.py

Installation
------------
Install from pip

::

	pip install lcdscreen

From there you can use it as you wish!

::

	from lcdscreen import LCDScreen

Next, initialise the class, passing in the parameters as required:

::

	lcd = LCDScreen({
		'pin_rs': 25,
		'pin_e': 24,
		'pins_db': [23, 17, 27, 22],
		'backlight': 18,
		'dimensions': [20, 4]
	})

The defaults are below. If you don't wish to change anything then you can initilise without passing anything in:

::

	config_preset = {
		'pin_rs': 25, # The input of the RS pin
		'pin_e': 24, # The input of the E pin
		'pins_db': [23, 17, 27, 22], # The input of the DB pins
		'backlight': 18, # The input of the Backlight pin
		'dimensions': [20, 4], # How big your screen is [width, height]
		'delay': 3, # The default delay time
		'spacer': ' ' # The default spacer character
	}

Once initialised, it's quite easy to operate. The class is well documented and the exmaple file shows how to use it

Usage
------

**Backlight**

Turn the backlight on:

::

	lcd.backlight('on')

And turn it off:

::

	lcd.backlight('off')

**Message**

::

	lcd.message('Your message')

**Delay**

::

	lcd.delay() # Delay by default delay time (set in config)
	lcd.delay(5) # Delay by 5 seconds
	lcd.delay_clear() # Wait default delay time then clear the screen
