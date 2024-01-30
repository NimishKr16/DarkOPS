# Fake Review Detection

## Overview

This repository contains the code and resources for a Fake Review Detection project. The primary objective of this project is to identify fake reviews using a RoBERTa (Robustly optimized BERT approach) model, which has proven to be highly effective in natural language processing tasks.

## Model and Training

We leveraged the RoBERTa model, an advanced version of BERT, to train our fake review detection system. The model was trained on a dataset obtained from the Open Science Framework (OSF). The training process resulted in impressive performance metrics, showcasing the model's capability in discerning between genuine and fake reviews.

### Performance Metrics

- **Accuracy:** 94.00%
- **Precision:** 91.75%
- **Recall:** 95.76%

#### Classification Report:
|            | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| CG         | 0.95      | 0.91   | 0.93     | 4010    |
| OR         | 0.92      | 0.96   | 0.94     | 4077    |
| Accuracy   |           |        | 0.94     | 8087    |
| Macro Avg  | 0.94      | 0.94   | 0.94     | 8087    |
| Weighted Avg | 0.94    | 0.94   | 0.94     | 8087    |



## Repository Structure

- `data/`: Includes the dataset obtained from OSF.
- `results/`: Holds the results of the model, such as performance metrics and classification reports.
- `notebooks/`: Jupyter notebooks used for data exploration, model training, and evaluation.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository: `git clone https://github.com/NimishKr16/Fake-Review-Detection.git`
2. Navigate to the project directory: `cd Fake-Review-Detection`
3. Explore the Jupyter notebooks in the `notebooks/` directory to understand the data and model training process.

## Results and Evaluation

For a detailed analysis of the model's performance, refer to the files in the `results/` directory. The classification report and metrics provide insights into the model's precision, recall, and accuracy.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to reach out if you have any questions or feedback!
