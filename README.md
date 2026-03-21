
# AI Tutor Chatbot

An AI-powered tutoring assistant that helps students learn through interactive conversations.

The chatbot follows the Socratic teaching method, guiding students by asking questions and encouraging deeper understanding instead of directly giving answers.

At the end of the learning session, the system generates a structured lesson summary describing what the student learned and what topic should be studied next.

------------------------------------------------------------

## Features

• Interactive AI tutoring conversation  
• Socratic teaching approach  
• Structured lesson summary generation  
• Conversation context memory  
• Automatic academic feedback report  

------------------------------------------------------------

## Technologies

Python  
OpenAI API  
Pydantic  
GPT Models  

------------------------------------------------------------

## How It Works

1. The user starts a conversation with the AI tutor.

2. The AI guides the learning process using the Socratic method.

3. The chatbot asks follow-up questions to help the student think and understand.

4. When the user types:

finish

the system generates a structured lesson report.

------------------------------------------------------------

## Example Lesson Summary

Subject Learned:
Linear Algebra

Key Concepts:
Vectors  
Matrix Multiplication  
Eigenvalues  

Student Performance:
The student showed good understanding but needs additional practice.

Next Recommended Topic:
Vector Spaces

------------------------------------------------------------

## Installation

Install the required libraries:

pip install openai pydantic

------------------------------------------------------------

## Run the Project

Run the chatbot:

python main.py

------------------------------------------------------------

## How To Use

Start chatting with the AI tutor.

To generate a lesson summary type:

finish

To exit the program type:

.

------------------------------------------------------------

## Project Structure

ai-tutor-chatbot

main.py  
README.md  
requirements.txt  

------------------------------------------------------------

## Future Improvements

Possible improvements for future versions:

• Web interface  
• Student progress tracking  
• Database integration  
• Personalized learning recommendations
## Why This Project Stands Out

- Uses LLM (GPT) for real-time reasoning
- Implements structured outputs with Pydantic
- Applies the Socratic teaching method
- Maintains conversation context
- Demonstrates AI + software engineering skills
