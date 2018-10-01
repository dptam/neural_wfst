import sys 
import os

def trim_dev_file(dev_file_path, trimmed_dev_file_path):
    with open(dev_file_path, 'r') as read_file, open(trimmed_dev_file_path, 'w') as write_file:  
        counter = 0

        for line in read_file.readlines():

            entities = line.strip('\n').split('\t')
            if(int(entities[2]) == 1):
                line = entities[0] + '\t' + entities[1] + '\n'
                line.replace('^', '') 
                write_file.write(line)
                counter += 1
                if(counter >= 1000):
                    break

def main():
    file_path = sys.argv[1]
    trimmed_file_path = file_path + "_trimmed"
    trim_dev_file(file_path, trimmed_file_path)

if __name__ == "__main__":
    main()
