# GPT Cacheable Response Service

This project utilizes the [GPT Cache library](https://github.com/zilliztech/GPTCache) to create a cacheable GPT-3 or GPT-4 response service with FastAPI, OpenAI API, Faiss, and SQLite. The GPT Cache library optimizes performance and reduces query costs by caching and reusing previous responses for similar queries. This implementation focuses on improving code readability, modularity, and application performance using local file caches.

## Features

- Leverage the GPT Cache library to optimize performance and reduce query costs
- Use FastAPI, OpenAI API, Faiss, and SQLite for a cacheable GPT-3 or GPT-4 response service
- Improve code readability and modularity by adopting best software development practices
- Use local file caches to enhance application performance
- Launch a beta version of the application with Docker support
- Easily deploy and manage the service using docker-compose

## Pre-requisites

- Python 3.8 or newer
- Docker and docker-compose installed

## Usage

1. Clone this repository:

```bash
git clone https://github.com/SelectCode/GPTCacheService.git
cd gpt-cacheable-response-service
```

2. Create a `.env` file in the project root directory with the following content:

```ini
OPENAI_API_KEY=your_openai_api_key_here
```

*Replace `your_openai_api_key_here` with your actual OpenAI API key.*

3. Build and run the project using Docker and docker-compose:

```bash
docker-compose build
docker-compose up -d
```

4. Visit `http://localhost:8000` in your browser to access the FastAPI documentation and interact with the API.

### API Endpoints

There are two main endpoints for query requests:

- `GET /query?prompt=<your_prompt_here>`
- `POST /query`

   ```json
   {
     "prompt": "your prompt here"
   }
   ```

Additionally, the root endpoint returns a simple greeting message:

- `GET /`



## Future Improvements

- Further expand API functionality by adding more endpoints and options
- Add support for other GPT models, not just GPT-3 and GPT-4
- Improve cache performance by exploring additional storage options, such as Redis or other distributed databases

## Credits

This project is built using the [GPT Cache library](https://github.com/zilliztech/GPTCache) as the main component for optimizing GPT queries and managing cached responses.

