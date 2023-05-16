from textblob import TextBlob
y=input ("Type Your Sentence: ")
edu=TextBlob(y)
x=edu.sentiment.polarity
#negative=x<0 and Neutral=0 and positive=x>0 && x<=1
if x<0:
    print('Negative')
elif x==0:
    print('Neutral')
elif x>0:
    print('Positive')
elif x<=1:
    print('Positive')



