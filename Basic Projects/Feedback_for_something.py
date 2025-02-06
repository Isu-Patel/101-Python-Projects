def ask_for_feedback():

  feedback = input("How did you feel this Course? ")

  rating = input("Please rate the course from 1 to 5 ( 1 being poor rating and 5 means excellent rating ): ")

  suggestions = input("Do you have Any suggestions for improvement? ")

  print("\nThanks for your feedback!")

  print("\nHere is the feedback you provided: ")
  print(f"Course Feedback: {feedback}")
  print(f"Rating: {rating}")
  print(f"Suggestions: {suggestions}")

ask_for_feedback()
