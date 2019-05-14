for i in `seq 0 15`; do echo $i; sh -c "python3 parallel_Edge.py /home/neoinmtv/dev/memesearch/data/allpng_200x150_shard_$i Output &" ; done
