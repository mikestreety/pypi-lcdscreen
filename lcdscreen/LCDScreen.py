#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

class LCDScreen:

	def __init__(self, config_user = {}, GPIO = None):
		config_preset = {
			'pin_rs': 25, # The input of the RS pin
			'pin_e': 24, # The input of the E pin
			'pins_db': [23, 17, 27, 22], # The input of the DB pins
			'backlight': 18, # The input of the Backlight pin
			'dimensions': [20, 4], # How big your screen is [width, height]
			'delay': 3, # The default delay time
			'spacer': ' ' # The default spacer character
		}

		# Take user input and merge with above - overwrite if necessary
		config = config_preset.copy()
		config.update(config_user)

		# If no GPIO, import it
		if not GPIO:
			import RPi.GPIO as GPIO
			GPIO.setwarnings(False)

		# Set up basic properties
		self.config = config
		self.GPIO = GPIO
		self.line_endings = [0x80, 0xC0, 0x94, 0xD4]
		self.lines_passed = 0

		# Initialise the GPIO outputs
		self.GPIO.setmode(GPIO.BCM)
		self.GPIO.setup(self.config['pin_e'], GPIO.OUT)
		self.GPIO.setup(self.config['pin_rs'], GPIO.OUT)
		self.GPIO.setup(self.config['backlight'], GPIO.OUT)

		for pin in self.config['pins_db']:
			self.GPIO.setup(pin, GPIO.OUT)

		self.write_bit(0x33)
		self.write_bit(0x32)
		self.write_bit(0x28)
		self.write_bit(0x0C)
		self.write_bit(0x06)
		self.write_bit(0x01)
		self.reset_lines()

	# Controls the backlight
	def backlight(self, state):
		if state == 'on':
			light = True
		elif state == 'off':
			light = False
		else:
			raise SyntaxError('State can either be on or off')

		self.GPIO.output(self.config['backlight'], light)

	# Writes a Message
	# @string: the message you want to write
	# @alignment: whether the string is left, right or center aligned
	# @clear: whether the screen should clear if message (dimensions =" height" + 1) gets passed in
	#	e.g. if a 4 line screen and you pass in 5 lines, should the screen clear? Default is yes
	#	note: needed for the push up as you don't want it to clear in that case
	def message(self, string, alignment = 'left', spacer = False, clear = True):

		if spacer == False:
			spacer = self.config['spacer']
		spacer = spacer[0] # Make sure spacer is only 1 character

		if alignment == 'left':
			string = string.ljust(self.config['dimensions'][0], spacer)
		elif alignment == 'right':
			string = string.rjust(self.config['dimensions'][0], spacer)
		elif (alignment == 'center') or (alignment == 'centre'):
			string = string.center(self.config['dimensions'][0], spacer)
		else:
			raise SyntaxError('String alignment error. Can either be left, right or center')

		if self.lines_passed > (self.config['dimensions'][1] - 1):
			self.lines_passed = 0
			if clear == True:
				self.clear()

		self.write_bit(self.line_endings[self.lines_passed])
		self.lines[self.lines_passed] = string
		self.lines_passed = self.lines_passed + 1

		for i in range(len(string)):
			self.write_bit(ord(string[i]), True)

	# Adds string to the bottom or top and pushes the rest up or down
	# @direction: can be up or down
	# @string: the message you wish to add
	# @alignment: whether the string is left, right or centered
	# @spacer: what to fill the rest of the space with
	def push(self, direction, string, alignment = 'left', spacer = False):
		if spacer == False:
			spacer = self.config['spacer']

		if direction == 'up':
			del self.lines[0]
			self.lines.append(string)
		elif direction == 'down':
			self.lines.insert(0, string)
			del self.lines[self.config['dimensions'][1]]
		else:
			raise SyntaxError('Direction can be either up or down')

		self.lines_passed = 0
		for line in self.lines:
			self.message(line, 'left', spacer, False)

	# Shortcut for push('up')
	def push_up(self, string, alignment = 'left', spacer = False):
		if spacer == False:
			spacer = self.config['spacer']
		self.push('up', string, alignment, spacer)

	# Shortcut for push('down')
	def push_down(self, string, alignment = 'left', spacer = False):
		if spacer == False:
			spacer = self.config['spacer']
		self.push('down', string, alignment, spacer)

	# Clears the screen
	def clear(self):
		self.write_bit(0x01)  # command to clear display
		self.lines_passed = 0
		self.reset_lines()
		self.delay_microseconds(3000)

	# Clears the screen and then delays
	# @seconds: Seconds to delay it
	def clear_delay(self, seconds = False):
		if seconds == False:
			seconds = self.config['delay']

		self.clear()
		self.delay(seconds)

	# Delay and then clear (useful for showing a message and clearing)
	# @seconds: Seconds to delay it
	def delay_clear(self, seconds = False):
		if seconds == False:
			seconds = self.config['delay']

		self.delay(seconds)
		self.clear()

	##
	# String Modifiers
	##

	# Spaces out two strings with a character in between
	# 	e.g. Left-----------Right
	def spaced(self, left, right, spacer = ' '):
		spacing = self.config['dimensions'][0] - (len(left) + len(right))
		spacer = spacer * spacing
		return left + spacer + right

	##
	# Internal Functions
	##

	# Write bit to screen
	def write_bit(self, bits, char_mode = False):
		self.delay_microseconds(1000)  # 1000 microsecond sleep
		bits = bin(bits)[2:].zfill(8)
		self.GPIO.output(self.config['pin_rs'], char_mode)

		for pin in self.config['pins_db']:
			self.GPIO.output(pin, False)

		for i in range(4):
			if bits[i] == "1":
				self.GPIO.output(self.config['pins_db'][::-1][i], True)
		self.pulse_enable()

		for pin in self.config['pins_db']:
			self.GPIO.output(pin, False)

		for i in range(4, 8):
			if bits[i] == "1":
				self.GPIO.output(self.config['pins_db'][::-1][i-4], True)
		self.pulse_enable()

	# Delay (saves loading "time" in application)
	# @seconds: Seconds to delay
	def delay(self, seconds = False):
		if seconds == False:
			seconds = self.config['delay']
		time.sleep(seconds)

	# Delay (saves loading "time" in application)
	# @microseconds: Microseconds to delay
	def delay_microseconds(self, microseconds):
		seconds = microseconds / float(1000000)
		time.sleep(seconds)

	def pulse_enable(self):
		self.GPIO.output(self.config['pin_e'], False)
		self.delay_microseconds(1)       # 1 microsecond pause - enable pulse must be > 450ns
		self.GPIO.output(self.config['pin_e'], True)
		self.delay_microseconds(1)       # 1 microsecond pause - enable pulse must be > 450ns
		self.GPIO.output(self.config['pin_e'], False)
		self.delay_microseconds(1)

	# Reset the line count (for clearing after X lines)
	def reset_lines(self):
		self.lines = []
		for i in range(self.config['dimensions'][1]):
			self.lines.append(' ')
