#Deep Thought
#The question "What is the answer to the Great Question of Life, the Universe and Everything?" comes from the science fiction comedy series The Hitchhiker's Guide to the Galaxy by Douglas Adams. It's a humorous exploration of life, the universe, and our place in it.
#The Story
#In the series, a supercomputer named Deep Thought is tasked with figuring out the ultimate question of life, the universe, and everything.
#After spending 7.5 million years crunching numbers, Deep Thought announces the answer is 42.
#The Twist:
#The problem is, no one knows what the actual question is! Deep Thought built another even more powerful computer, Earth, specifically designed to figure out the question. (Spoiler alert: Earth gets demolished before it can deliver the answer.)
#Get user input
answer = input("what is answer to the Great Question of Life, the Universe and Everything?")

#print yes if the user inputs 42 or (case-insensitively) forty two
if answer.strip() == "42":
    print("yes")
elif answer.lower().strip() == "forty-two":
    print("yes")
elif answer.lower().strip() == "forty two":
    print ("yes")
#otherwise output NO.
else:
    print("No")

#possible_answers = ("42", "forty-two", "forty two")

#answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

#if answer in possible_answers:
 #   print("Yes")
#else:
 #   print("No")


