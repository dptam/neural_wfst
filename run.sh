#!/usr/bin/env bash

sbatch --partition=titanx-long --gres=gpu:1 train.sh res/wiki/artist/artist.train_trimmed res/wiki/artist/artist.dev_trimmed res/wiki/artist/artist.test_trimmed results/artist/run_2

sbatch --partition=titanx-long --gres=gpu:1 train.sh res/wiki/assignee/assignee.train_trimmed res/wiki/assignee/assignee.dev_trimmed res/wiki/assignee/assignee.test_trimmed results/assignee/run_2

sbatch --partition=titanx-long --gres=gpu:1 train.sh res/wiki/disease/disease.train_trimmed res/wiki/disease/disease.dev_trimmed res/wiki/disease/disease.test_trimmed results/disease/run_2

sbatch --partition=titanx-long --gres=gpu:1 train.sh res/wiki/wiki/wiki.train_trimmed res/wiki/wiki/wiki.dev_trimmed res/wiki/wiki/wiki.test_trimmed results/wiki/run_2

sbatch --partition=titanx-long --gres=gpu:1 train.sh res/wiki/wikippl/wikippl.train_trimmed res/wiki/wikippl/wikippl.dev_trimmed res/wiki/wikippl/wikippl.test_trimmed results/wikippl/run_2



