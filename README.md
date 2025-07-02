# Setup virtual environment
python -m venv .venv

source .venv/Scripts/activate
# Windows
pip install -r requirements.txt

# Run tests
**_Run by order user test_** - pytest test/test_user_management.py -v

_**Run by order login test**_ - pytest test/test_login.py -v

_**Generate user report generate**_ -
pytest -v --tb=short test/test_user_management.py --html=reports/user_management_report.html --self-contained-html --metadata "Project" "i2v QA (user_management)" --metadata "Tester" "Lakshya"

_**Generate login report generate**_ -
pytest -v --tb=short test/test_login.py --html=reports/login_report.html --self-contained-html --metadata "Project" "i2v QA (login_page)" --metadata "Tester" "Lakshya"

Test Cases Covered - User management -
Test ID-
TC_User_001,
TC_User_002,
TC_User_003,
TC_User_004,
TC_User_005,

Test Cases Covered - Login page -
Test ID-
TC_Login_page_001,
TC_Login_page_002,
TC_Login_page_009,
TC_Login_page_011,

# Reports - (download and open in browser)

report link user_management - https://drive.google.com/file/d/1s6pY4wDJrlbm_MQU_kAoZBLI-npoWPzn/view?usp=sharing

report link login page - https://drive.google.com/file/d/1Tn5vztxZNPBu_2rBjqcpwvM9noIsi6mr/view?usp=sharing
