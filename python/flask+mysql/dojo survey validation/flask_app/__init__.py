from flask import Flask

app=Flask(__name__)
app.secret_key="azertyuiop"
DATABASE="dojo_survey_schema"