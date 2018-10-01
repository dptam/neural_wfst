import sys 
import os
from random import choices

def trim_test_file(test_file_path, trimmed_test_file_path):
    (map_query_2_positives, map_query_2_negatives) = get_map_query_2_lines(test_file_path)

    with open(trimmed_test_file_path, 'w') as write_file: 
        counter = 0

        for (k, v) in map_query_2_positives.items():
            num_pos_lines = 0
            for v in map_query_2_positives[k]:
                line = '\t'.join(v) + '\n'
                write_file.write(line)
                num_pos_lines += 1
                if(num_pos_lines >= 100):
                    break
            num_neg_lines = choices(map_query_2_negatives[k], k = (100 - num_pos_lines))

            for i in num_neg_lines:
                line = '\t'.join(i) + '\n'
                write_file.write(line)

            counter += 1
            if(counter >= 50):
                return


def get_map_query_2_lines(filepath):
    map_query_2_positives = {}
    map_query_2_negatives = {}

    with open(filepath, 'r') as file:        
        for line in file.readlines():
            entities = line.strip('\n').split('\t')
            query = entities[0]
            label = int(entities[2])

            if(label == 1):
                if query in map_query_2_positives.keys():
                    map_query_2_positives[query].append(entities)
                else:
                    map_query_2_positives[query] = [entities]
            else:
                if query in map_query_2_negatives.keys():
                    map_query_2_negatives[query].append(entities)
                else:
                    map_query_2_negatives[query] = [entities]


    return (map_query_2_positives, map_query_2_negatives)

def main():
    file_path = sys.argv[1]
    trimmed_file_path = file_path + "_trimmed"
    trim_test_file(file_path, trimmed_file_path)

if __name__ == "__main__":
    main()
