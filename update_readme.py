import os

README_PATH = "README.md"
COUNTER_PATH = ".counter"

def get_count():
    if os.path.exists(COUNTER_PATH):
        with open(COUNTER_PATH, "r") as f:
            return int(f.read().strip())
    return 0

def save_count(count):
    with open(COUNTER_PATH, "w") as f:
        f.write(str(count))

def update_readme(count):
    message = f"I wrote a cheeky script that automatically contributes to my Github to illustrate why more than commits matter. This is the {count} time this script has run."
    with open(README_PATH, "w") as f:
        f.write(message)

def main():
    count = get_count() + 1
    update_readme(count)
    save_count(count)

if __name__ == "__main__":
    main()
