import glob
import pandas as pd
import os

# get data file names
path =r'C:/Development/MAKEathon/text_files'
filenames = glob.glob(path + "/*.txt")

dfs = []
cpes = []
i = 0

for filename in filenames:
    f = open(filename, "r")
    first_line = f.readline()
    lines = f.readlines()[0:]
    full_text = ' '.join(lines)
    full_text = full_text.rstrip("\n")
    first_line = first_line.rstrip("\n")
    dfs.append(full_text)
    cpes.append(first_line)

dict = {'CPE': cpes, 'text': dfs}
df = pd.DataFrame(dict)

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