import numpy as np
import os
import subprocess
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

plt.ion()

def parse_batlog():

    batlog_dir = '/Users/willettk/batlog'
    batlog_file = '%s/batlog.dat' % batlog_dir

    os.system('grep "^[A-Z]" %s > dates.txt' % batlog_file)
    os.system('grep "CurrentCapacity" %s > cc.txt' % batlog_file)
    os.system('grep "MaxCapacity" %s > mc.txt' % batlog_file)

    f = open('%s/dates.txt' % batlog_dir)
    date_lines = f.readlines()
    f.close()

    f = open('%s/cc.txt' % batlog_dir)
    cc_lines = f.readlines()
    f.close()

    f = open('%s/mc.txt' % batlog_dir)
    mc_lines = f.readlines()
    f.close()

    dt = [datetime.strptime(d.rstrip(),'%a %b %d %X %Z %Y') for d in date_lines]
    cc = [c.split('= ')[-1][:-1] for c in cc_lines]
    mc = [m.split('= ')[-1][:-1] for m in mc_lines]

    return dt,cc,mc

def plot_capacity_time(dt,cc,mc):

    design_capacity = float(subprocess.check_output("ioreg -l | grep 'DesignCapacity' | awk '{print $5}'", shell=True).rsplit()[0])
    dc = design_capacity

    max_percentage = [float(m)/float(dc) for m in mc]
    current_percentage = [float(c)/float(dc) for c in cc]

    fig,ax = plt.subplots(num=4)

    years    = mdates.YearLocator()   # every year
    days   = mdates.HourLocator(interval=12)  # every day
    fullFmt = mdates.DateFormatter('%Y-%b-%d %H:%M')

    #ax.plot_date(dt,cc,'.',color='blue')
    #ax.plot_date(dt,mc,'.',color='red')
    ax.plot_date(dt,current_percentage,'.',color='blue')
    ax.plot_date(dt,max_percentage,'.',color='red')

    ax.autoscale_view()
    #ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(fullFmt)
    fig.autofmt_xdate()

    plt.legend(('CurrentCapacity','MaxCapacity'), 'best', shadow=True, fancybox=True, numpoints=1)
    plt.show()

    return None

'''
def plot_folded_day():

def plot_day_vs_time():
'''
