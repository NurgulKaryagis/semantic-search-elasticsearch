# Semantic Search with Elasticsearch

Semantic Search with Elasticsearch is a project designed to perform semantic search operations on textual data using Elasticsearch and Sentence Transformers. This system enhances search capabilities by transforming texts into vector embeddings and querying these embeddings within Elasticsearch.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.8 or higher
- Elasticsearch 7.x
- Pipenv or any Python virtual environment tool

### Installation

1. **Clone the Repository**
   
   ```bash
   git clone https://github.com/NurgulKaryagis/semantic-search-elasticsearch.git
   cd semantic-search-elasticsearch
   ```

2. **Set Up Python Environment**
   
   ```bash
   pipenv install
   ```

   Or using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Elasticsearch Configuration**

   Ensure that Elasticsearch is running on your local machine, or adjust the Elasticsearch configuration in the code to point to your Elasticsearch instance.

4. **Download the Data**

   Download the dataset used for this project from the Hugging Face dataset repository:

   [Mini BioASQ dataset](https://huggingface.co/datasets/rag-datasets/mini-bioasq/tree/main/data)

   Place the downloaded data in a directory accessible by the project.

### Usage

To use the system, follow these steps:

1. **Start Elasticsearch**

   Make sure your Elasticsearch server is up and running.

2. **Run the Application**

   Activate your virtual environment and execute the main script:

   ```bash
   python main.py --mode [mode] --data_path [path_to_data] --index_name [index_name]
   ```

   Replace `[mode]` with `upload_es`, `search`, `create_index`, or `delete_index` depending on what operation you want to perform. Specify the appropriate `[path_to_data]` and `[index_name]`.

### Available Commands

- **upload_es**: Uploads data to Elasticsearch, converting text to embeddings before uploading.
- **search**: Performs a search operation using a query transformed into embeddings.
- **create_index**: Creates an Elasticsearch index suitable for storing vector embeddings.
- **delete_index**: Deletes a specified Elasticsearch index.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, suggest features, or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

