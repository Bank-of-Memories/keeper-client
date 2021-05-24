#!/bin/bash

wget https://dist.ipfs.io/go-ipfs/v0.8.0/go-ipfs_v0.8.0_linux-amd64.tar.gz
tar xvfz go-ipfs_*
cd go-ipfs*
sudo ./install.sh

ipfs init
echo "/key/swarm/psk/1.0.0/
/base16/
cbcf8b0c0a962df0ca530c50ae567f8d1ee5e5c791701c52e4aef8bfa222b6c9" > ~/.ipfs/swarm.key

ipfs bootstrap rm --all
ipfs bootstrap add /ip4/167.86.71.92/tcp/4005/ipfs/12D3KooWHw78xTEE99hbRghAAM68jGdeHsexg3rkFQ2aT8Evijcw

export LIBP2P_FORCE_PNET=1