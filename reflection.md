# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
The hint was useless. I had to choose a number between 1 and 100. I first chose 6 and it said to go higher. Then I chose 99 and it still said go higher. I chose 100 just to check in the rare case that it atually was 100, but instead it told me go lower. There is no whole number in between 99 and 100 so the hint was obviously incorrect. Another bug was that using the new game button did not reset everything. It reset the secret number, but it didn't allow you to guess again and the message saying "You already won. Start a new game to play again" remained even after pressing the new game button multiple times. Another bug was that changing the difficulty on the left didn't actually change anything in the game. It was always on the same difficulty no matter what.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
I used Copilot and highlighted the code I saw was responsible for the wrong hint message bug and it suggested switching the greater than and less than signs in the code. I tried that and it worked, the hint message was correct after that change. I also used ChatGPT to ask about how to use session state to fix the bug of the secret number changing. It suggested using st.session_state to store the secret number, but it didn't give me a clear example of how to do that. I had to do some more research and trial and error to figure out how to implement that correctly.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I decided a bug was really fixed when I could play the game and win without any issues. For example, after fixing the hint message, I ran the game and tried different guesses to see if the hints were correct. I also ran pytest to check if all the tests in logic_utils.py were passing. AI helped me understand how to write tests for my code, especially when I was refactoring the logic into a separate file. It gave me suggestions on how to structure my tests and what cases to cover.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---
The secret number kept changing in the original app because Streamlit reruns the entire script every time an interaction happens (like clicking a button). This means that any variable defined in the script gets reset to its initial value on each rerun. To explain Streamlit reruns and session state to a friend, I would say that Streamlit is rerunning your script every time you click on something like a button or slider. Its like starting a YouTube video over from the beginning every time you pressed the pause button. The change I made to give the game a stable secret number was to use st.session_state to store the secret number so it doesn't get reset on each rerun.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

---
One habit I want to reuse in future projects is writing tests for my code, especially when refactoring. It helps ensure that my changes don't break existing functionality. Next time I work with AI on a coding task I'd be more specific in my prompts to get clearer suggestions. This project made me realize that while AI can be a helpful tool, it's not always perfect and requires an actual human to test to ensure the code works as expected.
