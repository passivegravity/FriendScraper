import requests
import art
import os

# clear the console screen
os.system('cls')

# generate the header
header_text = "Friend Scraper"
header_art = art.text2art(header_text)
header_art = "\033[32m" + header_art + "\033[0m"
print(header_art)

# get the user token
token = input("\033[35mProvide User Token: \033[0m")

# make the request to get the friend list
headers = {
    "Authorization": token
}

response = requests.get("https://discord.com/api/users/@me/relationships", headers=headers)
friends = response.json()

# write the friend list to a text file
with open("discord_friends.txt", "w", encoding="utf-8") as f:
    f.write("To decode User IDs use this site: https://discord.id/\n")
    for friend in friends:
        username = friend["user"]["username"] + "#" + friend["user"]["discriminator"]
        user_id = friend["user"]["id"]
        f.write(f"{username} <{user_id}>\n")

print("Discord friends saved to discord_friends.txt.")
