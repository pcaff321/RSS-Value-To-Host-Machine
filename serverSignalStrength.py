import socket                                                                                                                                 
                                                                                                                                              
UDP_IP = "192.168.1.185"                                                                                                                      
UDP_PORT = 5005                                                                                                                               
                                                                                                                                              
print("UDP target IP: %s" % UDP_IP)                                                                                                           
print("UDP target port: %s" % UDP_PORT)                                                                                                       
                                                                                                                                              
                                                                                                                                              
sock = socket.socket(socket.AF_INET, # Internet                                                                                               
                     socket.SOCK_DGRAM) # UDP                                                                                                 
                                                                                                                                              
print("RUNNING...\n")                                                                                                                         
print("CTRL + C TO STOP TRANSMITTING")                                                                                                        
                                                                                                                                              
while True:                                                                                                                                   
    f = open("/proc/net/wireless", "r")                                                                                                       
    line = f.readline()                                                                                                                       
    rss = ''                                                                                                                                  
                                                                                                                                              
    while line != '':                                                                                                                         
        splitLine = line.split()                                                                                                              
        if splitLine[0] == "wlan2:":                                                                                                          
            rss = splitLine[3].replace('.', '')                                                                                               
        line = f.readline()                                                                                                                   
                                                                                                                                              
    msg= rss.encode(encoding="UTF-8")                                                                                                         
    sock.sendto(msg, (UDP_IP, UDP_PORT))                                                                                                      
                                            
