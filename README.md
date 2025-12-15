This project focuses on data preprocessing for Market Basket Analysis using a grocery dataset.
The goal is to clean, transform, and prepare transaction data so it can be used for association rule mining and machine learning models.

Market Basket Analysis helps us understand which items are frequently bought together.

📂 Dataset Used

Dataset Name: Groceries_dataset.csv

Dataset Description:

Contains grocery purchase transactions

Each row represents items bought in a single transaction

Used widely for association rule learning problems

🛠️ Technologies & Libraries Used

Python

Pandas – data manipulation

NumPy – numerical operations

ast – converting string data to list format

mlxtend – transaction encoder

scikit-learn

CountVectorizer

TruncatedSVD

joblib – saving processed models/data

🔄 Steps Performed in Data Preprocessing
1️⃣ Import Required Libraries

All necessary Python libraries for data handling, encoding, and dimensionality reduction are imported.

2️⃣ Load the Dataset

The grocery dataset is loaded using Pandas and basic inspection is performed.

df = pd.read_csv("Groceries_dataset.csv")

3️⃣ Data Cleaning

Checked for missing values

Ensured transaction data is in the correct format

Converted string-based item lists into Python lists

4️⃣ Transaction Encoding

Grocery items are converted into binary format

Each column represents an item

Values indicate presence (1) or absence (0)

This format is required for:

Association rule mining

Machine learning algorithms

5️⃣ Feature Extraction

Used CountVectorizer to convert item lists into a numerical matrix

Helps machine learning models understand item frequency

6️⃣ Dimensionality Reduction

Applied Truncated SVD

Reduces large feature space

Improves performance and efficiency

7️⃣ Saving Processed Data

Processed objects and models are saved using joblib

Allows reuse without repeating preprocessing steps
