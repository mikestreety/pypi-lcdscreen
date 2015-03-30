#!/usr/bin/python
# -*- coding: utf-8 -*-

from LCDScreen import LCDScreen

# Initialise the
lcd = LCDScreen({
	'pin_rs': 25,
	'pin_e': 24,
	'pins_db': [23, 17, 27, 22],
	'backlight': 18,
	'dimensions': [20, 4]
})

lcd.backlight('on')

lcd.message(' LCD Screen ', 'center', '-')
lcd.message('Welcome to your')
lcd.message('screen. If you see')
lcd.message('this - it works!')
lcd.message('see?')

lcd.delay()
lcd.push('up', ' ')
lcd.push_up('You can push up')

lcd.delay()
lcd.push('down', ' ')
lcd.push_down('Or push down')

lcd.delay_clear()
lcd.message('You can', 'center')
lcd.message('clear the screen', 'center')

lcd.delay_clear()
lcd.message('And add')
lcd.message(lcd.spaced('Spaced', 'out'))
lcd.message('Messages')

lcd.delay_clear()
lcd.message('You can also', 'right')
lcd.message('right align text', 'right')
lcd.message('or center it!', 'center')

lcd.delay_clear()
lcd.message('And add', 'left', '-')
lcd.message('Filling symbols', 'center', '*')
lcd.message('around your', 'center', '^')
lcd.message('text', 'right', '%')

lcd.delay()
lcd.message('If you don\'t clear')
lcd.message('the screen, it')
lcd.message('clears and resets')
lcd.message('back to the top.')

lcd.delay(2)
lcd.message('...like this')

lcd.delay_clear()
lcd.message('Enjoy!', 'center')

lcd.delay(5)
lcd.backlight('off')
lcd.clear()
