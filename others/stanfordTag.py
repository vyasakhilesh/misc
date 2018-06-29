import os
from nltk.parse import stanford
os.getenv('CLASSPATH')

os.environ['STANFORD_PARSER'] = 'stanford/jars'
os.environ['STANFORD_MODELS'] = 'stanford/jars'

parser = stanford.StanfordParser(model_path="englishPCFG.ser.gz")
sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your name?"))
print sentences

# GUI
for line in sentences:
    for sentence in line:
        #sentence.draw()
        print sentence
