# Chatbot

This is a chatbot application built with [Chainlit](https://chainlit.io), [LiteLLM](https://litellm.ai), and [Gemini](https://ai.google.dev/).

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (optional, but recommended for faster dependency management)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/chatbot.git
    cd chatbot
    ```

2.  **Create a virtual environment and install dependencies:**

    Using `uv`:
    ```bash
    uv venv
    source .venv/bin/activate # On Windows use `.venv\Scripts\activate`
    uv pip install .
    ```

    Using `pip`:
    ```bash
    python -m venv .venv
    source .venv/bin/activate # On Windows use `.venv\Scripts\activate`
    pip install .
    ```

3.  **Set up your environment variables:**

    Create a file named `.env` in the root of the project and add your Gemini API key:

    ```
    GEMINI_API_KEY="your-gemini-api-key"
    ```

## Usage

To start the chatbot, run the following command in your terminal:

```bash
chainlit run main.py -w
```

This will start the Chainlit server, and you can interact with the chatbot in your browser. The `-w` flag enables auto-reloading, so the server will restart automatically when you make changes to the code.

## How It Works

-   **`main.py`**: This is the main entry point of the application. It uses Chainlit to create the chat interface and handles the conversation logic.
-   **`litellm`**: This library is used to interact with the Gemini language model. It provides a simple and consistent API for calling different LLMs.
-   **`.env`**: This file stores your `GEMINI_API_KEY` securely.
-   **`chainlit.md`**: This file is used to display additional information or documentation within the Chainlit interface.
