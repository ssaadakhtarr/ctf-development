#!/bin/sh
exec socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 jail.py,pty,stderr,setsid,sigint,sane"
