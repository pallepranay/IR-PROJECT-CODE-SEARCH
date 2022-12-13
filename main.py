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
print(">>>> 1. Loading data...")
data = load_data()  # Loading the data
data = drop_nan(data)

# Getting the pos_index
print(">>> 2. Constructing the Positional Indexing..")
pos_index = get_pos_index(data)

# Vectorizing the training data
print(">>> 3. Vectorizing the data.")
tfidf, tfidf_transformed_vector = tfidf_vectorize_data(data)

# Ranking for the given query
print(">>>> 4. Ranking and displaying outputs for the query...")

print(">>>>>>>> 5. Printing the query <<<<<<<<")
print(query)
print('--------------------------------------------------')

cosine_sim = cosine_sim(query, tfidf, tfidf_transformed_vector)

top_results = get_top_results(data, cosine_sim)
print(top_results)


