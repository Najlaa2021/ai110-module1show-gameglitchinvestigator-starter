# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game was functional the first time , relativlly. i entered a value and it asked me to go higher in my guess/assumption. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    1) the game always asks you to go higher.
    2) i feel as there is only "go higher"option. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  5    | go lower.         | go higher          None
| 100   | go higher           go lower           None           
|  17   | you won              wrong             Not able to start a new game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
  I made use of Claude ,whcih i integrated with my VS code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
  Ai suggested that we fix the comparison (lower/higher)
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  did not run into this issue

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
  I tested it both by running the test file and also check the wesbiste again after every fix. 
- Describe at least one test you ran (manual or using pytest)  
  after the fixes. I triggered the site again and entered diffrent values 
  and what it showed you about your code. 
    it showed me that the code is working accordingly 
- Did AI help you design or understand any tests? How? yes, it helped me barainstorm some edge cases

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlist is basiclaly a python library that to turn data into an app aplication 
  

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects
?
  better prompting and connecting with the AI

  - This could be a testing habit, a prompting strategy, or a way you used Git.

- What is one thing you would do differently next time you work with AI on a coding task?
  have a clear layout of whats expected and then move to the technicality of things . 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  I have been using cursor at work so i definitly have a preconcived notion about AI but it definitly tuckles the minor details while giving me time to think and process much bigger issues and actually work on bigger design, code, prgramming..etc. it also helps me learn and/or remember things which may have skipped my mind of things that i may have forgotten.
