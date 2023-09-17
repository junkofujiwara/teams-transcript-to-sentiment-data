"""file utility"""
import csv

def read(filename):
    """Reads a file and returns a list of lines"""
    with open(filename, encoding="utf-8") as file:
        lines = [line.strip() for line in file]
    return lines

def write(data, filename, delimiter="\t"):
    """Writes a list of lines to a file"""
    with open(filename, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        for row in data:
            writer.writerow(row)

def convert(lines, timeseparator="-->"):
    """Converts a list of lines to a list of lists"""
    data = []
    item = []
    count = 0
    for line in lines:
        if timeseparator in line:
            count = 0
            row = line.split(timeseparator)
            item = []
            item.append(row[0].strip())
            item.append(row[1].strip())
        else:
            count += 1
            item.append(line)
            if count == 2:
                data.append(item)
    return data

def format_output(index, line, sentiment_result, phrases_result):
    """Formats a output line"""
    sentiment, positive, neutral, negative = sentiment_result[0][1], sentiment_result[0][2], sentiment_result[0][3], sentiment_result[0][4]
    phrases = phrases_result[0][1]
    result_line = []
    result_line.append(index)
    result_line.append(line[0])
    result_line.append(line[1])
    result_line.append(line[2])
    result_line.append(line[3])
    result_line.append(sentiment)
    result_line.append(positive)
    result_line.append(neutral)
    result_line.append(negative)
    result_line.append(','.join(phrases))
    return result_line