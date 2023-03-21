import os
import sys
import socket
import datetime
import time

FILE = os.path.join(os.getcwd(), 'networkinfo.log')


def ping():

    try:
        socket.setdefaulttimeout(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        host = '8.8.8.8'
        port = 53

        server_address = (host, port)
        s.connect(server_address)

    except OSError as error:
        return False
    else:
        s.close()

        return True



def calculate_time(start, stop):
    
    diff = stop-start
    sec = float(str(diff.total_seconds()))

    return str(datetime.timedelta(seconds=seconds)).split('.')[0]


def first_check():

    if ping():
        live = '\nConnection Acquired\n'

        print(live)
        connection_acquired_time = datetime.datetime.now()
        acquiring_message = 'connection acquired at: ' + str(connection_acquired_time).split('.')[0]

        print(acquiring_message)

        with open(FILE, 'a') as file:
            file.write(live)
            file.write(acquiring_message)

        return True
    else:

        not_live = '\nConnection not Acquired\n'
        print(not_live)

        with open(FILE, 'a') as file:
            file.write(not_live)

        return False



def main():

    monitor_start_time = datetime.datetime.now()
    monitoring_date_time = 'Monitoring started at: ' + str(monitor_start_time).split('.')[0]

    if first_check():
        print(monitoring_date_time)
    else:
        while True:
            if not ping():
                time.sleep(1)

            else:
                first_check()
                print(monitoring_date_time)
                break
    with open(FILE, 'a') as file:

        file.write('\n')
        file.write(monitoring_date_time + '\n')

    while True:
        if ping():
            time.sleep(5)

        else:
            down_time = datetime.datetime.now()
            fail_msg = 'disconnected at: ' + str(down_time).split('.')[0]

            print(fail_msg)

            with open(FILE, 'a') as file:
                file.write(fail_msg + '\n')

            while not ping():
                time.sleep(1)
            uptime = datetime.datetime.now()

            uptime_msg = 'connected again: ' + str(uptime).split('.')[0]
            downtime = calculate_time(down_time, up_time)

            un_avail_time = 'connection was unavailable for :' + downtime
            print(uptime_msg)
            print(un_avail_time)

            with open(FILE, 'a') as file:
                file.write(uptime_msg + '\n')
                file.write(un_avail_time + '\n')




if __name__ == '__main__':
    main()
