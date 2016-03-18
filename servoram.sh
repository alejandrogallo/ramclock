#! /usr/bin/env bash

MAX_ANGLE=180

CURRENT_ANGLE=$(free | grep Mem: | awk '{print '$MAX_ANGLE'*$3/$2}')


echo $CURRENT_ANGLE
sudo python servo_move.py -a $CURRENT_ANGLE
