batlog
======

Forked from the original repo by @jradavenport

Laptop Battery Logs

This repo is an ongoing study of the battery health of my laptop (for @willettk, a 2010 MacBook Pro). Logs are saved every 1 min that I am using the computer, starting on 29 Oct 2013.

The data file is a litle ugly, but nothing a simple parser can't fix. Should add such a Python parser to the repo. 

To prevent emails every minute on the minute, download the following shell script, named cronic, from http://habilis.net/cronic/

Install it in your /usr/bin/ directory and set commands appropriately

    chmod 755 cronic

To run the cron script, set up the crontab:

    $ crontab -e

and enter this:

    * * * * * cronic /Users/willettk/batlog/battest.sh

This will append data on the date + battery life data every minute on the minute to a file named:

    /Users/willettk/batlog/batlog.dat
