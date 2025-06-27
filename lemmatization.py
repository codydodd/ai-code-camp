import en_core_web_md

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