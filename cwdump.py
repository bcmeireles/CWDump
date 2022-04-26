import requests
import os
from selenium import webdriver

def main():
  if not os.path.exists('generated'):
    os.makedirs('generated')

  driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
  driver.get("https://www.codewars.com/users/sign_in")

  input("Please login on the browser and press enter to continue...")

  username = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/ul/li[4]/div/div/ul/li[1]/a").get_attribute("href")
  username = username[31:]
  print(username)

  driver.get("https://www.codewars.com/users/dvnt/completed_solutions")

  profile = requests.get(f"https://www.codewars.com/api/v1/users/{username}").json()

  langs = [x for x in profile['ranks']['languages']]
  for lang in langs:
    if not os.path.exists(f"generated/{lang}"):
      os.makedirs(f"generated/{lang}")
  

  totalCompleted = profile["codeChallenges"]["totalCompleted"]

  index = 0
  while index < totalCompleted:
    index += 1
    base = f"/html/body/div[1]/div[1]/main/div[5]/div/div/div[2]/div[{index}]"
    chalName = driver.find_element_by_xpath(f"{base}/div[1]/a").text
    chalURL = driver.find_element_by_xpath(f"{base}/div[1]/a").get_attribute("href")
    
    challenge = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{chalURL[30:]}").json()

    print(challenge)
    input()
    try:
      creator = challenge["createdBy"]["username"]
    except:
      creator = "Unknown"
    input(creator)
    rank = challenge["rank"]["name"]
    input(rank)
    desc = challenge["description"]
    tags = challenge["tags"]
    tags = "` `".join(tags)
    tags += "`"
    tags = "`" + tags
    input(tags)

    lang = driver.find_element_by_xpath(f"{base}/h6").text.lower()[:-1]
    code = driver.find_element_by_xpath(f"{base}/div[2]/pre/code").text

    solution = f"""```{lang}
{code}
```"""
    with open(f"generated/{lang}/{rank}.md", "a") as f:
      f.write(f"# [{chalName}]({chalURL})\nby [{creator}](https://www.codewars.com/users/{creator})\n## Description\n{desc}\n## Solution:\n{solution}\n###\nTags: {tags}\n<br>\n")

    input()




  

if __name__ == "__main__":
  main()