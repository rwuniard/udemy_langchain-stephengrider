# OpenAI with Langchain

This README file provides instructions for setting up the environment to use OpenAI with Langchain. It includes steps for installing Python 3.11, setting up Pipenv, and configuring the Pipfile with necessary dependencies. The guide also covers how to create and enter a new environment using Pipenv, and provides tips for managing environment variables and handling potential conflicts with Anaconda.

## Key Steps

1. **Install Python 3.11**  
   First, you must have the 3.11 version of Python installed:  
   [Download Python 3.11](https://www.python.org/downloads/)  
   This is very important, as only a few versions of Python support LangChain and OpenAI.

2. **Install Pipenv**  
   In your terminal, run `pip install pipenv` or, depending on your environment, `pip3 install pipenv`.

3. **Create and Configure a Pipfile**

    - Create a `pycode` directory somewhere on your development machine if you haven't already.
    - Inside your `pycode` project directory, create a file called `Pipfile`.
    - Copy and paste the following code into the new `Pipfile`:

        ```toml
        [[source]]
        url = "https://pypi.org/simple"
        verify_ssl = true
        name = "pypi"

        [packages]
        langchain = "==0.0.352"
        openai = "==0.27.8"
        python-dotenv = "==1.0.0"

        [dev-packages]

        [requires]
        python_version = "3.11"
        ```

4. **Install Dependencies Using Pipenv**  
   Inside your `pycode` project directory, run the following command to install your dependencies from the Pipfile:

    ```sh
    pipenv install
    ```

5. **Create and Enter a New Environment with Pipenv**  
   Run the following command to create and enter a new environment:

    ```sh
    pipenv shell
    ```

    After doing this, your terminal will now be running commands in this new environment managed by Pipenv. Once inside this shell, you can run Python commands just as shown in the lecture videos, e.g.:

    ```sh
    python main.py
    ```

    When you run this multiple times, you will create duplicates embeddings inside the Chroma DB.
    The prompt.py will remove the duplicates since it uses the RedundantFilterRetriever class.

6. **ChromaDB to store vector values**  
   Run the following command to install ChromaDB:

    ```sh
    pip install chromadb
    ```

7. **tiktoken - tokenizer**  
   Run the following command to install tiktoken.
   tiktoken is a fast and efficient tokenizer library developed by OpenAI. It is designed to tokenize text into tokens, which are the smallest units of meaning in a language model.

    ```sh
    pip install tiktoken
    ```

## Usage

To use the Python script, follow these steps:

1. Ensure you have set up your environment and installed the dependencies as described above.
2. Go to https://platform.openai.com/settings/profile?tab=api-keys and find your api key
3. Create a `.env` file in the root directory of your project and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```
4. Run the Python script to generate vector values from facts.txt:

    ```sh
    python main.py
    ```

5. Run the Python script to prompt the user:

    ```sh
    python prompt.py
    ```

## Visualizing Embeddings

To visualize the embeddings:
If you are using Visual Studio Code or Cursor, please install Jupyter in the IDE

1. Ensure you have matplotlib installed:

    ```
    pip install matplotlib
    ```

2. Execute all cells in the notebook to generate the visualization.
   At the bottom of the jupyter notebook, you will see the grid that shows values to indicate how close each of the sentence to each other.
