import spacy
import en_core_web_md

# Load spaCy's English model (you can reuse en_core_web_md or en_core_web_lg)
nlp = spacy.load("en_core_web_md")


## Simple

# Open the text file for reading
with open('words.txt', 'r') as file:
    content = file.read()
    print(content)

nlp = en_core_web_md.load()

for word in nlp(content):
    print(word)
    this_lemma = ""
    if word.lemma_.lower() != word.text.lower():
        this_lemma = word.lemma_.lower()
    token = {"word": word.text.lower(), "lemma": this_lemma}
    print(token)



## Advanced

# Sample text
text = "Dr. Alice Johnson visited Ottawa on November 10th to meet with Microsoft executives."

# Process the text
doc = nlp(text)

# Token-level analysis
print("Token Analysis:")
for token in doc:
    print(f"Text: {token.text}, POS: {token.pos_}, Lemma: {token.lemma_}")

# Named Entity Recognition
print("\n🏷️ Named Entities:")
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
