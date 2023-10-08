# Import the pywhatkit library
import pywhatkit as kit

# Phone numbers to send messages to
phone_numbers = [
    '+91{PhoneNumbers}'
] # Add the numbers you want to message

# Message to be sent
message_text = 'You have been selected to the chess club join this group: https://chat.whatsapp.com/GLlrwGymNou77OCro7b9HZ'

# Loop through the list of phone numbers and send the message
for phone_number in phone_numbers:
    kit.sendwhatmsg_instantly(phone_number, message_text, 10, True, 3)
    print(f"Message sent to {phone_number}")
