from lemma.lemma import get_lemma
import difflib
from bag_of_words import sqe, seq_sample



def similarity(s1, s2):
  matcher = difflib.SequenceMatcher(None, s1, s2)
  return matcher.ratio()


path = "C:\\Users\\max\\PycharmProjects\\analis\\doc_analizator\\TZ\\good\\GOOD_Техническое задание2.docx"
path_sample = 'C:\\Users\\max\\PycharmProjects\\analis\\doc_analizator\\politics\\sample.docx'

sample = get_lemma(path_sample)
real = get_lemma(path)

print(similarity(real, sample))
print(similarity(sqe, seq_sample))