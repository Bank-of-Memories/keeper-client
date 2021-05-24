@echo off

wget https://dist.ipfs.io/go-ipfs/v0.8.0/go-ipfs_v0.8.0_windows-amd64.zip
tar -xf go-ipfs_*
cd go-ipfs*
ipfs.exe init
ipfs.exe bootstrap rm --all
ipfs.exe bootstrap add /ip4/167.86.71.92/tcp/4005/ipfs/12D3KooWHw78xTEE99hbRghAAM68jGdeHsexg3rkFQ2aT8Evijcw