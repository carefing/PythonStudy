"""
Define Clock and show clock time
"""

import time

class Clock(object):

	def __init__(self, **hms):
		if 'hour' in hms and 'minute' in hms and 'second' in hms:
			self._hour = hms['hour']
			self._minute = hms['minute']
			self._second = hms['second']
		else:
			tm = time.localtime(time.time())
			self._hour = tm.tm_hour
			self._minute = tm.tm_min
			self._second = tm.tm_sec

	def run(self):
		self._second += 1
		if self._second == 60:
			self._second = 0
			self._minute += 1
			if self._minute == 60:
				self._minute = 0
				self._hour += 1
				if self._hour == 24:
					self._hour = 0
	
	def show(self):
		return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

if __name__ == "__main__":
	# clock = Clock(hour=10, minute=15, second=22)
	clock = Clock()
	while True:
		print(clock.show())
		time.sleep(1)
		clock.run()