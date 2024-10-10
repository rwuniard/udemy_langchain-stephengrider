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

6. **Manage Environment Variables and Handle Anaconda Conflicts**  
   If you make any changes to your environment variables or keys, you may need to exit the shell and re-enter using the `pipenv shell` command.  
   **Important**: Anaconda users may find that Pipenv conflicts with their environment. Please deactivate your conda environment if you find this to be true.
