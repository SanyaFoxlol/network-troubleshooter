# Ping & Browser Monitor

## Description

This is a simple Python console program that monitors your internet connection ping and detects which web browser is currently running on your system.

The program:

* shows your **hostname**
* shows your **local IP address**
* checks **ping to google.com**
* detects if a **web browser is running**
* updates the information every second

This project was created as a **simple practice project**.

## Requirements

* Python 3
* psutil library

Install the required library:

pip install psutil

## How to Run

1. Save the script as `monitor.py`
2. Run it in the terminal:

python monitor.py

## Example Output

## PING MONITOR

Ping: 23.41 ms
Browser: Google Chrome

The screen updates every second with new data.

## Supported Browsers

The program currently detects:

* Google Chrome
* Mozilla Firefox
* Microsoft Edge
* Opera
* Brave

## Notes

* The ping is measured by checking connection time to **google.com**.
* The program scans running processes to detect active browsers.
* The console screen refreshes to avoid printing new lines continuously.
