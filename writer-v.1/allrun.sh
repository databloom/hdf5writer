#!/bin/bash


echo "das sec2"
 time python writer.py ;
rm -f /opt/big/*data.h5;
#echo "das core"
# time python writer_core.py;
rm -f /opt/big/*data* ;
echo "nfs sec2"
 time python nfs_writer.py;
# rm -f /gonzo/hdf5/data* ;
#echo "nfs core"
# time python nfs_writer_core.py ;
# rm -f /gonzo/hdf5/data*;
echo "nfs  sec2 concurrent"
 time python nfs_writer_conncurrent.py;
 rm -f /gonzo/hdf5/concurrent/*;
echo "nfs sec2 streaming "
 time python nfs_writer_streaming.py ;
 rm -f /gonzo/hdf5/streaming/*

echo "nfs fozzie  sec2 concurrent"
 time python nfs_writer_conn_h400.py;
 rm -f /fozzie/hdf5/concurrent/*;
echo "nfs fozzie sec2 streaming "
 time python nfs_writer_streaming_h400.py ;
 rm -f /fozzie/hdf5/streaming/*

