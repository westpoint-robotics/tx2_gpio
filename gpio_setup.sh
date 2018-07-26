#!/bin/bash
for pin in 388 289 480 486; do
    echo $pin > /sys/class/gpio/export
done

