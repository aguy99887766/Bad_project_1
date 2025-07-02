import json
import os

FILENAME = "messages.json"

def generate_messages() -> str:
	with open(FILENAME, "r") as file:
		for row in json.load(file):
			yield row


def get_messages() -> list[dict]:
	try:
		with open(FILENAME, "r") as file:
			messages = json.load(file)
		return messages
	except FileNotFoundError:
		print(f"[!] {FILENAME} not found creating")
		message('SYSTEM', 'WELCOME TO THE CHATROOM')

def load_messages(start: int, end: int) -> list[dict]:
	
	loaded_messages = []	
	
	for current_val, message in enumerate(generate_messages()):

		if current_val < start:
			continue
		
		if current_val >= end:
			return loaded_messages

		loaded_messages.append(message)
	

def message(user: str, content: str) -> None:
	new_message = {"USER": user, "MESSAGE": content}

	if os.path.exists(FILENAME):
		with open(FILENAME, "r") as file:
			try:
				messages = json.load(file)
			except json.JSONDecodeError as e:
				messages = []	
				print(f"[!] {e} - Json could not be decoded")

	else:
		messages = []
			
	messages.append(new_message)
	
	with open("messages.json", "w") as file:
		json.dump(messages, file, indent=2)


if __name__ == '__main__':
	'''
	import random

	names = ["Timmy", "Thomas", "Coraline", "Johnson"]
	responses = ["Cool", "Hello", "Whats up", "Im good", "Lets go to the park", "What are you doing"]
	
	for _ in range(50):
		username = random.choice(names)
		response = random.choice(responses)
		
		message(username, response)
	'''

	messages = load_messages(10, 20)
	print(len(messages))
