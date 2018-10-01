"""
Copyright (C) 2017-2018 University of Massachusetts Amherst.
This file is part of "learned-string-alignments"
http://github.com/iesl/learned-string-alignments
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
import os

if __name__ == "__main__":
    test_dir = sys.argv[1]
    num_partitions = sys.argv[2]
    
    test_prediction_filename = os.path.join(test_dir, "test.predictions")
    with open(test_prediction_filename, 'w+') as f_out:
        total_lines = 0
        for i in range(int(num_partitions)):
            parititon_prediction_filename = os.path.join(test_dir, "partition_{}".format(str(i)), "current.test.txt")
            if(os.path.exists(parititon_prediction_filename)):
                with open(parititon_prediction_filename, 'r') as f_in:
                    all_lines =  f_in.readlines()
                total_lines += len(all_lines)
                for line in all_lines:
                    if("input prediction goldOutput" not in line):
                        f_out.write(line)
