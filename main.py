import socket
import time
import csv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    msgFromClient = "255"

    bytesToSend = str.encode(msgFromClient)

    serverAddressPort = ("192.168.23.120", 20000)

    bufferSize = 1024

    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    t = []
    roll = []
    pitch = []
    yaw = []

    # Send to server using created UDP socket
    print("Click to send message to server")
    input()

    absolute_time = time.time()
    cnt = 500

    for i in range(0, cnt):
        print("Odczytuje z robura: {}".format(i))
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "Message from robur:\n {}".format(msgFromServer[0].decode())
        print(msg)

        # Data format: 255;255;roll;pitch;yaw
        data = msgFromServer[0].decode().split(";")
        t.append(time.time() - absolute_time)
        roll.append(float(data[2]))
        pitch.append(float(data[3]))
        yaw.append(float(data[4]))

        time.sleep(0.05)

    # Save to CSV
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['t', 'roll', 'pitch', 'yaw'])
        for i in range(0, cnt):
            writer.writerow([t[i], roll[i], pitch[i], yaw[i]])