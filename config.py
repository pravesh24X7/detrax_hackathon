import subprocess as sb

def main():

    print('[+] Listing System Active Connections...')

    sb.run('python3 netscan.py', shell=True)
    print('[+] Listening over Network...')
    
    sb.run('python3 net_monitoring.py', shell=True)
    
    print('[+] Monitoring User Logging Activity...')
    sb.run('python3 user_logging.py', shell=True)
    sb.run('python3 usr_logging.py', shell=True)

    print('[+] Card Detection failed...\ncreditcard.csv not found')
    print('[+] Monitoring Transaction failed\ntransaction.log not found')


if __name__ == '__main__':
    main()

