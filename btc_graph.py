# -*- coding: utf-8 -*-
import poloniex
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt


def main():
    date, data = getDataPoloniex()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(date, data)
    ax.set_title("BTC Price")
    ax.set_xlabel("Day")
    ax.set_ylabel("BTC Price[$]")
    plt.grid(fig)
#    plt.show(fig)
    plt.show()

def getDataPoloniex():
    polo = poloniex.Poloniex()
    polo.timeout = 2
#    chartUSDT_BTC = polo.returnChartData(
#        'USDT_BTC', period=polo.DAY, start=time.time() - polo.DAY * 500, end=time.time())
    chartUSDT_BTC = polo.returnChartData(
        'USDT_BTC', period=86400, start=time.time() - polo.DAY * 500, end=time.time())
    tmpDate = [chartUSDT_BTC[i]['date'] for i in range(len(chartUSDT_BTC))]
    date = [datetime.datetime.fromtimestamp(
        tmpDate[i]).date() for i in range(len(tmpDate))]
    data = [float(chartUSDT_BTC[i]['open']) for i in range(len(chartUSDT_BTC))]
    return date, data


if __name__ == "__main__":
    main()
