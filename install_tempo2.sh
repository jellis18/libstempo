#!/bin/bash

# get install location
if [ $# -eq 0 ]
	then
		echo 'No install location defined, using' $HOME'/.local/tempo2'
		prefix=$HOME/.local/tempo2
	else
		prefix=$1
		echo 'Will install in' $prefix
fi

#git clone https://bitbucket.org/psrsoft/tempo2.git
git clone https://jellis11@bitbucket.org/jellis11/tempo2.git
cd tempo2
./bootstrap
mkdir -p $prefix
export TEMPO2=$prefix
export LD_LIBRARY_PATH=$TEMPO2/lib:$LD_LIBRARY_PATH
cp -r T2runtime/* $TEMPO2
./configure --prefix=$TEMPO2
make && make install
make plugins-install
cd ../
rm -rf tempo2
