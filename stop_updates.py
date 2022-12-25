# python 3.7.9
# display resolution 1920*1080
# size of text 150%
import sys
import os
import time
import datetime as dt
import argparse
import logging
import pyautogui

# Parser for arguments in script
parser = argparse.ArgumentParser(description=f"Script name")
parser.add_argument("--debug", help="sample: --debug 1")
args = parser.parse_args(sys.argv[1:])
debug = False
if args.debug is not None:
	debug = True

# Create log file
time_now = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
print(time_now)

log_file_name = f"{time_now}_log.txt"
if not os.path.exists(os.path.join(os.getcwd(), "log")):
	os.makedirs(os.path.join(os.getcwd(), "log"))
log_file = os.path.join(os.getcwd(), "log", log_file_name)

print(f"log file name => {log_file_name}")
print(f"log file path => {log_file}")

logger = logging.getLogger()
fhandler = logging.FileHandler(filename=log_file, mode='a')
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

# Create folder for screenshots
if not os.path.exists(os.path.join(os.getcwd(), "screenshots")):
	os.makedirs(os.path.join(os.getcwd(), "screenshots"))

# Create folder for screenshots with current date
current_date = dt.datetime.now().strftime("%Y%m%d")
if not os.path.exists(os.path.join(os.getcwd(), "screenshots", current_date)):
	os.makedirs(os.path.join(os.getcwd(), "screenshots", current_date))


# Get the size of the primary monitor.
screen_width, screen_hight = pyautogui.size()
print(f"screen_width:{screen_width}\nscreen_hight:{screen_hight}")

# Returns two integers, the x and y of the mouse cursor's current position.
current_mouse_x, current_mouse_y = pyautogui.position()
print(f"current_mouse_x:{current_mouse_x}\ncurrent_mouse_y:{current_mouse_y}")


# def open_file_explorer():
# 	this_function_name = sys._getframe().f_code.co_name
# 	logging.info(f"{str(dt.datetime.now())}:Started {this_function_name}")
# 	try:
# 		# keyboard combination windows + D
# 		pyautogui.hotkey('win', 'd')
# 		# Move the mouse to the File Explorer shortcut.
# 		pyautogui.moveTo(705, 1050)
# 		pyautogui.click()
# 	except Exception as err:
# 		logging.error(f"{str(dt.datetime.now())}:ERROR occurred in {this_function_name}:{err}")
# 		print(f"ERROR occurred in {this_function_name}:{err}")


def run_stop_updates_shorcut():
	this_function_name = sys._getframe().f_code.co_name
	logging.info(f"{str(dt.datetime.now())}:Started {this_function_name}")
	try:
		# keyboard combination windows + D
		# pyautogui.hotkey('win', 'd')
		# move mouse cursore to Slack shortcut on descktop
		# pyautogui.moveTo(5, 5)
		# double click on Slack shortcut
		pyautogui.doubleClick(x=5, y=5)
	except Exception as err:
		logging.error(f"{str(dt.datetime.now())}:ERROR occurred in {this_function_name}:{err}")
		print(f"ERROR occurred in {this_function_name}:{err}")

# Open Slack via shortcut
# def open_slack():
# 	this_function_name = sys._getframe().f_code.co_name
# 	logging.info(f"{str(dt.datetime.now())}:Started {this_function_name}")
# 	try:
# 		# keyboard combination windows + D
# 		pyautogui.hotkey('win', 'd')
# 		# move mouse cursore to Slack shortcut on descktop
# 		pyautogui.moveTo(770, 1050)
# 		# double click on Slack shortcut
# 		pyautogui.doubleClick()
# 		time.sleep(180)
# 		pyautogui.press('d')
# 	except Exception as err:
# 		logging.error(f"{str(dt.datetime.now())}:ERROR occurred in {this_function_name}:{err}")
# 		print(f"ERROR occurred in {this_function_name}:{err}")

# Make screenshot of full display or part of display
# def screenshot():
# 	this_function_name = sys._getframe().f_code.co_name
# 	logging.info(f"{str(dt.datetime.now())}:Started {this_function_name}")
# 	try:
# 		screenshot_time = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
# 		print(screenshot_time)
# 		scrn_nm = f"{screenshot_time}.jpg"
# 		scrn_file = os.path.join(os.getcwd(), "screenshots", current_date, scrn_nm)
# Make screenshot of display. region: 0 - start position. number of pixels from left displey border
#                               0 - start position. number of pixels from upper display border
#                               300 - lenght in pixel from left start position
#                               768 - lenght in pixel from upper start position
# 		img = pyautogui.screenshot(scrn_file, region=(0,0, 300, 768))
# 	except Exception as err:
# 		logging.error(f"{str(dt.datetime.now())}:ERROR occurred in {this_function_name}:{err}")
# 		print(f"ERROR occurred in {this_function_name}:{err}")



def main():
	script_start = dt.datetime.now()
	logging.info(f"{str(dt.datetime.now())}:Script started on {script_start}")
	log_off_time = dt.time(23, 15, 0)
	# print(f"log_off_time: {log_off_time}")
	last_scrn_time = script_start
	current_time = script_start.time()
	while True:
		time.sleep(5)
		run_stop_updates_shorcut()
		time.sleep(600)
		logging.info(f"{str(dt.datetime.now())}:Script execution time: {round((dt.datetime.now() - script_start).total_seconds()/3600, 1)} hours")
		print(f"{str(dt.datetime.now())}:Script execution time: {round((dt.datetime.now() - script_start).total_seconds()/3600, 1)} hours")
	script_end = dt.datetime.now()
	logging.info(f"{str(dt.datetime.now())}:Script execution time: {(script_end - script_start).seconds} seconds")
	print(f"Script execution time: {round((script_end - script_start).total_seconds()/60, 1)} minutes")


if __name__ == '__main__':
	main()

