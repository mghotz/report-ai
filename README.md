# LangChain Chat Application

This LangChain chat application integrates a conversational AI interface with a SQLite database, enabling users to interact with and query database information through natural language. The application leverages OpenAI's powerful models, along with custom tooling for database interaction and report generation, to provide a seamless user experience.

## Features

- **Natural Language Database Queries**: Users can ask questions about the data stored in the SQLite database in natural language.
- **Dynamic Report Generation**: The application can generate HTML reports based on user queries, summarizing data insights.
- **Extensible Framework**: Built on the LangChain library, the app can be extended with additional tools and functionalities as needed.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- Pip for installing Python packages

## Setup

### Environment Variables

You need to create a `.env` file in the root directory of the application and add the following environment variable:

OPENAI_API_KEY=your_openai_api_key_here

markdown
Copy code

Replace `your_openai_api_key_here` with your actual OpenAI API key.

### Installation

1. Clone the repository to your local machine.
2. Navigate to the application directory.
3. Install the required Python packages:

```bash
pip install -r requirements.txt
Running the Application
To start the application, run:

bash
Copy code
python main.py
Once the application is running, follow the on-screen prompts to interact with the chat interface.

Usage
After launching the app, you will be prompted to enter your queries. Here are some example queries you can start with:

"How many orders are there? Write the result to an HTML report."
"Repeat the exact same process for users."
The application supports natural language queries related to the data in the SQLite database, so feel free to experiment with different questions.

Contributing
Contributions to the application are welcome! Please feel free to fork the repository, make changes, and submit pull requests.
