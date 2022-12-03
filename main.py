from modules import *
from utils import *
from loader import *
from indexer import *
from vectorizer import *
from preprocess import *
import sys

# time = datetime.datetime.now()

query = sys.argv[1]




# Main file

# print("Loading data...")
data = load_data()  # Loading the data


data = drop_nan(data)
# Getting the pos_index
# print("Constructing Positional Indexing...")
pos_index = get_pos_index(data)


# Vectorizing the training data
# print("Vectorizing data...")
tfidf, tfidf_transformed_vector = tfidf_vectorize_data(data)

# print("Ranking and displaying outputs for the query...")
# Ranking for the given query

# used for taking input from txt file
# reminder: need to uncomment while showing to RP Sir.

# with open("input.txt", "r") as input:
#     query = input.readlines()
#     query = ' '.join(query)


# print("*****Printing query*****")
# print(query)
# print('--------------------------------------------------')

cosine_sim = cosine_sim(query, tfidf, tfidf_transformed_vector)

top_results = get_top_results(data, cosine_sim)
print(top_results)


# Acessing Relevance

# relevence_feedback = input(
#     "Enter the indices of relevant documents retrieved (space seperated): \n").split(" ")

