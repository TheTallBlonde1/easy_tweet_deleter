import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from distutils.core import setup
setup(
  name = 'easy_tweet_deleter',
  packages = ['easy_tweet_deleter'],
  version = '0.0.1',
  license='MIT',
  description = 'A simple app to delete tweets',
    long_description=long_description,
    long_description_content_type="text/markdown",
  author = 'Stefan Selby',
  author_email = 'stefanselby@gmail.com', 
  url = 'https://github.com/TheTallBlonde1/easy_tweet_deleter', 
  download_url = 'https://github.com/TheTallBlonde1/easy_tweet_deleter/archive/v_0_0_1.tar.gz',    # I explain this later on
  keywords = ['DELETE', 'TWEETS', 'TWITTER'],
  install_requires=[
    'python-twitter',
    'GetOldTweets3'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ]
)