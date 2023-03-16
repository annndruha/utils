@ECHO OFF
echo ---------------------------------------------------------------
echo Current directory: %cd%
echo ---------------------------------------------------------------
python --version
echo ---------------------------------------------------------------
echo Starting...
echo Install virtual environment...
echo ---------------------------------------------------------------
python -m pip install --user --no-warn-script-location --disable-pip-version-check --no-index virtualenv
python -m venv venv
echo ---------------------------------------------------------------
echo Upgrade pip...
echo ---------------------------------------------------------------
venv\Scripts\python -m pip install --upgrade pip
echo Installing packages into venv...
echo ---------------------------------------------------------------
venv\Scripts\python -m pip install -r requirements.txt
echo ---------------------------------------------------------------
echo Virtual environment info:
echo ---------------------------------------------------------------
venv\Scripts\python --version
venv\Scripts\python -m pip --version
venv\Scripts\python -m pip list
echo ---------------------------------------------------------------
pause