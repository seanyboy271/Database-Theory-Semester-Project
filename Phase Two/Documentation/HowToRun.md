# To run this database demonstration:
  1. Start main.py
  2. Enter these commands to cmd:
      1. cd <location of folder "Phase Two">
      2. cloud_sql_proxy.exe -instances=cmsc-508-project:us-east1:cmsc-508-database=tcp:3306
  3. Enter "127.0.0.1:5000" to Google search to open the web app
    
Be sure that you have Google Cloud SDK installed and initialized.
Be sure that you have Python version 3.7 (may work with other Python versions as well)

### Dependencies
These dependencies must be installed to run the demonstration:
  1.  pip install Flask
  2.  pip install pymysql
  3.  pip install sqlalchemy
  4.  pip install flask-login
  5.  pip install bcrypt
