# Ghulam Qadir Mughal

I always enjoy modular and object-oriented ways to approach things in programming. If you have any Question, regarding
anything please don't hesitate to contact me. I tried not to over engineer the things, but my focus was to be able to
use this on a larger scale. I also restrict my self to only the questions those mentioned in the email.

Moreover, this research is only based on reading different article and try to produce the best results. as its type of
unsupervised learning (which word is belongs to which categories based on no labels). please follow the code for more
detail.
Data description
the file that i choose is  
project.CSV and after choosing i pick 2 columns from this file 1st is called title and 2nd is objecties because these are the full of text after worked on these files i got the expectional output:
text based output can be found in ROOT_DIR\src\output in the form of HTML display and also in CSV(contain preprossessed column which consist of important word for each prject) and wc.png(as a tag could PNG file output)
## UML Diagram

There are three files which consist of different classes for more detail please follow the below diagram

<p align="center">
    <img width="790" height="707" src="/architecture/umlDia.png" alt=""/>
</p>

## Requirements

* python 3.9 or >
* redistribution c++ 14 or greater build tools for only word cloud to run on windows operating system

## Get started

Let's get into it, to start lets have a look at the repo what included in it

### Structure of the Repo

1. architecture->consist of UML images of the application
2. csv -> csv for assessment
3. demo -> sample running app screenshot
4. src-> main repo for text processing, and main(main.py and Testing.py).
5. Readme.md ->
6. requirements.txt -> requirements for the python module

## App in action

please install the dependencies by this command, running from ROOT_DIR

```
pip install -r requirements.txt
```

please run the main.py file on command line or from IDE of your preference and follow the code for detail
(like which function is doing what)
How is it working? let's see...

1. main.py will pass the file to the FileHandler class
2. FileHandler will give bac pandas dataframe
3. then it will take care of the duplicates
4. running the model and saving the results into html file
5. showing the visual in browser of your choose
6. showing the tag cloud

## Further Improvements

would like to do more if I have more time

1. explore the LDA hyper-parameter tuning
2. further, preprocessing (need more reading how can I achieve that)
3. test on other unsupervised learning algorithms
4. finding the accuracy and improving it
5. needed to be done more testing

## Expected results

Screenshots are available in ```ROOT_DIR/demo``` directory

## Task Time Analysis

1. API Review -> 30min
2. Research and reading -> 2 hour
3. Preparing the skeleton directory -> 30min
4. Coding -> 1 hour
5. Readme -> 1 hour
6. Screenshot and demo -> 30 min
7. Architecture diagrams -> 20min

# Task

Hi Ghulam,

thanks for applying at Chainstep! We’d love to get to know you better – and your coding style.

Please try solving the following task by building a Jupyter notebook or self-contained python script including the setup
for a conda environment, and send us the link to your repository.

1. Download and extract https://cordis.europa.eu/data/cordis-h2020projects-csv.zip
2. Create a script that extracts the most important topics for each project from the csv
3. Create and show a tag cloud for a randomly selected 10 projects
4. Give us some ideas how you would process this data further, and try out one of them. Our goal is showing a concise
   preview that helps understand at one glance what the project is about.

We are interested in understanding your way of working, so we prefer a good version history over seeing the finished
product only. Please keep it simple, we don’t expect you to add features beyond what was described above, we are more
interested in your design decisions and rationale.

Feel free to use https://github.com/lisanka93/text_analysis_python_101/blob/master/Dummy%20movie%20dataset.ipynb as a
starting point – but if you have a better idea how to start, we would love to learn from you.

Have fun and let us know if you have any questions.

Best regards Surabhi
