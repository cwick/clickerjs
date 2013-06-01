#!/bin/bash
dns-sd -R myPairingService _touch-remote._tcp . 50006 \
    DvNm="fezmonkey_test" \
    DvTy=iPod \
    RemV=10000 \
    RemN=Remote \
    txtvers=1 \
    Pair=0000000000000001


