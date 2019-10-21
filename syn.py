from socket import *
import threading
serverName = "10.14.140.15"
serverPort = 12005

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while 1:			
	sentence = raw_input("Input lowercase sentence:")
	if(sentence=="exit"):
		break
	clientSocket.send(sentence)
	modifiedSentence = clientSocket.recv(1024)
	print "From Server:", modifiedSentence
	
	modifiedSentence = clientSocket.recv(1024)
	print "From Server:", modifiedSentence
clientSocket.close()


'''
def sender():
	while(1):
		
		global serverName,serverPort
		clientSocket = socket(AF_INET, SOCK_STREAM)
		clientSocket.connect((serverName,serverPort))
		sentence = raw_input("Input lowercase sentence:")
		if(sentence=="exit"):
			break
		clientSocket.send(sentence)
		#modifiedSentence = clientSocket.recv(1024)
		#print "From Server:", modifiedSentence
	clientSocket.close()

def receiver():
 while 1:
  global serverName,serverPort
  serverSocket = socket(AF_INET,SOCK_STREAM)
  serverSocket.bind(("",serverPort))
  serverSocket.listen(1)
  connectionSocket, addr = serverSocket.accept()
  sentence = connectionSocket.recv(1024)
  if(sentence=="exit"):
	break
  print(sentence)  
	#capitalizedSentence = sentence.upper()
  #connectionSocket.send(capitalizedSentence)
 connectionSocket.close()

if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=receiver,args=()) 
    t2 = threading.Thread(target=sender, args=()) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 
'''
