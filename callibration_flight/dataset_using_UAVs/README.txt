#Overview

This file details the data collection campaign based on LoRa devices estimating RSSI and SNR values of a transmitter, buried under snow, and a receiver mounted on an unmanned aerial vehicle (UAV). Data were collected at three different times: April 2024, February 2025 and April 2025.

#How to cite
Mavilia F., La Rosa D., Berton A., Girolami M. "An Experimental Dataset Using UAVs and LoRa Technology in Avalanche Scenarios", ---paper under review

#Hardware settings

##LoRa devices

T-beam boards (by LILYGO) which embeds ESP32 and SX1276 chipsets. Each T-beam board features a GSM/GPRS Antenna L722 (by LILYGO) and is powered by a 30,000 mAh powerbank.

The firmware is set with the following parameters:
- Transmission Power = 14 dBm
- Carrier Frequency = 868 MHz (EU band)
- Spreading Factor = 7
- Bandwidth = 125 kHz
- Coding Rate = 4/5

The UAV used in our experiments is the DJI Matrice 300 RTK. Concerning the antenna, we execute tests with two models: 1. the circular-polarized WANTENNAX019, produced by CAEN RFID; 2. the GSM/GPRS dipole antenna L7222, by LILYGO.


#Test typologies

##The goal is to collect data from an aerial perspective. All the tests can be organized into three main categories:
1. A standing measurement is conducted using a UAV at each of the 121 measurement points, which are regularly arranged in a 100 m × 100 m grid centered on the burial site. This configuration allows for an accurate assessment of LoRa signal propagation by utilizing a large number of measurement points.
2. Measurements are collected in motion over a 100 m × 100 m area, with the UAV following multiple flight paths of different lengths. This configuration emulates reasonable UAV paths during a realistic SAR operation covering a moderate wide area.
3. Measurements are collected in motion over an area exceeding 50,000 square meters, with the UAV following multiple flight paths of different lengths. This configuration emulates UAV paths during a realistic SAR operation covering a large wide area.

Range of parameters:
	Receiver mounted on the UAV.
	- covered area: 10,000 to 120,000 square meters;
	- antenna type: dipole, omnidirectional;
	- speed: 0 to 6.2 m/s;
	- height [a.g.l.]: 15 to 37 meters;
	
	Transmitter buried under the snow.
	- burial depth: 0.4 m, 0.5 m, 0.6 m;
	- antenna polarization: horizontal, vertical;

Details are reported in the paper.

