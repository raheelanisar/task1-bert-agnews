# task1-bert-agnews
# BERT AG News Classification

## Project Overview
This project performs text classification on the AG News dataset using the BERT (Bidirectional Encoder Representations from Transformers) model from Hugging Face Transformers.

The model classifies news articles into four categories:
- World
- Sports
- Business
- Science & Technology

## Features
- Data preprocessing
- BERT tokenizer
- Fine-tuning BERT model
- Model evaluation
- Accuracy calculation
- Save trained model
- Predict custom news articles

## Project Structure

```
task1-bert-agnews/
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── models/
│   └── bert_agnews_model/
│
├── outputs/
│
├── BERT_AGNews.py
├── BERT_AGNews.ipynb
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Required Libraries

- pandas
- numpy
- torch
- transformers
- datasets
- scikit-learn

## Run

```bash
python BERT_AGNews.py
```
<img width="638" height="315" alt="image" src="https://github.com/user-attachments/assets/9106fb3c-ca5f-4cbc-9ca3-def67eb088c1" />
<img width="640" height="314" alt="image" src="https://github.com/user-attachments/assets/6b57c65c-9045-45b5-b3c4-4306bf351f20" />
<img width="640" height="319" alt="image" src="https://github.com/user-attachments/assets/f6ab83c2-2cb9-449f-b6ca-f404e3ad5fad" />
<img width="640" height="321" alt="image" src="https://github.com/user-attachments/assets/000e88b3-2343-4022-ae70-40609e2f30b7" />
<img width="636" height="319" alt="image" src="https://github.com/user-attachments/assets/0a50affa-6503-4f10-8d9d-e47ef14a41b5" />
<img width="640" height="317" alt="image" src="https://github.com/user-attachments/assets/332b6be3-3c38-401a-b9b5-88165620b590" />
<img width="640" height="317" alt="image" src="https://github.com/user-attachments/assets/89643870-b117-4ca1-bdf7-151fb19ee126" />


Or open:

```
BERT_AGNews.ipynb
```

in Jupyter Notebook.

## Model

- Model: bert-base-uncased
- Dataset: AG News
- Framework: PyTorch
- Library: Hugging Face Transformers

## Results

The trained BERT model achieves high accuracy on the AG News classification dataset after fine-tuning.

## Author

**Raheela Nisar**

BS Computer Science

DevelopersHub Corporation

AI/ML Engineering Internship

## License

This project is created for educational and internship purposes.
