import time
def ask_questions():
    questions = [
        {
            "question": "Q1: How do you feel in crowds?",
            "options": {
                "A": "Energized",
                "B": "Neutral",
                "C": "Drained"
            },
            "scores": {"A": "extrovert", "B": "neutral", "C": "introvert"}
        },
        {
            "question": "Q2: Do you prefer working in groups or alone?",
            "options": {
                "A": "Groups",
                "B": "Depends",
                "C": "Alone"
            },
            "scores": {"A": "extrovert", "B": "neutral", "C": "introvert"}
        },
        {
            "question": "Q3: How do you make decisions?",
            "options": {
                "A": "Logically",
                "B": "Both logic and feeling",
                "C": "Emotionally"
            },
            "scores": {"A": "logical", "B": "balanced", "C": "emotional"}
        }
    ]

    traits = {"introvert": 0, "extrovert": 0, "neutral": 0, "logical": 0, "emotional": 0, "balanced": 0}

    for q in questions:
        print("\n" + q["question"])
        for key, value in q["options"].items():
            print(f"  {key}. {value}")
        
        answer = ""
        while answer not in ["A", "B", "C"]:
            answer = input("Your answer (A/B/C): ").strip().upper()

        trait = q["scores"][answer]
        traits[trait] += 1

    return traits


def analyze_traits(traits):
    print("\nAnalyzing your behavior...")
    time.sleep(5)
    print('\n\n')
    if traits["introvert"] > traits["extrovert"]:
        print("You are more introverted.")
    elif traits["extrovert"] > traits["introvert"]:
        print("You are more extroverted.")
    else:
        print("You are balanced between introversion and extroversion.")

    if traits["logical"] > traits["emotional"]:
        print("You are more logical in decision-making.")
    elif traits["emotional"] > traits["logical"]:
        print("You are more emotionally driven.")
    else:
        print("You balance logic and emotion well.")

traits = ask_questions()
analyze_traits(traits)