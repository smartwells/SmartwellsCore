#!/bin/bash

stty 57600 cs8 -parenb -cstopb -echo icrnl ixon opost onlcr isig icanon iexten echoe echok echoctl echoke -F /dev/ttyS0
