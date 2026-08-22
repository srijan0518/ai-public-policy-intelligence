@echo off
python -m venv .venv
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm
echo.
echo Setup complete.
echo Add your API key to .env, then run:
echo streamlit run app.py
pause
