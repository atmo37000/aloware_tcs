Sample of Selenium test case for Aloware
Conducts check of buttons in header panel and page title

How to run:
- Install Google Chrome and chromedriver
- Clone repo
- Create venv by running *python3 -m venv venv*
- Activate on win machine venv *source venv/Scripts/activate*
- Run *pip install -r requirements.txt*
- Run *pytest test_landing_page_header.py*

Note:
In order to avoid 403 error use this recipe for your chromedriver: https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver
