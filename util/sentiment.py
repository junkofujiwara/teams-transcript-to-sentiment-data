""" Sentiment analysis using Azure Text Analytics API"""
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def authenticate_client(endpoint, key):
    """Authenticates the client"""
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

def analyze_sentiment(client, documents):
    """Analyzes sentiment in a list of documents"""
    result = []
    sentiment_result = client.analyze_sentiment(documents, show_opinion_mining=True)
    docs = [doc for doc in sentiment_result if not doc.is_error]
    for idx, doc in enumerate(docs):
        line_result = (documents[idx], doc.sentiment,
                       doc.confidence_scores.positive,
                        doc.confidence_scores.neutral,
                       doc.confidence_scores.negative)
        result.append(line_result)
    return result

def key_phrase_extraction(client, documents):
    """Extracts key phrases from a list of documents"""
    result = []
    key_phrase_result = client.extract_key_phrases(documents)
    docs = [doc for doc in key_phrase_result if not doc.is_error]
    for idx, doc in enumerate(docs):
        line_result = documents[idx], doc.key_phrases
        result.append(line_result)
    return result
