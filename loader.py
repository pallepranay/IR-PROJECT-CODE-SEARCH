from modules import *

# Loading data


def load_data():
    # if not os.path.exists("data\cleaned_data_small.csv"):
    #     with open('data\dump-original.jsonl') as json_file:
    #         data = json_file.readlines()
    #         data = list(map(json.loads, data))

    #     original_df = pd.DataFrame(data)

    #     with open('data\dump-tokenized.jsonl') as json_file:
    #         data = json_file.readlines()
    #         data = list(map(json.loads, data))

    #     tokenized_df = pd.DataFrame(data)

    #     original_df["source_tokenized"] = tokenized_df["source"]
    #     original_df.rename(
    #         columns={"source": "source_original"}, inplace=True)

    #     original_df.to_csv("data\cleaned_data.csv")
    #     original_df.iloc[:1000].to_csv("data\cleaned_data_small.csv")
    #     original_df_small = original_df.iloc[:1000]
    # else:
    original_df_small = pd.read_csv("E://IR-MiniProject//data//cleaned_data_small.csv")
    return original_df_small
