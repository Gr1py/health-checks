#!/usr/bin/env python3

import os
import sys

def check_reboot():
    """Retunr True if the computer"""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print ("Pending Reboot.")
        sys.exit(1)
    if disk_full():
        print ("disk full")
        sys.exit(1)
    print ("Everything ok.They made some changes")
    sys.exit(0)

main()
