import re
from collections import defaultdict

# Define a regular expression to match login events in the log file
login_regex = re.compile(r"(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*sshd.*Accepted.*(\d+\.\d+\.\d+\.\d+)\s+([a-zA-Z0-9_-]+)")

# Define a dictionary to store the login events
login_events = defaultdict(list)

# Open the auth.log file and read each line
with open('/var/log/auth.log', 'r') as log_file:
    for line in log_file:
        # Check if the line matches the login regex
        match = login_regex.match(line)
        if match:
            # Extract the login event data from the regex match
            timestamp = match.group(1)
            ip_address = match.group(2)
            username = match.group(3)

            # Add the login event to the login events dictionary
            login_events[username].append((timestamp, ip_address))

# Generate a report of the login events
print("Login Events Report")
print("--------------------")
for username, events in login_events.items():
    print(f"Username: {username}")
    print("Login events:")
    for event in events:
        print(f"  Timestamp: {event[0]}, IP Address: {event[1]}")
    print()

