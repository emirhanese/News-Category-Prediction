# Importing required libraries.
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import word_tokenize
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from translate import Translator
import pickle
import re


class Model:
    def __init__(self):
        # Machine learning algorithm that we'll use. # ! Learn hyper parameters.
        self.model = LogisticRegression(solver='newton-cg', multi_class='multinomial', penalty='l2', C=1, random_state=1881)
        self.vectorizer = CountVectorizer()  # ! Learn
        self.model_accuracy = float
        self.mapping_dict = {}
        self.features_train = []
        self.features_test = []
        self.labels_train = []
        self.labels_test = []

    # Investigating the data.
    def investigate_data(self):
        try:
            print(self.data.info())

        except AttributeError:
            self.data = pd.read_csv("Dataset/news.csv")

        print(self.data.info())  # *There is not any null data in the dataset.
        print(end="\n")
        print(self.data.head())
        print(end="\n")
        print(self.categories)

    # Adding new data that includes new categories to our actual dataset.
    def concatenate_data(self):
        new_data = pd.read_json("Dataset/News_Category_Dataset_v2.json", lines=True)
        df2 = self.data

        # Columns that we want to add to our main dataset.
        colsToBeConcat = ["CRIME", "POLITICS", "SPORTS"]

        for col in colsToBeConcat:
            df = new_data[new_data["category"] == col]
            df = df[["headline", "category"]]

            # Renaming the columns from 'headline' to 'TITLE' and 'category' to 'CATEGORY'
            df = df.rename(columns={"headline": "TITLE", "category": "CATEGORY"})
            df["CATEGORY"] = df["CATEGORY"].apply(lambda text: text.lower()[0])
            df2 = df2.append(df, ignore_index=True)

        self.data = df2
        self.data.to_csv("Dataset/news.csv")

    # Visualize the data.
    def visualize_data(self):
        try:
            print(self.data.info())

        except AttributeError:
            self.data = pd.read_csv("Dataset/news.csv")
        value_counts = []

        for category in self.categories:
            value_counts.append(self.data.value_counts("CATEGORY")[category])

        plt.figure(figsize=(8, 7))
        plt.xlabel("Kategori", fontsize=14)
        plt.ylabel("Sayı", fontsize=14)
        plt.title("Kategorilerin Sayıca Dağılımı", fontsize=16)
        plt.bar(self.categories, value_counts, color=("r", "g", "b", "purple"))
        plt.show()

    # Cleaning the dataset from reduntant data.
    def clean_text(self, text: str):
        text = text.lower()
        stop_words = stopwords.words('english')
        text = re.sub('\s\W', ' ', text)
        text = re.sub('\W\s', ' ', text)
        text = re.sub('\s+', ' ', text)
        text = re.sub("\'\w+", '', text)

        word_tokenized = word_tokenize(text)

        filtered_text = [
            word for word in word_tokenized if word not in stop_words]

        final_text = ' '.join(filtered_text)

        return final_text

    # Encode and vectorize the data.
    def encode_and_vectorize(self):
        self.data["Processed Text"] = self.data['TITLE'].apply(self.clean_text)
        self.data["Processed Text"].to_csv("Model/processed.csv")

        # Encoding the categories in dataset. mapping_dict = {0:b, 1:e, 2:m, 3:t}
        label_encoder = LabelEncoder()
        self.data["CATEGORY"] = [str(category)
                                 for category in self.data["CATEGORY"]]
        self.data["TARGET"] = label_encoder.fit_transform(
            self.data["CATEGORY"])
        self.mapping_dict = {index: label for index,
                             label in enumerate(label_encoder.classes_)}

        # Vectorizing the data. Vectorizing means, converting the text data into numeric value.
        x = self.vectorizer.fit_transform(self.data['Processed Text'])

        # TARGET column has already been turned into numeric value (mapping_dict). So we don't apply vectorizer to that column.
        y = self.data["TARGET"]

        # split into train and test sets
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2)

        self.features_train = x_train
        self.labels_train = y_train

        self.features_test = x_test
        self.labels_test = y_test

    # Creating the model.
    def create_model(self):
        self.model.fit(self.features_train, self.labels_train)
        lg_predictions = self.model.predict(self.features_test)
        self.model_accuracy = accuracy_score(self.labels_test, lg_predictions)

        # *Saving the model with pickle module.
        with open("Model/saved_model.pkl", 'wb') as file:
            pickle.dump((self.model, self.vectorizer.vocabulary_,
                         self.mapping_dict, self.model_accuracy, self.categories), file)

        # Demonstrating the accuracy of the model that has been created.
        print("Accuracy:", self.model_accuracy)

    # To check if the text is in Turkish.
    def isTurkish(self, text:str):
        tr_characters = "çÇğĞıİöÖşŞüÜ"
        for i in tr_characters:
            if i in text:
                return True

        return False

    # If input is in Turkish then this function is being used to translate Turkish text to English.
    def translate(self, text:str):
        translator = Translator(to_lang="en")
        translation = translator.translate(text)

        return translation

    # A function which takes string as a parameter is created. This function makes a prediction according to user's input.
    def forecast(self, text_to_predict:str):
        if self.isTurkish(text_to_predict):
            text_to_predict = self.translate(text_to_predict)
            
        text_to_predict = [self.clean_text(text_to_predict)]
        text_to_predict = self.vectorizer.transform(text_to_predict)
        prediction = self.model.predict(text_to_predict)
        return self.mapping_dict.get(int(prediction))

    # Initializing the model. This function first cleans, encodes and vectorizes the data and then creates the model that we'll use.
    def initialize_model(self):
        # ! Try - except bloklari eklenip optimize edilecektir.
        try:
            with open("Model/saved_model.pkl", "rb") as file:
                self.model, vocab, self.mapping_dict, self.model_accuracy, self.categories = pickle.load(file)
                self.vectorizer = CountVectorizer(vocabulary=vocab)

        except Exception as e:
            self.data = pd.read_csv("Dataset/uci-news-aggregator.csv")
            # Data in the other columns is unnecessary. So we only get TITLE and CATEGORY column.
            self.data = self.data[['TITLE', 'CATEGORY']]
            # Now we'll concatenate the new data with 'concatenate_data' function to our main dataset.
            self.concatenate_data()
            # Unique categories in the dataset.
            self.categories = self.data["CATEGORY"].unique()
            self.encode_and_vectorize()
            self.create_model()
