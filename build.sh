#!/bin/sh

pyuic5 -x ./src/components/mainWindow/main_window.ui -o ./src/components/mainWindow/main_window.py

pyuic5 -x ./src/components/ipRules/ip_rules.ui -o ./src/components/ipRules/IPRules.py

pyuic5 -x ./src/components/macRules/mac_rules.ui -o ./src/components/macRules/MACRules.py
