@echo off
echo Initializing virtual environment
call virtualenv NuRS_executable

echo Installing requirements and dependencies
call NuRS_executable\Scripts\activate
call pip install -r requirements.txt
