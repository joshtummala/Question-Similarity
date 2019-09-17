from bert_serving.client import BertClient

embedding = BertEmbeddings()
s1 = 'i am sitting on a river bank'
s2 = 'i am going to rob a bank'

s1 = embedding.embed(s1)
s2 = embedding.embed(s2)
print(s1)
print(s2)