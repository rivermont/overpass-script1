#!/bin/bash
#
# Write out current crontab
crontab -l > .crons
# echo new cron into cron file
echo "00 01 * * * ./script.py" >> .crons
# Install new cron file
crontab .crons
rm .crons
