import time

# define the filename of the transaction log
LOG_FILENAME = 'transactions.log'  # replace with the name of the transaction log file

# initialize variables for monitoring
last_position = 0

# continuously monitor the transaction log
while True:
    # open the log file in read mode and seek to the last position
    with open(LOG_FILENAME, 'r') as log_file:
        log_file.seek(last_position)
        
        # read all new lines in the log file
        new_lines = log_file.readlines()
        if new_lines:
            # process each new line in the log file
            for line in new_lines:
                transaction = line.strip()
                # perform actions based on the transaction (e.g., update a database)
                print(f"New transaction: {transaction}")
                
            # update the last position of the log file
            last_position = log_file.tell()
            
    # wait for a few seconds before checking for new transactions
    time.sleep(5)

