import re
from config import FINAL_REGEX, INPUT_FILENAME, OUTPUT_FILENAME


def find_logs_by_regex(filename, time):
    pattern = re.compile(time)
    saved_logs = list()
    with open(filename, 'r', encoding='utf-8', errors='ignore') as logfile:
        for line in logfile:
            if pattern.match(line):
                saved_logs.append(line)
    return saved_logs


def write_received_logs_to_file(filename, logs):
    with open(filename, 'w') as outfile:
        for line in logs:
            outfile.write(line)


def main():
    logs = find_logs_by_regex(INPUT_FILENAME, FINAL_REGEX)
    write_received_logs_to_file(OUTPUT_FILENAME, logs)


if __name__ == '__main__':
    main()
