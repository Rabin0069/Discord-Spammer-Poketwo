from webserver import keep_alive
import requests

channelID = 1068823620740194315
headers = {
    "authorization":
    "MTE2MTI0NjkzNDM1NTQyMzMwMg.GT63DO.aV9CXGfZ9nw6O06Sb7Sru-RPHArbNULtz_7KII"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
