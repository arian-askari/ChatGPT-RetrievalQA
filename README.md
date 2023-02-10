# ChatGPT-RetrievalQA
A dataset for training Question Answering Retrieval models on ChatGPT responses and evaluation on human responses

### Answer ranking dataset

This dataset is based on the public HC3 dataset [1], although our experimental setup and evaluation will be quite different.
We will use a different set of test queries and we will use relevance judges to evaluate the quality of answer ranking retrieval.

| Description                                           | Filename                                                                                                                | File size |                        Num Records | Format                                                         |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------:|-----------------------------------:|----------------------------------------------------------------|
| Collection-H (Human Responses)                                | [collection.tar.gz](https://dropbox.com/collection.tar.gz)                             |    X MB |                         58,546  | tsv: pid, passage |
| Collection-C (ChatGPT Responses)                                | [collection.tar.gz](https://dropbox.com/collection.tar.gz)                             |    X GB |                         xxx,yyy,zzz  | tsv: pid, passage |
| Queries                                   | [queries.tar.gz](https://dropbox.com/msmarcoranking/queries.tar.gz)                                   |   42.0 MB |                         xxx,yyy,zzz  | tsv: qid, query |
| Qrels-H Train (Human Responses)                                | [qrels.test.tsv](https://dropbox.com/msmarcoranking/qrels.dev.tsv)                                     |    1.1 MB |                            xxx,yyy,zzz  | TREC qrels format |
| Qrels-H Validation (Human Responses)                              | [qrels.train.tsv](https://dropbox.com/msmarcoranking/qrels.train.tsv)                                 |   10.1 MB |                           xxx,yyy,zzz  | TREC qrels format |
| Qrels-H Test (Human Responses)                              | [qrels.train.tsv](https://dropbox.com/msmarcoranking/qrels.train.tsv)                                 |   X MB |                           xxx,yyy,zzz  | TREC qrels format |
| Qrels-C Train (ChatGPT Responses)                                 | [qrels.test.tsv](https://dropbox.com/msmarcoranking/qrels.dev.tsv)                                     |    1.1 MB |                            xxx,yyy,zzz  | TREC qrels format |
| Qrels-C Validation (ChatGPT Responses)                              | [qrels.train.tsv](https://dropbox.com/msmarcoranking/qrels.train.tsv)                                 |   10.1 MB |                           xxx,yyy,zzz  | TREC qrels format |
| Qrels-C Test (ChatGPT Responses)                              | [qrels.train.tsv](https://dropbox.com/msmarcoranking/qrels.train.tsv)                                 |   X MB |                           xxx,yyy,zzz  | TREC qrels format |
| Queries, Answers, and Relevance   Labels | [collectionandqueries.tar.gz](https://dropbox.com/collectionandqueries.tar.gz)         |    X GB |                        xxx,yyy,zzz  | |
| Train Triples                       | [triples.train.small.tar.gz](https://dropbox.com/triples.train.tar.gz)           |  X GB |                        xxx,yyy,zzz  | tsv: query, positive passage, negative passage |
| Validation Triple                       | [triples.train.small.tar.gz](https://dropbox.com/triples.train.tar.gz)           |   X GB |                        xxx,yyy,zzz  | tsv: query, positive passage, negative passage |
| Train Triples QID PID Format               | [qidpidtriples.train.full.2.tsv.gz](https://dropbox.com/qidpidtriples.train.full.2.tsv.gz) |    5.7 GB |                       xxx,yyy,zzz  | tsv: qid, positive pid, negative pid |
| Top 1000 Train                            | [top1000.train.tar.gz](https://dropbox.com/top1000.train.tar.gz)                       |  175.0 GB |                       xxx,yyy,zzz  | tsv: qid, pid, query, passage |
| Top 1000 Validation                              | [top1000.dev.tar.gz](https://dropbox.com/top1000.dev.tar.gz)                           |    2.5 GB |                         xxx,yyy,zzz  | tsv: qid, pid, query, passage |
| Top 1000 Test                              | [top1000.test.tar.gz](https://dropbox.com/top1000.test.tar.gz)                           |    2.5 GB |                         xxx,yyy,zzz  | tsv: qid, pid, query, passage |

