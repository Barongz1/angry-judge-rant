"""Angry Judge: The Short Rant Contest — entry for make.fun.

Writes one short rant to /output/entry.txt. The rant is about a broken printer, at most 400 characters, and nothing else.
"""
import os

RANT = "Dear printer: you have one job. One. You sat there all morning, blinking, humming, pretending to think, and the moment the boss walked in you decided to jam. You are not broken. You are dramatic. And I am done apologising for you in meetings."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT + "\n")

if __name__ == "__main__":
    main()
