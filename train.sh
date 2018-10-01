#!/usr/bin/env bash

train_file=$1
dev_file=$2
test_file=$3
folder=$4

export train_file
export dev_file
export test_file
export folder


python -c "import os; import transducer_score; print (transducer_score.main(train_fn=os.environ['train_file'], dev_fn=os.environ['dev_file'], test_fn=os.environ['test_file'], folder=os.environ['folder']))"
