import sys 
import os

def trim_train_file(train_file_path, trimmed_train_file_path):
    map_query_2_positives = get_map_query_2_positives(train_file_path)

    counter = 0

    with open(trimmed_train_file_path, 'w') as write_file:  
        for k in map_query_2_positives.keys():

            for v in map_query_2_positives[k]:
                line = k + '\t' + v + '\n'  
                line.replace('^', '') 
                write_file.write(line)
                break
            counter += 1
            if(counter >= 10000):
                return

def get_map_query_2_positives(filepath):
    map_query_2_positives = {}

    with open(filepath, 'r') as file:        
        for line in file.readlines():
            entities = line.strip('\n').split('\t')
            query = entities[0]
            positive = entities[1]
            if query in map_query_2_positives.keys():
                map_query_2_positives[query].add(positive)
            else:
                map_query_2_positives[query] = {positive}

    return map_query_2_positives

def main():
    file_path = sys.argv[1]
    trimmed_file_path = file_path + "_trimmed"
    trim_train_file(file_path, trimmed_file_path)

if __name__ == "__main__":
    main()
