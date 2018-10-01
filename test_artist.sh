#!/usr/bin/env bash


python -c "import os; import transducer_score; print (transducer_score.main(train_fn='res/wiki/artist/artist.train_trimmed', dev_fn='res/wiki/artist/artist.dev_trimmed', test_fn='res/wiki/artist/test_partitions/partition_0', folder='results/artist/run_1/test/partition_0', pretrained_param_pklfile='results/artist/run_1/train/transducer.pkl', perform_training=0, perform_testing=1, nepochs=50))"
