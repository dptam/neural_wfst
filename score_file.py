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

from EvalHitsAtK import eval_hits_at_k_file

from EvalMap import eval_map_file


def score(prediction_filename, true_label_filename):
    """ Given a file of predictions, compute all metrics
    
    :param prediction_filename: TSV file of predictions
    :param model_name: Name of the model
    :param dataset_name: Name of the dataset
    :return: 
    """
    scores = ""
    map_score = eval_map_file(prediction_filename, true_label_filename)
    scores += "MAP\t{}\n".format(map_score)
    scores += "Hits@1\t{}\n".format(eval_hits_at_k_file(prediction_filename, true_label_filename, 1))
    scores += "Hits@10\t{}\n".format(eval_hits_at_k_file(prediction_filename, true_label_filename, 10))
    scores += "Hits@50\t{}\n".format(eval_hits_at_k_file(prediction_filename, true_label_filename, 50))
    return scores

if __name__ == "__main__":
    prediction_file = sys.argv[1]
    label_file = sys.argv[2]

    out_file = os.path.join(os.path.split(prediction_file)[0], "scores.json")
    with open(out_file,'w') as fout:
        s = score(prediction_file, label_file)
        fout.write(s)
