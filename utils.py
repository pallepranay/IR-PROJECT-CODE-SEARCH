from modules import *


def finding_all_unique_words_and_frequency(words):
    words_unique = []
    word_freq = {}

    for word in words:
        if word not in words_unique:
            words_unique.append(word)
    for word in words_unique:
        word_freq[word] = words.count(word)

    return word_freq


def finding_freq_of_word_in_doc(word, words):
    freq = words.count(word)


def cosine_sim(query, vectorizer, tfidf_transformed):
    test_tfidf = vectorizer.transform([query])
    cos = []
    cosing_similarities = linear_kernel(
        test_tfidf, tfidf_transformed).flatten()
    cos.append(cosing_similarities)
    return np.array(cos).flatten()


def get_top_results(data, score):
    top_results = score.argsort()[::-1]
    results = {"Code": [], "Similarity": []}
    for idx in top_results[:10]:
        results["Code"].append(data.iloc[idx]["source_original"])
        results["Similarity"].append(score[idx])

    results_str = ""
    for i in range(10):
        results_str += "Index: " + str(top_results[i]) + "\n" + \
            results["Code"][i] + "\n" + "Cosine Similarity: " + \
            str(results["Similarity"][i]) + "\n"
        results_str = results_str + "-"*50 + "\n"

    print(results_str)
    with open("data/results.txt", "w") as file:
        file.writelines(results_str)

    return results_str
