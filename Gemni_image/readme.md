Build a Multi-Modal GenAI Application: Challenge Lab
experiment

This content is not yet optimized for mobile devices.
For the best experience, please visit us on a desktop computer using a link sent by email.
Google Cloud self-paced labs logo

Overview
In a challenge lab you’re given a scenario and a set of tasks. Instead of following step-by-step instructions, you will use the skills learned from the labs in the course to figure out how to complete the tasks on your own! An automated scoring system (shown on this page) will provide feedback on whether you have completed your tasks correctly.

When you take a challenge lab, you will not be taught new Google Cloud concepts. You are expected to extend your learned skills, like changing default values and reading and researching error messages to fix your own mistakes.


Labs are timed and cannot be paused. The timer starts when you click Start Lab.
The included cloud terminal is preconfigured with the gcloud SDK.
Use the terminal to execute commands and then click Check my progress to verify your work.
Challenge scenario
### Scenario: You're a developer at an AI-powered bouquet design company. Your clients can describe their dream bouquet, and your system generates realistic images for their approval. To further enhance the experience, you're integrating cutting-edge image analysis to provide descriptive summaries of the generated bouquets. Your main application will invoke the relevant methods based on the users' interaction and to facilitate that, you need to finish the below tasks:

Task 1: Develop a Python function named generate_bouquet_image(prompt). This function should invoke the imagen-3.0-generate-002 model using the supplied prompt, generate the image, and store it locally. For this challenge, use the prompt: Create an image containing a bouquet of 2 sunflowers and 3 roses.

Click Check my progress to verify the objective.

Generate an image by sending a text prompt
### Task 2: Develop a second Python function called analyze_bouquet_image(image_path). This function will take the image path as input along with a text prompt to generate birthday wishes based on the image passed and send it to the gemini-2.0-flash-001 model. To ensure responses can be obtained as and when they are generated, enable streaming on the prompt requests.

Click Check my progress to verify the objective.