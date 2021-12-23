def show_messages(messages):
	for message in messages:
		print(message)

def send_messages(messages, sendmessages):
	while messages:
		current_message = messages.pop()
		print(current_message)
		sendmessages.append(current_message)

messages = ['Hello, welcome to python world!', 'I think you will fall in love with this language.', 'Welcome on, greener!']
sendmessages = []
send_messages(messages,sendmessages)

print("\nmessages:")
show_messages(messages)

print("\nsendmessages:")
show_messages(sendmessages)