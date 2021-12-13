"""
@Author: Qadir Mughal

NOTE: Main text processing script which is responsible to taking care of data and
inserting into different function

this research is based on LDA. LDA (short for Latent Dirichlet Allocation) is an
unsupervised machine-learning model that takes documents as input and finds topics
as output.
"""

import gensim
from gensim.models.ldamulticore import LdaMulticore
from gensim import corpora
from nltk.corpus import stopwords
import pyLDAvis.gensim_models
import string
from nltk.stem.wordnet import WordNetLemmatizer
import webbrowser
import sys
from wordcloud import WordCloud
import logging


class TextProcessing:

    def __init__(self, dataframe):
        """

        :param dataframe:
        """
        self.stopwords = set(stopwords.words('english'))
        self.exclude = set(string.punctuation)
        self.lemma = WordNetLemmatizer()
        self.model = gensim.models
        self.dataframe = dataframe

    def preprocessing(self, text):
        """
        things happening here
        1. Tokenization
        2. removing word with less than 3 char
        3. removing stopwords
        4. lemmatized: converting to first-person verb and past and future to present
        :param text:
        :return:
        """
        try:
            logging.info("Preprocessing started")

            stop_free = ' '.join([word for word in text.lower().split() if word not in self.stopwords])
            punc_free = ''.join(ch for ch in stop_free if ch not in self.exclude)
            normalized = ' '.join([self.lemma.lemmatize(word) for word in punc_free.split()])
            return normalized.split()
        except Exception as e:
            print("Error: preprocessing error")
            print(e)

    def converting_to_bag_of_words(self, text_column):
        """
        converting text to the bag of words
        :param text_column:
        :return:
        """
        try:
            logging.info("preparing the data to be trained")

            self.dataframe['preprocessed'] = self.dataframe[text_column].apply(self.preprocessing)
            dictionary = corpora.Dictionary(self.dataframe['preprocessed'])
            doc_term_matrix = [dictionary.doc2bow(doc) for doc in self.dataframe['preprocessed']]
            return doc_term_matrix, dictionary

        except Exception as e:
            print("Error: error while preparing the data")
            print(e)

    def build_model(self, text_column, num_topics):
        """
        Running LDA on specific column
        :param text_column:
        :param num_topics:
        :return:
        """
        doc_term_matrix, dictionary = self.converting_to_bag_of_words(text_column)
        try:
            logging.info("Building the LDA Model")

            return self.model.LdaMulticore(
                doc_term_matrix,
                num_topics=num_topics,
                id2word=dictionary,
                passes=50,
                minimum_probability=0,
                workers=13), doc_term_matrix, dictionary

        except Exception as e:
            print("Error: building model error")
            print(e)

    def build_with_save_html(self, text_column, num_topics):
        """
        result and saving to html
        :param text_column:
        :param num_topics:
        :return:
        """
        try:
            logging.info("Creating Html interactive visual")

            lda_model, doc_term_matrix, dictionary = self.build_model(text_column, num_topics)
            lda_model.print_topics(num_topics=num_topics)

            lda_display = pyLDAvis.gensim_models.prepare(
                lda_model,
                doc_term_matrix,
                dictionary,
                sort_topics=False,
                mds='mmds',
                R=num_topics)

            pyLDAvis.save_html(lda_display, 'output/top_word_visual.html')
            self.dataframe.to_csv('output/top_words.csv', ';')

        except Exception as e:
            print("Error: Html visual error")
            print(e)

    def show_topic_visual(self):
        """
        showing result on chrome
        :return:
        """
        try:
            logging.info("HTML Visual showing")

            webbrowser.open('file://' + sys.path[0] + '/output/top_word_visual.html')

        except Exception as e:
            print("Error: error while genrating the visual")
            print(e)

    def show_tag_cloud(self):
        """
        task to show tag cloud
        please see the output folder for more information
        :return:
        """
        try:
            logging.info("Word Cloud")

            wc = WordCloud(
                background_color='white',
                stopwords=set(stopwords.words('english')),
                height=1000,
                width=1000
            )
            random_10_project = self.dataframe['preprocessed'].sample(n=10)
            text = (' '.join(random_10_project.map(str))).replace('\'', '')
            wc.generate(text)
            wc.to_file('output/wc.png')

        except Exception as e:
            print("Error: can not show the show the cloud of words ")
            print(e)
