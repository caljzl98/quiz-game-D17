class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0
    
    def next_question(self):
        current = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current.text} (True/False): ")
        self.check_answer(user_answer, current.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def check_answer(self, guess, answer):
        if guess.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The corerct answer was: {answer}.")
        print(f"You current score is: {self.score}/{self.question_number}.\n")