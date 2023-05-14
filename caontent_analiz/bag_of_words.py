from lemma.lemma import get_lemma
from collections import Counter
import numpy as np



def add_zero(list1, list2):
    mx = max((len(list1), len(list2)))
    mn = min((len(list1), len(list2)))
    x = []
    for i in range(mx - mn):
        x.append(0)
    if len(list1) > len(list2):
        x = x + list2
        return np.array(list1), np.array(x)
    else:
        x = x + list1
        return np.array(x), np.array(list2)


path = "C:\\Users\\max\\PycharmProjects\\analis\\doc_analizator\\TZ\\good\\GOOD_Техническое задание2.docx"
path_sample = 'C:\\Users\\max\\PycharmProjects\\analis\\doc_analizator\\politics\\sample.docx'

# Сначала попробуем без стоп слов
sample = get_lemma(path_sample)
real = get_lemma(path)

words_sample = Counter(sample)
word_to_index_sample = {}
index_to_word_sample = {}

for i, word in enumerate(words_sample.most_common(
        10000 - 2)):  # принцип такой найти все слова и изходя из них самомому попуряному давать цифру 2 и так далее
    word_to_index_sample[word[0]] = i + 2
    index_to_word_sample[i + 2] = word[0]

seq_sample = [word_to_index_sample.get(world, 1) for world in sample]
sqe = [word_to_index_sample.get(world, 1) for world in real]
buffer  = add_zero(seq_sample, sqe)
sample_vector = buffer[0]
real_vector = buffer[1]

print(len(sample_vector))
print(real_vector)
print(len(real_vector))
#
#
#
#
# print(spatial.distance.cosine(real_vector, sample_vector))
# print(F.cosine_similarity(torch.FloatTensor(sample_vector), torch.FloatTensor(real_vector), dim=0))
# #
# sns.histplot(data=np.array(sqe))
# sns.histplot(data=np.array(seq_sample))
# plt.show()