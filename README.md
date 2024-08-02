# AsyncIO Projects Repository

Welcome to the AsyncIO Projects Repository! This repository contains a collection of projects and examples demonstrating the use of Python's `asyncio` library for asynchronous I/O operations.

## Introduction

Asynchronous I/O (Input/Output) enables your program to handle other tasks while waiting for I/O operations to complete. Python's `asyncio` library provides a framework to write concurrent code using the `async` and `await` keywords. This repository showcases various projects that leverage `asyncio` to perform asynchronous tasks, ranging from web scraping to network communication.

## Requirements

To run the projects in this repository, you need the following requirements:

- Python 3.11 or higher
- `asyncio` library (built-in with Python 3.7+)
- Additional dependencies as specified in each project's `requirements.txt`

## Installation

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/hosseinabadii/asyncio
   cd asyncio
   ```

2. Set up a virtual environment (optional but recommended):

   ```sh
   python3 -m venv env
   source env/bin/activate    # MacOS/Linux
   .\env\Scripts\activate     # Windows
   ```

3. Install the required dependencies for each project:

   ```sh
   pip install -r requirements.txt
   ```

## Project List

1. **Gather vs TaskGroup**
2. **Convert Blocking Function to Async**
3. **Pokemon API**
4. **IOT Example**

### Example Code Snippet

Here is a small example showing how to use `asyncio` to run async tasks:

```python
import asyncio

async def say_hello():
    print("Hello, world!")
    await asyncio.sleep(1)
    print("Hello again!")

async def main():
    await asyncio.gather(say_hello(), say_hello())

if __name__ == "__main__":
    asyncio.run(main())
```

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
