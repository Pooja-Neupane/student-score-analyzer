import numpy as np

def get_scores():
    while True:
        try:
            scores_input = input("🔢 Enter scores separated by space: ").strip()
            scores = np.array(list(map(float, scores_input.split())))
            if scores.size == 0:
                raise ValueError("No scores entered.")
            return scores
        except ValueError as e:
            print(f"❌ Invalid input: {e}. Please try again.\n")

def analyze_scores(scores):
    average = np.mean(scores)
    highest = np.max(scores)
    lowest = np.min(scores)
    std_dev = np.std(scores)

    print("\n📊 Score Analysis Result:")
    print(f"• Average Score          : {average:.2f}")
    print(f"• Highest Score          : {highest}")
    print(f"• Lowest Score           : {lowest}")
    print(f"• Standard Deviation     : {std_dev:.2f}")

    # Optional interpretation
    if std_dev > 15:
        print("⚠️ Wide range in scores. Consider consistency improvement.")
    elif std_dev < 5:
        print("✅ Very consistent performance.")
    else:
        print("📌 Moderate variation in scores.")

if __name__ == "__main__":
    scores = get_scores()
    analyze_scores(scores)
