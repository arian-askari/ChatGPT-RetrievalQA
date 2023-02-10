# ChatGPT-RetrievalQA
A dataset for training/evaluating Question Answering Retrieval models on ChatGPT responses with the possibility to training/evaluating on real human responses.

### Answer ranking dataset

This dataset is based on the public HC3 dataset [1], although our experimental setup and evaluation will be quite different.
We will use a different set of test queries and we will use relevance judges to evaluate the quality of answer ranking retrieval.

| Description                                           | Filename                                                                                                                | File size |                        Num Records | Format                                                         |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------:|-----------------------------------:|----------------------------------------------------------------|
| Collection-H (H: Human Responses)                                | [collection_h.tsv](https://drive.google.com/file/d/1M5ZN-5CSnp6fL7u0EgtUjcyjrWQwqiJZ/view?usp=share_link)                             |   38.6 MB |                         58,546  | tsv: pid, passage |
| Collection-C (C: ChatGPT Responses)                                | [collection_c.tsv](https://drive.google.com/file/d/1-8LI4WLPI3ExDz24vLMJ71am4imzflYn/view?usp=share_link)                             |    26.2 MB |                         26,903  | tsv: pid, passage |
| Queries                                   | [queries.tsv](https://drive.google.com/file/d/1-9H60KOBVy6vRvkaIMySUKGXV8A45Ygp/view?usp=share_link)                                   |   4 MB |                         24,322  | tsv: qid, query |
| Qrels-H Train (Train set Qrels for Human Responses)                                | [qrels_h_train.tsv](https://drive.google.com/file/d/1-9gu7BhdeRewU7i5ClcTgEbkb2tIUR9x/view?usp=share_link)                                     |    724 KB |                            40,406 | TREC qrels format |
| Qrels-H Validation (Validation set Qrels for Human Responses)                              | [qrels_h_valid.tsv](https://drive.google.com/file/d/1-JH0b37WFL8V-KhDUYShiGcidGArUodZ/view?usp=share_link)                                 |   29 KB |                           1,460  | TREC qrels format |
| Qrels-H Test (Test set Qrels for Human Responses)                              | [qrels_h_test.tsv](https://drive.google.com/file/d/1-IJEzHUJFVoELAuT68k0otFKN4QyZua0/view?usp=share_link)                                 |   326 KB |                           16,680  | TREC qrels format |
| Qrels-C Train (Train set Qrels for ChatGPT Responses)                                 | [qrels_c_train.tsv](https://drive.google.com/file/d/1-Kllea1-oP3LoS98TU5WAHJ3SyALav-g/view?usp=share_link)                                     |    339 KB |                            18,465  | TREC qrels format |
| Qrels-C Validation (Validation set Qrels for ChatGPT Responses)                              | [qrels_c_valid.tsv](https://drive.google.com/file/d/1-S0tA7_B_vqjU3AGG2I1QTu-WaQ_9O0X/view?usp=share_link)                                 |   13 KB |                           672  | TREC qrels format |
| Qrels-C Test (Test set Qrels for ChatGPT Responses)                              | [qrels_c_test.tsv](https://drive.google.com/file/d/1-UC8sq8mKTvUxnyZCZljMQ1JCI-iYFRp/view?usp=share_link)                                 |   152 KB |                           7,766  | TREC qrels format |
| Queries, Answers, and Relevance   Labels | [collectionandqueries.zip](https://drive.google.com/file/d/1-VDhikUVr6k0ZRRArGruazQuCMPtk-mT/view?usp=share_link)         |    24 MB |                        866,548  | |
| Train-H Triples                       | [triples.train.small.tar.gz](https://drive.google.com/file/d/1-7Im-U8RG7XvWW9QxOfERFii69S8clJ5/view?usp=share_link)           |  58.68 GB |                        40,641,772  | tsv: query, positive passage, negative passage |
| Validation-H Triple                       | [triples.train.small.tar.gz](https://drive.google.com/file/d/1-PnmO8fG_HgcBeWS5Akf9tc67VFyMQWz/view?usp=share_link)           |   2.02 GB |                        1,468,526  | tsv: query, positive passage, negative passage |
| Train-H Triples QID PID Format               | [train_h_qidpidtriples.tsv](https://drive.google.com/file/d/1-G3GCx50PnwF4LaZAHcHkmcmBpe81j5i/view?usp=share_link) |    921.7 MB |                       40,641,772  | tsv: qid, positive pid, negative pid |
| Validation-H Triples QID PID Format               | [valid_h_qidpidtriples.tsv](https://drive.google.com/file/d/1-SITWpMrKGDW7RZiXjntJjKa7gcRpSHB/view?usp=share_link) |    X GB |                       1,468,526  | tsv: qid, positive pid, negative pid |
| Train-C Triples                       | [triples.train.small.tar.gz](https://dropbox.com/triples.train.tar.gz)           |  X GB |                        xxx,yyy,zzz  | tsv: query, positive passage, negative passage |
| Validation-C Triple                       | [triples.train.small.tar.gz](https://dropbox.com/triples.train.tar.gz)           |   X GB |                        xxx,yyy,zzz  | tsv: query, positive passage, negative passage |
| Train-C Triples QID PID Format               | [qidpidtriples.train.full.2.tsv.gz](https://dropbox.com/qidpidtriples.train.full.2.tsv.gz) |    X GB |                       xxx,yyy,zzz  | tsv: qid, positive pid, negative pid |
| Validation-C Triples QID PID Format               | [qidpidtriples.train.full.2.tsv.gz](https://dropbox.com/qidpidtriples.train.full.2.tsv.gz) |    X GB |                       xxx,yyy,zzz  | tsv: qid, positive pid, negative pid |


P.S: Given each query and positive answer, 1000 negative answers have been sampled randomly.


### Answer re-anking dataset (comming soon)
| Description                                           | Filename                                                                                                                | File size |                        Num Records | Format                                                         |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------:|-----------------------------------:|----------------------------------------------------------------|
| Top-H 1000 Train                            | [top1000.train.tar.gz](https://dropbox.com/top1000.train.tar.gz)                       |  xxx GB |                       xxx,yyy,zzz  | tsv: qid, pid, query, passage |
| Top-H 1000 Validation                              | [top1000.dev.tar.gz](https://dropbox.com/top1000.dev.tar.gz)                           |    xxx GB |                         xxx,yyy,zzz  | tsv: qid, pid, query, passage |
| Top-H 1000 Test                              | [top1000.test.tar.gz](https://dropbox.com/top1000.test.tar.gz)                           |    xxx GB |                         xxx,yyy,zzz  | tsv: qid, pid, query, passage |
| Top-C 1000 Train                            | [top1000.train.tar.gz](https://dropbox.com/top1000.train.tar.gz)                       |  xxx GB |                       xxx,yyy,zzz  | tsv: qid, pid, query, passage |
| Top-C 1000 Validation                              | [top1000.dev.tar.gz](https://dropbox.com/top1000.dev.tar.gz)                           |   xxx GB |                         xxx,yyy,zzz  | tsv: qid, pid, query, passage |
| Top-C 1000 Test                              | [top1000.test.tar.gz](https://dropbox.com/top1000.test.tar.gz)                           |    xxx GB |                         xxx,yyy,zzz  | tsv: qid, pid, query, passage |


## Code for creating the dataset
[ChatGPT-RetrievalQA-Dataset-Creator](https://colab.research.google.com/drive/1OK8H_SYUD7n_LKTNj33kANP4t2fLcmGt?usp=sharing)

## Dataset source and copyright
Special thanks to the [HC3 team](https://github.com/Hello-SimpleAI/chatgpt-comparison-detection) for releasing Human ChatGPT Comparison Corpus (HC3) corpus. Our data is created based on their dataset and follows the license of them.

