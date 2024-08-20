class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


info = input()
email_objects = []

while info != "Stop":
    sender, receiver, content = info.split()
    email = Email(sender, receiver, content)
    email_objects.append(email)

    info = input()

indices = [int(x) for x in input().split(', ')]

for index, email in enumerate(email_objects):
    if index in email_objects:
        email_objects[index].send()

    print(f"{email.sender} says to {email.receiver}: {email.content}. Sent: {email.is_sent}")
