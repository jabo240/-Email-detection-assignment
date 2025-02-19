# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_G9sYebhIjX7S971jSQOscG73YGoG1aU
"""

import pandas as pd

phishing_keywords = ["urgent", "password reset", "bank", "verify", "account suspended"]



emails = pd.read_csv("/content/2401000260.csv")


if 'content' in emails.columns:

    emails["is_phishing"] = emails["content"].apply(
        lambda x: any(keyword in str(x).lower() for keyword in phishing_keywords)
    )



    emails.to_csv("/content/analyzed_emails.csv", index=False)
    print("Phishing detection complete. ✅")
else:
    print("Error: The 'content' column is missing from the dataset.")


text1 = "This is a sample sample  text about is this legal sample issues."
text2 = "This text legal  discusses legal and ethical This issues in legal computing."


similarity, common_words = jaccard similarity(text1, text2)