import sys
import time
from messanger import message, get_messages

args = sys.argv[1:]
if not args:
	print(f"ERR: [name: str]")

USERNAME = args[0]

while True:
	messages = get_messages()

	for m in messages:
		print(f"{m['USER']} -> {m['MESSAGE']}")

	user = input(f"MESSAGE as {USERNAME}: ")
	message(USERNAME, user)
	time.sleep(0.5)
