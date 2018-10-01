import os
import sys

if __name__ == "__main__":
    train_file = sys.argv[1]
    dev_file = sys.argv[2]
    test_folder = sys.argv[3]
    folder = sys.argv[4]
    param_file = sys.argv[5]
    partition = sys.argv[6]

    bash_script = os.path.join(folder, "parallel_eval_model.sh")

    with open(bash_script, 'w+') as f:
        f.write("#!/usr/bin/env bash \n")

        for i in range(10):
            test_file = os.path.join(test_folder, ('partition_' + str(i)))
            folder_file = os.path.join(folder, ('partition_' + str(i)))
            error_file = os.path.join(folder_file, "error")
            output_file = os.path.join(folder_file, "output")
            command = "sbatch --partition={} --gres=gpu:1 --error={} --output={}--mem=15GB test.sh {} {} {} {} {} \n".format(partition, error_file, output_file, train_file, dev_file, test_file, folder_file, param_file)
            f.write(command + '\n')