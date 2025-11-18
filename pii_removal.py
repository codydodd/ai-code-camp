from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Advanced
from presidio_analyzer import PatternRecognizer, Pattern, RecognizerRegistry

# Initialize engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Sample fake data
text = "Hi, my name is Alice Johnson. My phone number is 555-123-4567 and my email is alice.j@example.com."

# Step 1: Analyze PII
results = analyzer.analyze(text=text, entities=["PHONE_NUMBER", "EMAIL_ADDRESS", "PERSON"], language="en")

# Step 2: Anonymize PII
anonymized_result = anonymizer.anonymize(text=text, analyzer_results=results)

# Output
print("Original Text:\n", text)
print("\nAnonymized Text:\n", anonymized_result.text)


## Advanced, adding Canadian SIN
# Define SIN pattern: 9 digits, optionally with dashes
sin_pattern = Pattern(name="SIN Pattern", regex=r"\b\d{3}-\d{3}-\d{3}\b|\b\d{9}\b", score=0.85)
sin_recognizer = PatternRecognizer(supported_entity="CANADIAN_SIN", patterns=[sin_pattern])
postal_code_pattern = Pattern(name="Canadian Postal Code Pattern", regex=r"\b[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d\b", score=0.85)
postal_code_recognizer = PatternRecognizer(supported_entity="CANADIAN_POSTAL_CODE", patterns=[postal_code_pattern]) 

# Set up analyzer with custom recognizer
registry = RecognizerRegistry()
registry.load_predefined_recognizers()
registry.add_recognizer(sin_recognizer)
registry.add_recognizer(postal_code_recognizer)

analyzer = AnalyzerEngine(registry=registry)

# Set up anonymizer
anonymizer = AnonymizerEngine()

# Sample fake data
text = (
    "Hi, my name is Alice Johnson. My phone number is 555-123-4567, "
    "my email is alice.j@example.com, and my SIN is 123456789. I live at K0H 5X6"
)

# Analyze and anonymize
results = analyzer.analyze(text=text, entities=["PHONE_NUMBER", "EMAIL_ADDRESS", "PERSON", "CANADIAN_SIN", "CANADIAN_POSTAL_CODE"], language="en")
anonymized_result = anonymizer.anonymize(text=text, analyzer_results=results)

# Output
print("Original Text:\n", text)
print("\nAnonymized Text:\n", anonymized_result.text)

