import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
blue = 6
yellow = 13
red= 19
green= 26
now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

##LED Blue
GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, 0) #Off initially
#LED Yellow
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, 0) #Off initially
#LED Red
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0) #Off initially
#LED green
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0) #Off initially
def action(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	print ('Received: %s' % command)
	message = "comandos"
	telegram_bot.sendMessage (chat_id, message)
	message = "all on \n all off \n blue on \n yellow on \n red on \n green on \n blue off \n yellow off \n red off \n green off  "
	telegram_bot.sendMessage (chat_id, message)
	if 'on' in command:
		message = "on"
		if 'blue' in command:
			message = message + "blue "
			GPIO.output(blue, 1)
		if 'yellow' in command:
			message = message + "yellow "
			GPIO.output(yellow, 1)
		if 'red' in command:
			message = message + "red "
			GPIO.output(red, 1)
		if 'green' in command:
			message = message + "green "
			GPIO.output(green, 1)
		if 'all' in command:
			message = message + "all "
			GPIO.output(blue, 1)
			GPIO.output(yellow, 1)
			GPIO.output(red, 1)
			GPIO.output(green, 1)
		message = message + "light(s)"
		telegram_bot.sendMessage (chat_id, message)
	if 'off' in command:
		message = "off "
		if 'blue' in command:
			message = message + "blue "
			GPIO.output(blue, 0)
		if 'yellow' in command:
			message = message + "yellow "
			GPIO.output(yellow, 0)
		if 'red' in command:
			message = message + "red "
			GPIO.output(red, 0)
		if 'green' in command:
			message = message + "green "
			GPIO.output(green, 0)
		if 'all' in command:
			message = message + "all "
			GPIO.output(blue, 0)
			GPIO.output(yellow, 0)
			GPIO.output(red, 0)
			GPIO.output(green, 0)
		message = message + "light(s)"
		telegram_bot.sendMessage (chat_id, message)
telegram_bot = telepot.Bot('1811246047:AAG8DNKb6csehwWXjXjETnsoZadDuQ_E0eA')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')
while 1:
	time.sleep(10)
