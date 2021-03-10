# We’ve provided a csv file containing data about the game show Jeopardy! in a file named jeopardy.csv.
# Load the data into a DataFrame and investigate its contents. Try to print out specific columns.
# Note that in order to make this project as “real-world” as possible, we haven’t modified the data
# at all — we’re giving it to you exactly how we found it. As a result, this data isn’t as “clean”
# as the datasets you normally find on Codecademy. More specifically, there’s something odd about
# the column names. After you figure out the problem with the column names, you may want to rename
# them to make your life easier the rest of the project.
# In order to display the full contents of a column, we’ve added this line of code to the top of your file:
# from typing import Any, Union

import pandas as pd

pd.set_option('display.max_colwidth', None)

df = pd.read_csv("jeopardy.csv")

df.rename(columns={" Air Date": "Air Date", " Round": "Round", " Category": "Category", " Value": "Value",
                   " Question": "Question", " Answer": "Answer"}, inplace=True)
# print(df.head(20))


# 3
# Write a function that filters the dataset for questions that contains all of the words in a list of words.
# For example, when the list ["King", "England"] was passed to our function, the function returned a DataFrame
# of 152 rows. Every row had the strings "King" and "England" somewhere in its " Question".
# 4
# Test your function by printing out the column containing the question of each row of the dataset.


def filter_for_words(dataframe, words):
    filtered = lambda x: all(word.lower() in x.lower() for word in words)
    return dataframe.loc[dataframe["Question"].apply(filtered)]


filtered_df = filter_for_words(df, ["dog", "girl"])["Question"]
# print(filtered_df)

# 5
# We may want to eventually compute aggregate statistics, like .mean() on the " Value" column.
# But right now, the values in that column are strings. Convert the " Value" column to floats.
# If you’d like to, you can create a new column with the float values.


df["Value_numeric"] = df["Value"].str.extract(r"(\$)(\d+)", expand=True)[1]
df["Value_numeric"] = pd.to_numeric(df["Value_numeric"], downcast="float")
# print(df["Value_numeric"].dtypes)


# Now that you can filter the dataset of question, use your new column that contains the float values
# of each question to find the “difficulty” of certain topics. For example, what is the average value
# of questions that contain the word "King"?
# Make sure to use the dataset that contains the float values as the dataset you use in your filtering function.

difficult_words = filter_for_words(df, ["dog", "duck"])["Value_numeric"]
print(difficult_words.mean())

# 6
# Write a function that returns the count of the unique answers to all of the questions in a dataset. For example,
# after filtering the entire dataset to only questions containing the word "King", we could then find all of the
# unique answers to those questions. The answer “Henry VIII” appeared 3 times and was the most common answer.


def unique_answers(dataframe, words):
    filtered = filter_for_words(dataframe, words).copy()
    filtered.drop_duplicates(inplace=True, ignore_index=True)
    return len(filtered)

print(unique_answers(df, ["cow"]))

