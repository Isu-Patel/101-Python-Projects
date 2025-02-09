def ask_for_feedback():

    feedback = input("How did you find the course? ")

    rating = input("Please rate the course from 1 to 5(1 bring poor and 5 being excellent): ")

    suggestions = input("Do you have Any suggestions for improvement? ")

    print("\nThank you for your feedback!")


    print("\nHere is the feedback you provided: ")
    print(f"Course Feedback: {feedback}")
    print(f"Rating: {rating}")
    print(f"Suggestions: {suggestions}")

ask_for_feedback()

# ------------------------------- Output -------------------------------- #
# How did you find the course? It was great!
# Please rate the course from 1 to 5(1 bring poor and 5 being excellent): 5
# Do you have any suggestions for improvement? No, it was perfect!
# Thank you for your feedback!
# Here is the feedback you provided:
# Course Feedback: It was great!
# Rating: 5
# Suggestions: No, it was perfect!
