# Online-Tic-Tac-Toe

# System and Network Administration Final Project Report on: Online Tic-Tac-Toe Game with User Authentication

## Our Team:
- Demyan Zverev (SD-02)
- Emil Davlityarov
- Polina Pushkareva
- Renata Latypova (CS-02)

**Link to the Github repository:** [Online-Tic-Tac-Toe](https://github.com/Dema-koder/Online-Tic-Tac-Toe)  
**Link to Github Actions:** [tic-tac-toe.yml](https://github.com/Dema-koder/Online-Tic-Tac-Toe/blob/main/.github/workflows/tic-tac-toe.yml)  
**Link to the demo:** [YouTube Demo](https://youtu.be/sir5XYGR84Q)

## Goal and Tasks of the Project:
The goal of this project is to develop an online Tic-Tac-Toe application with the use of system administration concepts. To achieve this, we divided our work into the tasks described in detail below.

### Tasks of the Project:
- **Implement all the logic of the game using Python:** We need to implement the “server” functions of the application as well as the “client” functions. The “server” will be responsible for all management actions like database access and manipulations (like creating and searching for the game), provision of connections to games, finding the winner of the game according to made steps, and so on. The “client” implements all the logic associated with handling concrete clients, communicates with players requesting needed information, and responds with the appropriate game status.
- **Build a web page with HTML/CSS:** We need to provide the application view on all the implemented logic behind it. For this, we need to create a web page that includes authentication (login, sign up) windows, as well as a connection to the game.
- **Create a SQLite3 database:** We need to include the database in our project to have access to different games and user information to increase the overall performance of the application. We will store user information (such as id, nickname, password, and email) and games information (id of a game, cross and nought ids, the id of the user which will make the next move, winner id, and a sequence of moves in that game).
- **Prepare a monitoring system to collect statistics:** Metrics play an important role in understanding why the application is working in a certain way. So, we will use Prometheus to measure the performance of our application and Grafana for the visualization of the monitoring outcomes.
- **Prepare Docker for the application deployment:** For this, we need to set up docker-compose adjusting the project configurations for the deployment of our application on the remote server. We also need to ensure that everything we implement works fine.
- **Set up Github Actions pipeline:** We also will use the pipeline to build, test, and deploy our project. It will help to manage the project easier and automate future updates.
- **Wrap up all the implemented project steps in the final report for submission:** We need to summarize and explain all the completed work following the provided structure, which also includes the conclusion-making and analysis of how well the project was managed and built as a result.
- **Prepare the demo of the project:** We need to record a video to explain and show all the functionality we implemented and show the expected user session example.

### Responsibilities for Each Team Member:
- **Emil Davlityarov:** Preparing Docker, setting up Github Actions pipeline, preparing a monitoring system
- **Polina Pushkareva:** Implementing all the logic of the game using Python, writing the final report
- **Demyan Zverev:** Building a web page with HTML/CSS, creating SQLite3 database
- **Renata Latypova:** Implementing all the logic of the game using Python, demo of the project

## Methodology

### Technology Stack and Tools:
Our project utilized a diverse technology stack and various tools to achieve robust and scalable online Tic-Tac-Toe game functionality. The primary technologies used included:
- **Frontend Development:** HTML and CSS were used to create a dynamic and responsive user interface.
- **Backend Development:** Python, along with the Django framework, provided the server-side logic and interaction with the database.
- **Database Management:** SQLite3 was selected for user authentication and game session management due to its robustness and scalability.
- **Containerization:** Docker and Docker-compose were used to containerize the application, ensuring consistent environments across development, testing, and production.
- **Continuous Integration/Continuous Deployment (CI/CD):** Github Actions pipeline was implemented to automate the testing and deployment processes, enhancing the development workflow.
- **Monitoring:** Prometheus was integrated for monitoring the application’s performance in real-time.

### Development of Solution

#### Development Phases:
1. **Planning and Design:**
   - **Requirements Analysis:** Detailed discussions on project scope, objectives, and the functionalities required for the Tic-Tac-Toe game.
   - **System Design:** Architectural decisions, including database schema design and user system interaction possible outcomes.
2. **Implementation:**
   - **Backend Logic:** Development of game logic in Python, handling user requests, game state management, and database interactions.
   - **Frontend Interface:** Crafting the user interface with HTML/CSS.
   - **Database Setup:** Configuration of SQLite3 for storing user credentials and game sessions.
3. **Testing:**
   - **Unit Testing:** Each module, especially Python backend components, was subjected to thorough unit testing to ensure individual components function correctly.
4. **Deployment:**
   - Using Docker-compose to define and run multi-container Docker applications, preparing the system for deployment.
5. **Monitoring and Maintenance:**
   - Implementing Prometheus for monitoring system performance and uptime.
   - Routine checks and updates as part of maintenance.

### Tests as the PoC:

Development and Testing as Proof of Concept (PoC):
- Initial Prototype: Developed an initial version of the game to demonstrate basic playability and interface design.
- Scalability Testing: Ensured that the application could handle a significant number of simultaneous users without degradation of performance.
