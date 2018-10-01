import os
import sys

if __name__ == '__main__':
    test_data_dir = sys.argv[1]

    idx = 1
    while(True):
        run_test_data_dir = os.path.join(test_data_dir, "run_" + str(idx))
        if(not os.path.exists(run_test_data_dir)):
            os.makedirs(run_test_data_dir)
            train_folder = os.path.join(run_test_data_dir, "train")
            test_folder = os.path.join(run_test_data_dir, "test")
            os.makedirs(train_folder)
            os.makedirs(test_folder)
            for i in range(0, 10):
                partition_test_folder = os.path.join(test_folder, "partition_" + str(i))
                os.makedirs(partition_test_folder)

            break
        idx += 1

