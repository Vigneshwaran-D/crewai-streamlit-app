# CrewAI Configuration App with Streamlit and Azure OpenAI

This application configures and runs CrewAI agents with tasks using Azure OpenAI. It's built using Streamlit for an interactive web interface.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Vigneshwaran-D/crewai-streamlit-app.git
   cd crewai-streamlit-app
   streamlit run app.py


# Sample Task

To use these sample details in the Streamlit app:

Run your Streamlit app.
For the "Number of Agents" input, enter 2.
Fill in the details for each agent as described above.
For the "Number of Tasks" input, enter 4.
Fill in the details for each task as described above.
For the "Crew Name", enter "Quick Content Creation Team".
For the "Crew Description", enter "A small team focused on creating a short blog post quickly".

Here's how to input this information step-by-step:

Agent Configuration:

Agent 1:

Name: Writer
Role: Content Writer
Goal: Create engaging and informative content
Backstory: A versatile writer with experience in various topics and formats


Agent 2:

Name: Editor
Role: Content Editor
Goal: Ensure content quality and consistency
Backstory: An experienced editor with a keen eye for detail and clarity




Task Configuration:

Task 1:

Description: Come up with a topic for a short blog post about productivity tips
Expected Output: A clear, concise topic idea for a blog post
Assign to: Writer


Task 2:

Description: Write a 300-word draft blog post based on the generated idea
Expected Output: A 300-word draft blog post on productivity tips
Assign to: Writer


Task 3:

Description: Review the draft, correct any errors, and improve clarity and flow
Expected Output: An edited and refined version of the blog post
Assign to: Editor


Task 4:

Description: Perform a final review of the edited post and suggest any last improvements
Expected Output: A final version of the blog post ready for publication
Assign to: Writer




Crew Configuration:

Crew Name: Quick Content Creation Team
Crew Description: A small team focused on creating a short blog post quickly

# Sample Crew: Mobile App Development Team

## Agents

1. **Product Manager (PM)**
   - Role: Product Manager
   - Goal: Oversee the development of a successful mobile app that meets user needs and business objectives
   - Backstory: An experienced PM with a track record of launching successful apps in various industries

2. **UX Designer**
   - Role: User Experience Designer
   - Goal: Create an intuitive and engaging user interface for the mobile app
   - Backstory: A creative designer with a passion for user-centered design and a portfolio of award-winning mobile interfaces

3. **Software Developer**
   - Role: Mobile App Developer
   - Goal: Implement the app's features and ensure high-quality, bug-free code
   - Backstory: A skilled programmer with expertise in mobile app development across multiple platforms

4. **Quality Assurance (QA) Tester**
   - Role: QA Specialist
   - Goal: Ensure the app functions correctly and provides a smooth user experience
   - Backstory: A detail-oriented tester with a knack for finding edge cases and usability issues

## Tasks

1. **Define MVP Features**
   - Description: Create a list of Minimum Viable Product (MVP) features for the mobile app based on market research and user needs
   - Expected Output: A prioritized list of MVP features with brief descriptions
   - Assigned to: Product Manager

2. **Design App Wireframes**
   - Description: Create wireframes for the main screens of the mobile app based on the MVP features
   - Expected Output: A set of low-fidelity wireframes for key app screens
   - Assigned to: UX Designer

3. **Implement Core Functionality**
   - Description: Develop the core features of the app as defined in the MVP list
   - Expected Output: A working prototype of the app with basic functionality implemented
   - Assigned to: Software Developer

4. **Conduct Initial Testing**
   - Description: Perform a first round of testing on the app prototype, focusing on functionality and user experience
   - Expected Output: A detailed report of any bugs, usability issues, and suggestions for improvement
   - Assigned to: QA Tester

5. **Refine UI Design**
   - Description: Based on the wireframes and initial feedback, create a high-fidelity UI design for the app
   - Expected Output: A complete set of UI designs for all app screens
   - Assigned to: UX Designer

6. **Implement UI and Additional Features**
   - Description: Implement the refined UI design and add any additional features based on feedback
   - Expected Output: An updated version of the app with full UI implementation and all MVP features
   - Assigned to: Software Developer

7. **Conduct Final Testing**
   - Description: Perform a comprehensive test of the app, including functionality, usability, and performance
   - Expected Output: A final QA report detailing any remaining issues and overall app quality
   - Assigned to: QA Tester

8. **Prepare Launch Plan**
   - Description: Create a launch plan for the app, including marketing strategy and release timeline
   - Expected Output: A detailed launch plan document
   - Assigned to: Product Manager


Sample Output:

[CrewAI Streamlit APP (Sample Output).pdf](https://github.com/user-attachments/files/17361148/CrewAI.Streamlit.APP.Sample.Output.pdf)
