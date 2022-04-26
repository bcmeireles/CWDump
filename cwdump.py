import requests
import os

def main():
  if not os.path.exists('generated'):
    os.makedirs('generated')

  #username = input('Username: ')
  username = "dvnt"

  r = requests.get(f"https://www.codewars.com/api/v1/users/{username}")
  data = r.json()

  langs = [x for x in data['ranks']['languages']]

  totalCompleted = data["codeChallenges"]["totalCompleted"]

  page_count = abs(totalCompleted - 1) // 200

  while page_count >= 0:
    chals = requests.get(f"https://www.codewars.com/api/v1/users/{username}/code-challenges/completed?page={page_count}").json()
    for chal in chals["data"]:
      print(chal)
    page_count -= 1

if __name__ == "__main__":
  main()