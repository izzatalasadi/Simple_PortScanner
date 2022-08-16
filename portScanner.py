import sys
import os
from socket import error, gaierror, setdefaulttimeout, socket, AF_INET, SOCK_STREAM


# Define our target
if len(sys.argv) == 2:
    target = sys.argv[1]
else:
    print("Error: Invalid amount of target")
    print("python3 portScanner.py <Start IP address,ex: 192.168.1.1>")

try:
    # common used port
    common_port = [1, 5, 7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23, 25, 37, 39, 42, 43, 49, 50, 53, 63, 67, 68, 69, 70, 71, 72, 73, 73, 79, 80, 88, 95, 101, 102, 105, 107, 109, 110, 111, 113, 115, 117, 119, 123, 137, 138, 139, 143, 161, 162, 163, 164, 174, 177, 178, 179, 191, 194, 199, 201, 202, 204, 206, 209, 210, 213, 220, 245, 347, 363, 369, 370, 372, 389, 427, 434, 435, 443, 444, 445, 464, 468, 487, 488, 496, 500, 535, 538, 546, 547, 554, 563, 565, 587, 610, 611, 612, 631, 636, 674, 694, 749, 750, 751, 752, 754, 760,
                   765, 767, 873, 992, 993, 994, 995, 1080, 1109, 1236, 1300, 1433, 1434, 1494, 1512, 1524, 1525, 1645, 1646, 1649, 1701, 1718, 1719, 1720, 1758, 1759, 1789, 1812, 1813, 1911, 1985, 1986, 1997, 2049, 2053, 2102, 2103, 2104, 2105, 2401, 2430, 2430, 2431, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2809, 3130, 3306, 3346, 4011, 4321, 4444, 5002, 5308, 5999, 6000, 7000, 7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008, 7009, 9876, 10080, 11371, 11720, 13720, 13721, 13722, 13724, 13782, 13783, 22273, 26000, 26208, 33434]

    target_start_range = target.split(".")
    start = int(target_start_range[-1])
    ips = range(start, 254)

    for ip in ips:
        host = target[:-1]+str(ip)
        # check if the IP address is up
        HOST_UP = True if os.system(
            "ping -c 3 -W " + str(500) + " " + host + " > /dev/null 2>&1") == 0 else False

        if HOST_UP:
            # Banner
            txt = "{} is up\nScanning common_port on host: {}".format(
                host, host)
            print("{}\n{}".format("_"*len(txt), txt))

            for port in common_port:

                # init socket
                s = socket(AF_INET, SOCK_STREAM)

                # its mean that if the port is not connectable wait 0.1 sec and move on
                setdefaulttimeout(0.1)

                result = s.connect_ex((host, port))
                if result == 0:
                    print("{} is open".format(port))
                s.close()  # close the connection
            print("_"*len(txt))

        #print("Done scanning ports for {}".format(host))
except KeyboardInterrupt:
    print("\n CTL-C pressed .. Exiting the program")
    sys.exit()
except gaierror:  # when the host name cant be resolved
    print("IP address can't be resolved")
    sys.exit()
except error:  # if we cant connect to ip address that we specified
    print(" Coultdnt connect to the server")
    sys.exit()
