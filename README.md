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

   To run the web scraper and save JSON files, use the following script:

   ```
   python script.py <link to the docs>
   ```
   Alternatively, you can also use the streamlit GUI to crawl webpages.

<br>

4. **Start Streamlit GUI**:

   To start the GUI use the following CMD:

    ```
   streamlit run streamlit_app.py
   ```

<br>

5. **Process Docs**:

   To generate the vector DB from crawled links use the process documents button from the Streamlit GUI:
   ![image](https://github.com/kshitijagrwl/chat-with-docs/assets/74452705/a120c669-c8d9-4556-a10d-1533a120b342)


<br>

6. **Search the Database**:

   To perform a search query on the initialized database, use search button on GUI:

   ![image](https://github.com/kshitijagrwl/chat-with-docs/assets/74452705/c0e39e2c-ac38-488c-a701-53db52312029)


<br>

7. **Docker Support (Coming Soon)**:
   We are actively working on providing a Dockerized version of Chat with Your Docs to simplify the installation process. With Docker support, you'll be able to set up and run Chat with Your Docs in a containerized environment, making it easy to deploy and manage.

   Stay tuned for updates, and we will soon release instructions on how to install and run the application using Docker.

## Integration with LangChain Agents (Coming Soon)

We're excited to announce that we are actively working on integrating Chat with Docs with LangChain Agents, a cutting-edge technology that will take your documentation interaction to the next level. This integration will bring a new dimension of conversational AI to your document exploration.

With LangChain Agents integration, Chat with Docs will be able to engage in dynamic and context-rich conversations. You'll be able to ask questions, seek clarifications, and receive comprehensive answers in a more natural and interactive manner.

Here's a glimpse of what you can expect:

- **Conversational Depth:** LangChain Agents will empower Chat with Docs to hold conversations that go beyond simple queries. You'll be able to have back-and-forths that simulate human-like interactions.

- **Contextual Understanding:** The integration will enable Chat with Docs to better understand the context of your queries. It will remember previous interactions and provide more relevant responses based on the ongoing conversation.

- **Real-time Adaptation:** LangChain Agents will allow Chat with Docs to adapt to changes in your questions and provide nuanced responses in real time, resulting in a more dynamic and informative experience.

We're dedicated to delivering an integration that seamlessly combines the power of LangChain Agents with Chat with Docs, providing you with a sophisticated tool to explore and comprehend your documentation effortlessly.

Stay tuned for updates as we finalize the integration and roll it out to users. We're committed to enhancing your documentation interaction through this exciting advancement.


## Integration with OpenAI

We have added support for OpenAI in the Chat with Docs project, allowing you to enhance your documentation queries using advanced natural language processing models (Currently using gpt-3.5-turbo). To take advantage of this feature, follow these steps:

1. **Provide OpenAI Key:**
   In the Streamlit interface, enter your OpenAI key. This is required to enable the integration with OpenAI's natural language processing models.

2. **Enhanced Search Results:**
   With OpenAI integration, Chat with Docs will use advanced natural language processing models to enhance your search results. It will offer context-aware answers and better understand complex queries.

3. **Seamless User Experience:**
   The integration aims to deliver a seamless user experience, making your interactions with documentation even more productive and insightful.

Stay tuned for further updates as we finalize the integration and make it available to users. We are committed to delivering a cutting-edge solution that simplifies your documentation exploration.


## Contributing

We welcome contributions to improve and enhance Chat with Your Docs. If you would like to contribute, please follow our guidelines for [contributing](CONTRIBUTING.md), and don't forget to read our [code of conduct](CODE_OF_CONDUCT.md).

## Issues

If you encounter any issues while using Chat with Your Docs or have any feature requests, please report them on our GitHub Issues page. We appreciate your feedback and will work diligently to address any problems.

## License

Chat with Your Docs is licensed under the [MIT License](LICENSE).
