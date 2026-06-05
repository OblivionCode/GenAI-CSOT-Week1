# ChatAgent Submission

## Overview

I created a chatbot using OpenRouter and Python.

The chatbot supports multi-turn conversations and remembers previous messages using conversation history.

## Features

- Multi-turn conversation
- Rolling memory buffer
- Model selection
- Exit command
- Manual compact command

## Memory Management

The chatbot stores messages in a list.

When the number of messages exceeds the limit, older messages are removed using compact_history().

## Challenges Faced

- Understanding API calls
- Managing conversation history
- Fixing Python import issues

## Future Improvements

- Streaming output
- Better summarization
- GUI version

## Note

The final chatbot submission has been implemented directly within the second build itself. Instead of creating a completely separate final build file, the existing implementation was extended and polished to satisfy all the project requirements.
