# monitor internet speed
Make sure you're getting what you pay your ISP for, not just when your internet seems slow, but always. Here is a Python script and instructions to periodically monitor your internet speed.

Requires [speedtest-cli](https://github.com/sivel/speedtest-cli), pandas, matplotlib and seaborn.

To run yourself, you must change the following:
 - Change first line of "runspeedtest.py" to point to your python installation (locate from terminal with "which python" or "which python3").  This tells the Cron daemon how to run the script, or something.
 - Change the server number to the best server in your area (in python, run `import speedtest; print(speedtest.Speedtest().get_best_server()['id'])`; the result may vary with time).
 - Change paths to data and plot files (but give the full path!).
 
To run the script periodically on a Unix machine, do the following:
 - Make the python script executable by typing "chmod +x runspeedtest.py" in the terminal.
 - Add a line to your crontab file that will run the script by typing "crontab -e" in the terminal.  I check the speed every 20 minutes (on the hour and 20 and 40 minutes after) with the line `0,20,40 * * * * /Users/keatonb/runspeedtest.py >> ~/cron.log 2>&1`.  You can change the details of when to run the script by editing the first five space-separated items in this line (numbers and astrices here).  Use the [crontab guru](https://crontab.guru/) for help!  Don't forget to edit the path to point to runspeedtest.py.
 
If your internet speed looks this bad, do something about it!
![Example plot](https://github.com/keatonb/monitorinternetspeed/blob/master/speed.png)
