def show_messages(text):
	while sending_messages:
		copy=sending_messages.pop()
		sent.append(copy)

def sent_messages(sent):
	for a in sent:
		msg=f"Hello , {a.title()}"
		print(msg)

sending_messages=['haley','bailey','snow']
sent=[]
#show_messages(sending_messages)
sent_messages(sent)