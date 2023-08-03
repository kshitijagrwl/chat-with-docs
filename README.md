# Chat with Your Docs

Chat with Your Docs is a powerful tool that enables you to engage in interactive conversations with your preferred documentation. This project aims to facilitate easy communication with your documentation, making it more accessible and user-friendly. With Chat with Your Docs, you can seamlessly search for information, ask questions, and receive relevant answers from your chosen documentation.

## Usage

To use Chat with Your Docs, follow these simple steps:

1. **Start the Server**:

   To run the server, execute the `server.py` file using the following command:

   ```bash
   uvicorn server:app --host 0.0.0.0 --port 8000 --workers 1
   ```

   This will start the FastAPI server, which will be accessible on `http://localhost:8000` or `http://your-server-ip:8000` depending on your configuration.

   <br>

2. **Check Server Status**:

   After starting the server, you can verify if it's running fine by visiting the root endpoint:

   ```
   GET /
   ```

   The response should be:
   ```
   {"status": "Server is running fine!"}
   ```

<br>

3. **Run the Web Scraper**:

   To run the web scraper and save JSON files, use the following endpoint:

   ```
   GET /getLinks?start_url=<start_url>&allowed_domain=<allowed_domain>&max_depth=<max_depth>
   ```

   - `start_url`: The URL to start crawling from.
   - `allowed_domain`: The allowed domain to restrict crawling to.
   - `max_depth` (optional): The maximum depth for crawling (default is 2).

<br>

4. **Generate Full Text**:

   To generate the full text from the saved JSON files, use the following endpoint:

   ```
   GET /getText?path=<path_to_json_file>
   ```

   - `path` (optional): The path to the JSON file containing the links (default is "output_links.json").

<br>

5. **Initialize the Database** (We are currently using chromadb with all-MiniLM-L6-v2 embeddings):

   To initialize the database with the generated full text, use the following endpoint:

   ```
   GET /initializeDB
   ```

<br>

6. **Search the Database**:

   To perform a search query on the initialized database, use the following endpoint:

   ```
   GET /search?query=<your_query>&model_name=<model_name>
   ```

   - `query`: The search query you want to perform.
   - `model_name` (optional): The name of the model to use for the search (default is "all-MiniLM-L6-v2").

Remember to replace `<start_url>`, `<allowed_domain>`, `<max_depth>`, `<path_to_json_file>`, `<your_query>`, and `<model_name>` with appropriate values for your use case.

<br>

7. **Docker Support (Coming Soon)**:
   We are actively working on providing a Dockerized version of Chat with Your Docs to simplify the installation process. With Docker support, you'll be able to set up and run Chat with Your Docs in a containerized environment, making it easy to deploy and manage.

   Stay tuned for updates, and we will soon release instructions on how to install and run the application using Docker.

## Integration with OpenAI (Coming Soon)

We are actively working on integrating Chat with Your Docs with OpenAI, which will empower you to leverage the power of AI in your documentation queries. This integration will make your conversations even more insightful and efficient.

With OpenAI integration, Chat with Your Docs will use advanced natural language processing models to enhance your search results, offer context-aware answers, and better understand complex queries. The integration aims to deliver a seamless user experience and make your interactions with documentation even more productive.

Stay tuned for further updates as we finalize the integration and make it available to the users. We are committed to delivering a cutting-edge solution that simplifies your documentation exploration.

## Contributing

We welcome contributions to improve and enhance Chat with Your Docs. If you would like to contribute, please follow our guidelines for [contributing](CONTRIBUTING.md), and don't forget to read our [code of conduct](CODE_OF_CONDUCT.md).

## Issues

If you encounter any issues while using Chat with Your Docs or have any feature requests, please report them on our GitHub Issues page. We appreciate your feedback and will work diligently to address any problems.

## License

Chat with Your Docs is licensed under the [MIT License](LICENSE).
