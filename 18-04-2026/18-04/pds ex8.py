sentence = "python is easy and python is powerful"
sent=sentence.split()
from collections import Counter
print(Counter(sent))
sent_count={}
for sent in sent:
    if sent not in sent_count:
        sent_count[sent]=1
    else:
        sent_count[sent]+=1
print(sent_count)