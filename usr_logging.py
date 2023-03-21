import psutil

# Define a function to handle login events
def on_login(proc):
    # Extract the username from the process owner
    username = proc.username()

    # Do something with the extracted data (e.g., print it)
    print(f"User {username} logged in")


def main():
    # Set up a process monitor to watch for login processes
    monitor = psutil.process_iter(attrs=['pid', 'name', 'username'])
    for proc in monitor:
        if proc.name() == 'login':
            on_login(proc)

    # Continuously monitor the running processes for login events
    while True:
        for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
            if proc.name() == 'login':
                on_login(proc)


if __name__ == '__main__':
    main()
