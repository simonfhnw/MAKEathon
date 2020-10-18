import glob
import pandas as pd

# get data file names
path =r'C:/Development/MAKEathon/text_files'
filenames = glob.glob(path + "/*.txt")

dfs = []
i = 0

for filename in filenames:
    f = open(filename, "r")
    lines = f.read()
    # df = pd.read_csv(f, names=["text"], header=0)
    dfs.append(lines)

dict = {'text': dfs}
df = pd.DataFrame(dict)
big_df = pd.concat()



# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)
# print(big_frame)
print(df)






# from sklearn.feature_extraction.text import CountVectorizer
# import pandas as pd
# import os
#
# filepath_dict = {'test':   'CPE1.txt',
# }
#
# df_list = []
# for source, filepath in filepath_dict.items():
#     df = pd.read_csv(filepath, names=['text'])
#     df['classifier'] = os.path.splitext(filepath)[0]
#     df_list.append(df)
#
# df = pd.concat(df_list)
# print(df.iloc[0])
# print(df)
#
# sentences = ['John likes ice cream', 'John hates chocolate.']
#
# vectorizer = CountVectorizer(min_df=0, lowercase=False)
# vectorizer.fit(sentences)
# vectorizer.vocabulary_