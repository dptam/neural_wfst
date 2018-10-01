import sys 
import os

def flip_test_scores_file(file_path, flipped_test_scores_path):
    with open(file_path, 'r') as read_file, open(flipped_test_scores_path, 'w') as write_file:  
        for line in read_file.readlines():

            entities = line.strip('\n').split('\t')
            flipped_score = - float(entities[2])

            line = '\t'.join(entities[:2]) + '\t' + str(flipped_score) + '\n'
            write_file.write(line)

def main():
    file_path = sys.argv[1]
    flipped_test_scores_path = file_path + "_flipped"
    flip_test_scores_file(file_path, flipped_test_scores_path)

if __name__ == "__main__":
    main()
