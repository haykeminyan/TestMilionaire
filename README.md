<h1><b>Technical task for STDev</b></h1>

The game is like "Who Wants to Be a Millionaire?"<br/><br/>
• During each game, the player is asked 5 questions randomly selected from the base and not repeated during one game. For each question there are possible answer options (n number) and only one of them is correct. When the player chooses one of the answer options, the system informs about the problem being right or wrong. <br/><br/>
• Each question has its corresponding point. (for example, according to its complexity). If the answer is correct, the point for the given question is added to the points calculated for the given game, and each question can have 5-20 points. In case of an incorrect answer, the points are not added and the player is notified about the correct answer.<br/><br/>
• At the end of the game, the player is shown the number of points he has collected. This is the main problem where you need to manually add data to the Database; the content of the questions, of course, is not essential. <br/><br/>
• After completing this part, send it to us and continue working on the rest. Add Login Admin who can add / delete / modify questions, options for answering those questions and the right option, as well as the point for each question. Create a sign-in and log-in possibility (Name, Surname, Password). Playing is possible only after logging in. The best result is calculated for each user and the top ten is displayed on the screen (names and the highest score) based on the users’ best results.<br/><br/>


<h2>Technical implementation of the task</h2> <br/>
Tech stack is

* Django 4.2.4
* PostgreSQL
* Python 3.11.2
* JavaScript with CSS material Bootstrap version 5.3.0

A couple of technical words about this task

1. Can be launched via command <br/> docker-compose up --build <br/> in root main directory.
2. Through the admin area, which is on <br/> http://localhost:8000/admin <br/> (You can add/edit/delete questions throughout the admin area).
3. User-profile must be created in admin-area, and questions and answers models are developed with relation <br/> ONE to ONE relationship. This approach will keep unique questions and answers
4. View <b>game</b> contains this return as function {'user': <Profile: admin>, 'points': 0, 'question_id': 2, 'question': 'Which rock group is full of Armenians?', 'array_of_answers': ['System of a Down', 'Rammstein', 'Aerosmith', 'Linkin Park'], 'correct_answer': 'System of a Down'}. Some words about default fields. Profile-user as default has 0 points from creation, answers store in the list default it's the empty list: User can in admin area input whatever he wants.
5. All questions begin from easy to hard. Junior questions +5 points, Middle questions +10 points, Senior questions +20 points :=)
6. Added blockers with JavaScript in templates (when a user submits an answer he will not allowed to re-click the radio button and re-send the form via POST request).<br/> New page developed by GET request, submit form POST request. <br/> During POST request I checked what in the payload what user has inputted (answer) and added csrf-token in this request for safety too.
7. The user can quit the game whenever he wants and I added button to finish the game with the current result of the game or drop the game and return to the start.
8. Added pre-commit configuration with hooks that cleaned up all code (black, isort, trailing-comma, ... etc)


Things to improve and fix if wanna see amazing application:
1. <b>Bug</b>: The user can input the right answer refresh the page and collect points. Can be solved with sessions in Django.
2. <b>Improvement</b>: As the rule of the game user can manually choose difficulty with separate junior/middle/senior questions.
3. <b>Improvement</b>: Need add tests for backend part (pytest). For example to check if all questions are unique. <br/> For the Frontend part too. For example, Cypress or Playwright to check if the user can't cheat.
5. <b>Improvement</b>: Add a more responsive and user-friendly design (for example the user will see that all questions are answered and after the right/wrong choosing answer see his result in radio buttons) and deploy to some domain :=)
6. <b>Improvement</b>: Small clean-up in requirements.txt just copied from previous projects may be such a lot dependencies not needed.


https://github.com/haykeminyan/TestMilionaire/assets/43892880/36c15955-eeb7-4d0c-9e48-624b6bb1d88c


Short demo video with features which are described earlier.
