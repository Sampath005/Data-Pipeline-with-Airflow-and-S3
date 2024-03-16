# Data Pipeline with Airflow and S3

## Objective
The objective of this project is to automate the process of downloading a dataset from Kaggle, performing any necessary data transformations, and uploading the processed dataset to Amazon S3. This entire process will be orchestrated and scheduled using Apache Airflow.

## Architecture Diagram
![Architecture Diagram](https://github.com/Sampath005/Data-Pipeline-with-Airflow-and-S3/assets/97429122/4175d98d-c07d-4958-ac95-5a3196bb87b7)

## Pipeline Steps
1. **Download Dataset:** Airflow task to download the dataset from Kaggle using the Kaggle API.
2. **Data Transformation (Optional):** Task for cleaning or processing the dataset.
3. **Upload to S3:** Task to upload the processed dataset to Amazon S3 using Boto3.

## Usage
1. Clone the repository: `git clone https://github.com/Sampath005/Data-Pipeline-with-Airflow-and-S3.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your Kaggle API credentials and AWS credentials (if not already done).
4. Update the Airflow DAG (`pipeline.py`) with your specific dataset and S3 bucket details.
5. Start Airflow webserver: `airflow webserver`
6. Start Airflow scheduler: `airflow scheduler`
7. Access Airflow UI in your browser and trigger the DAG to run.
