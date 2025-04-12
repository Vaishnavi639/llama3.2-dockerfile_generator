import ollama

PROMPT = """
ONLY generate an ideal multi-stage Dockerfile using best practices for a {language} application built with the {framework} framework. 
Do NOT include any explanations or extra text.

The Dockerfile must include:
- An appropriate and secure base image
- Installing all necessary dependencies
- Setting the working directory
- Copying source code
- Exposing relevant ports (if applicable)
- Defining a proper entrypoint or command to run the app
- Optimized multi-stage build (e.g., builder and production stages)

Ensure the Dockerfile is ready for production deployment.
"""

def generate_dockerfile(language, framework):
    response = ollama.chat(
        model='llama3.2:latest',
        messages=[
            {
                'role': 'user',
                'content': PROMPT.format(language=language, framework=framework)
            }
        ]
    )
    return response['message']['content']

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    framework = input("Enter the framework (leave blank if none): ")
    dockerfile = generate_dockerfile(language, framework)

    print("\n Generated Dockerfile:\n")
    print(dockerfile)
