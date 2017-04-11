# SWCheckin
Quick and dirty script for automatically checking into Southwest flights. Once you fill-in your information and schedule the task, you'll be checked-in as soon as possible and have your boarding passes automatically emailed to you. 

# Usage 

Make sure you have Python 3.5 or greater installed on your machine.

Before you run the script, make sure you have Firefox or have changed the webdriver to the browser of your choice.

Additionally, before running do:

    Pip install selenium 


Next, open the script in the text editor of your choice and change #confirmation_number, #firstname, #lastname, #emailaddress to your information. 

Finally, schedule the script to run 24 hours ahead of your flight. On Linux, use cron. On Windows, use task scheduler. On OS X, I reccomend LaunchControl.



