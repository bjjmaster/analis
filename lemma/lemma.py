from Content_split.spiter import splitter_sample
import nltk
import pymorphy2


def get_lemma(path_):
    z = ""
    sample_lemmas = []
    sample = splitter_sample(path_)
    sample_list = [sample[1][z] for z in sample[1]]  # тут содержание без пунктов в олном массиве ['термины и определения', 'цели и задачи проекта', 'исходные данные' .....
    sample_list_split = [sample[0][z] for z in sample[0]]  # тут [['термины', 'и', 'определения'], ['цели', 'и', 'задачи', 'проекта'].......
    sample_list_in_one_letter = " ".join(sample_list).split()

    morth = pymorphy2.MorphAnalyzer()

    for token in sample_list_in_one_letter:
        sample_lemmas.append(morth.parse(token)[0].normal_form)

    return sample_lemmas










