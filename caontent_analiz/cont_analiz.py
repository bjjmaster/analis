from lemma.lemma import get_lemma
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

path = "C:\\Users\\max\\PycharmProjects\\analis\\doc_analizator\\TZ\\good\\GOOD_Техническое задание2.docx"
path_sample = 'C:\\Users\\max\\PycharmProjects\\analis\\doc_analizator\\politics\\sample.docx'

sample = get_lemma(path_sample)
real = get_lemma(path)

print(sample)
print(real)