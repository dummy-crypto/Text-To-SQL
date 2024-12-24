# Text-To-SQL

Text-To-SQL is a groundbreaking app that connects natural language with database queries. It allows users to retrieve data by transforming English sentences into SQL queries, making data manipulation and retrieval easier and more intuitive. This project not only simplifies the process of querying databases but also makes it more accessible for those with little to no knowledge of SQL.

Try the project : [ https://lnkd.in/ecJxqShg
](https://textsql-analysis.streamlit.app/)

Applications:

📊 Business Intelligence: Quickly extract insights from large datasets

📈 Data Analysis: Simplify querying and analyzing data for non-technical team members

Tech Stack used:
- NLP
- Generative AI
- Python
- SQL
- Data Manipulation
- Pandas

# Summary for install_dependencies python
### What it does:

Automates the setup of a development environment. Installs system packages, Python dependencies, and VSCode extensions. Runs a Streamlit app with specific settings.

### Limitations:

Does not handle containerization (Docker) or GitHub Codespaces setup. Cannot directly configure VSCode settings or themes. Limited to environments where Python and necessary tools (apt, pip, code) are already available.
Does not handle network and port forwarding tasks, which are typically managed by a containerization tool or cloud platform. If you're working in a local development environment or using a Docker-based container, this script will help you automate much of the setup. However, for more advanced setups like GitHub Codespaces or Dockerized containers, you'll still need additional configuration files like devcontainer.json




How It Works:
1. Load a CSV data file containing relational data.
2. Click the “Record” button and ask your question in plain English. For example, "Display the top 3 records" Alternatively, write your question in plain English and click the “Get SQL Query” button.
3. The app generates the corresponding SQL query, runs it on your CSV file, and provides the results instantly. The resulting CSV can be viewed or downloaded for further analysis.
