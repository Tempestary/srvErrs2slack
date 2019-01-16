Errs2slack

Prerequisites:

You need this great inferface from 
https://github.com/os/slacker
to make things work


`pip install slacker`

The other essential part of this is a running PID to check its logs for exceptions
AND at least RO-level access to files you are going to listen.

Configure the script so it meets your needs and then run on the target machine (supposed to be linux/unix system)

`tail -F <PATH-TO-YOUR-LOG>.log | python3 errsChecker.py`

-F parameter here takes care of any possible log rotation.

The trace will be displayed as an inlined code. 
It's also possible to create a bot user and authorize it with
 your slack account, and then invite it to the specific channel to post in, 
 and upload exceptions as files (it kinda looks better).



