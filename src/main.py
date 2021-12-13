"""
@Author: Qadir Mughal

NOTE: main Evacuating file
"""

import os
import sys
import nltk
import ssl
from FileHandler import FileHandler
from TextProcessing import TextProcessing
import warnings

"""
this is only for when nltk refuse to connect with http connection 
solution is directly copied form stackoverflow link is as follows:
https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed
thanks to @ishwardgret [https://stackoverflow.com/users/2275439/ishwardgret]
"""
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
"""------------------- until this ----------------"""

warnings.simplefilter('ignore')
nltk.download('wordnet')
nltk.download('stopwords')

# only needed for some operating system
os.chdir(sys.path[0])

if __name__ == '__main__':
    file = FileHandler('../csv/project.csv', ';')
    df = file.file_reading_by_dataframe()
    df = df.drop_duplicates()
    lda = TextProcessing(df)
    lda.build_with_save_html('objective', 30)
    lda.show_topic_visual()
    lda.show_tag_cloud()
