call virtualenv NuRS_executable
call pip install -r requirements.txt
pause
call NuRS_executable\Scripts\activate
call python src/main.py
pause