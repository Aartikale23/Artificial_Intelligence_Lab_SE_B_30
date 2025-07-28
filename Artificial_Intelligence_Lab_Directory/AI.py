def career_expert(choice1,choice2):
    if choice1=="Maths" and choice2=="Physics":
       return "Mechanical Engineering"
    elif choice1=="Programming" and choice2=="Maths":
       return "Computer Engineering"
    elif choice1=="Biology" and choice2=="Chemistry":
       return "Biotechnology"
    elif choice1=="Circuits" and choice2=="Maths":
       return "Electronic Engineering"  
    elif choice1=="Programming" and choice2=="Statics":
       return "Artificial Intelligence and Data Science"   
    elif choice1=="Programming" and choice2=="AI concepts":
      return "Artificial Intelligence and Machine Learning"
      
def main():
    print("Enter two subjects you like to choose from the given subjects:(Programming, Maths, Physics, Biology, Chemistry, Circuits, Statistics, AI Concepts):")
    sub1 = input("First choice: ")
    sub2 = input("Second choice: ")
    suggestion = career_expert(sub1, sub2)
    print(f"Suggested course:{suggestion}")
    
if __name__ == "__main__":
    main()


