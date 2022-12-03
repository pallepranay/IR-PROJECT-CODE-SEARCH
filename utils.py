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

#                              testing.....

# add feedback to the top results
import random
import pandas as pd

def read_csv():
    return pd.read_csv('D://IR-PROJECT-CODE-SEARCH//data//feedback.csv')
    
def get_top_results(data, score):
    top_results = score.argsort()[::-1]
    results = {"Code": [], "Similarity": [] , "feedback": [] , "index": [] }
    df = read_csv()
    # read df and add feedback to the top results
    for i in top_results[:10]:
        # print(i)
        if df.loc[df['index'] == i].empty:
            results["feedback"].append(0)
        else:
            results["feedback"].append(df.loc[df['index'] == i, 'feedback'].values[0])
    
    max_feedback = max(results["feedback"])==0 and 1 or max(results["feedback"])
    # for i in range (len(results["feedback"])): 
    #     results["feedback"][i] = ((results["feedback"][i]/ max_feedback)*60 + (results["Similarity"][i])*40)
    
    for idx in top_results[:10]:
        results["Code"].append(data.iloc[idx]["source_original"])
        results["Similarity"].append(score[idx])
        results["index"].append(idx)
        # results["feedback"][idx] = results["feedback"][idx]/max_feedback*60 + results["Similarity"][idx]*40
    for i in range (len(results["feedback"])):
        results["feedback"][i] = ((results["feedback"][i]/ max_feedback)*60 + (results["Similarity"][i])*40)

    results["Code"] = [x for _, x in sorted(zip(results["feedback"], results["Code"]), reverse=True)]
    results["Similarity"] = [x for _, x in sorted(zip(results["feedback"], results["Similarity"]), reverse=True)]
    results["index"] = [x for _, x in sorted(zip(results["feedback"], results["index"]), reverse=True)]
    results["feedback"] = sorted(results["feedback"], reverse=True)

    # for i in range(len(results["Code"])):
    #     print("after: ", results["feedback"][i])
        
    # print('--------------------------------------------------')
                
    results_str = ""
    for i in range(10):
        results_str += "Index: " + str(results["index"][i]) + "\n" + \
            results["Code"][i] + "\n" + "Cosine Similarity: " + \
            str(results["Similarity"][i]) + "\n"
        results_str = results_str + "-"*50 + "\n"

    print(results_str)
    with open("data/results.txt", "w") as file:
        file.writelines(results_str)

    return results_str