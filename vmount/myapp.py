FILENAME = "server.txt"

try:
    with open(FILENAME, "r") as file:
        servers = file.read().splitlines()
        print("📋 Current Servers:", servers)
except FileNotFoundError:
    print("❌ server.txt not found inside container.")
