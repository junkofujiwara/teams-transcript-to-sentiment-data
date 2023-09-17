"""Converts a file from txt to csv format"""
from util.file import read, convert, write, format_output
from util.sentiment import authenticate_client, analyze_sentiment, key_phrase_extraction
import settings

def main():
    """Main function"""
    lines = read(settings.INPUT_FILE)
    data = convert(lines)
    client = authenticate_client(settings.AZURE_LANGUAGE_ENDPOINT, settings.AZURE_LANGUAGE_KEY)
    sentence = []
    result_data = [["Index", "Start_Time", "End_Time", "Speaker", "Text",
                    "Sentiment", "Positive_Score", "Neutral_Score", "Negative_Score",
                    "Key_Phrases"]]
    index = 0
    for line in data:
        sentence = [line[3]]
        sentiment_result = analyze_sentiment(client, sentence)
        phrases_result = key_phrase_extraction(client, sentence)
        result_data.append(format_output(index, line, sentiment_result, phrases_result))
        index += 1
    write(result_data, settings.OUTPUT_FILE, settings.OUTPUT_DELIMITER)

if __name__ == "__main__":
    main()
