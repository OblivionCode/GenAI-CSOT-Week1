# ChatAgent Submission

## Overview

For this assignment, I built a multi-turn chatbot using Python and the OpenRouter API.

The chatbot can hold conversations across multiple turns by storing previous messages in memory. I implemented the chatbot using a `ChatAgent` class to keep the code modular and configurable.

Initially, I created separate build files while experimenting with API calls and conversation history. Later, I extended the second build itself into the final working chatbot instead of creating a completely separate final build file.

---

## How I Implemented the Chatbot

I separated the project into two main files:

* `call_model.py`
* `chatbot.py`

The `call_model.py` file is responsible for interacting with OpenRouter and sending requests to the selected model.

The `chatbot.py` file contains the `ChatAgent` class, conversation loop, memory handling, and user commands.

I used a list called `messages` to store conversation history. Each message is stored as a dictionary containing:

* role
* content

Every time the user sends a message, the full conversation history is passed to the model so the chatbot can remember previous context.

---

## Model Selection

One thing I implemented beyond basic chatting was model selection.

Instead of hardcoding a single model, I added a menu that allows the user to choose from multiple models before starting the chatbot. This made the chatbot more flexible and aligned with the requirement of keeping it model-agnostic.

---

## Memory Management

To manage long conversations, I implemented a rolling memory buffer using the `compact_history()` function.

Initially, I considered storing the entire conversation permanently, but I realized that the message list would keep growing unnecessarily.

So I implemented a system that keeps only the latest conversation turns while preserving the system prompt.

I also added a manual `/compact` command so memory can be compacted anytime during the conversation.

---

## Problems I Faced

One major issue I faced was Python import errors.

At one point, my files had names like:

* `build 1.py`
* `build 2.py`

I later learned that Python module names cannot contain spaces, which caused import problems.

Another issue I faced was:

* wrong terminal directory
* unsaved files
* incorrect function arguments

For example, I received an error saying:

`call_model() takes 1 positional argument but 2 were given`

I fixed this by updating the function definition so it correctly accepted both:

* `messages`
* `model`

I also learned the importance of running the terminal inside the correct project folder.

---

## Things I Tried That Did Not Work

At one point, I removed model selection entirely and hardcoded a single model to simplify testing.

However, I later realized that the assignment checklist specifically required model selection, so I added it back.

I also experimented with different file structures before deciding to separate API logic and chatbot logic into different files.

---

## What I Learned

Through this assignment, I learned:

* how APIs are integrated into Python projects
* how conversation history works in chatbots
* how multi-turn memory is implemented
* how environment variables improve security
* how Python imports and project structure work

I also became more comfortable debugging runtime errors and terminal issues.

---

## Future Improvements

If I continue this project, I would like to add:

* streaming responses
* better summarization instead of deleting old messages
* saving chat history to files
* a graphical user interface
* voice input/output support

---

## Files Included

* `chatbot.py`
* `call_model.py`
* `.gitignore`
* `SUBMISSION.md`

The API key is stored securely using a `.env` file and is excluded from GitHub uploads.
