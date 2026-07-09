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
