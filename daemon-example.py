#!/usr/bin/env python

import os, sys, time
from daemon import Daemon

class MyDaemon(Daemon):
    def run(self):
		while True:
			self.listen()
            
    def listen(self):
        files   = os.listdir('/Users/slmullin/Development/paemon/sample')
        entries = open("/Users/slmullin/Development/paemon/files", "r")
        lines   = [line.rstrip() for line in entries]
        for file in files:
            if file not in lines:
                f = open('/Users/slmullin/Development/paemon/files', 'a')
                f.write(file + '\n')
                f.close()
        time.sleep(1)

if __name__ == "__main__":
	daemon = MyDaemon('/tmp/daemon-example.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)