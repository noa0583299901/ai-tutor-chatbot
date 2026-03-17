import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from typing import List


load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class LessonSummary(BaseModel):
    subject_learned: str
    key_concepts: List[str]
    student_performance: str
    next_recommended_topic: str


user_schema = LessonSummary


def start_chat():

    history = [{
        "role": "system",
        "content": "You are a professional Academic Tutor. Follow the Socratic Method. Be formal and encouraging."
    }]

    print("--- AI Tutor System Started ---")
    print("Type '.' to exit or 'finish' for a summary report.\n")
    while True:
        user_input = input(">> ")
       
        if user_input.strip() == ".":
            print("AI Tutor: It was a pleasure learning with you. Goodbye!")
            break
      
        if user_input.lower() == "finish":
            print("\n--- Generating Lesson Report ---")
            response = client.beta.chat.completions.parse(
                model="gpt-4.1-mini",
                messages=history,
                response_format=user_schema 
            )
            report = response.choices[0].message.parsed
            
            print(f"\nסיכום שיעור: {report.subject_learned}")
            print(f"מושגים: {', '.join(report.key_concepts)}")
            print(f"ביצועים: {report.student_performance}")
            print(f"הנושא הבא: {report.next_recommended_topic}")
            break 
            
     
      
        history.append({"role": "user", "content": user_input})
        
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",  
                messages=history,
                max_tokens=150,
                temperature=0.7 
            )
            
            ai_message = response.choices[0].message.content
            print(f"AI: {ai_message}")
            history.append({"role": "assistant", "content": ai_message})
            
        except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    start_chat()