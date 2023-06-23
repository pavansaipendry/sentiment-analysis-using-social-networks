Sentiment-analysis-using-social-networks
The project finds the emotion in the given text. It takes input in a text/sentence format through the User or through Twitter API.

NLP Emotion Algorithm
 1) Check if the word in the final word list is also present in emotion.txt
  - open the emotion file
  - Loop through each line and clear it
  - Extract the word and emotion using split
 2) If word is present -> Add the emotion to emotion_list
 3) Finally count each emotion in the emotion list
Or there is another way of taking input. Here we have to mention the TwitterID and then it collects data and cleans it. Then does the same job as above.

