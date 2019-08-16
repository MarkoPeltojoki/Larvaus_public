import requests
import json
import os
from urllib.parse import urlparse
from datetime import date

from flask import Flask, render_template
app = Flask(__name__, static_folder='static', static_url_path='')

# Thanks for all the code hints Über, could not pull this through otherwise: https://github.com/uber/Python-Sample-Application

with open('config.json') as f:
    config = json.load(f)

def error_out():
    """Check the HTTP errors, return True/False"""
    # Get Scoring uri from config.json file, check for request error
    uri1 = config.get('scoring_uri1')
    uri2 = config.get('scoring_uri2')
    uri3 = config.get('scoring_uri3')
    uri4 = config.get('scoring_uri4')
    uri5 = config.get('scoring_uri5')
    uri6 = config.get('scoring_uri6')
    uri7 = config.get('scoring_uri7')
    try:
        requests.get(uri1)
        requests.get(uri2)
        requests.get(uri3)
        requests.get(uri4)
        requests.get(uri5)
        requests.get(uri6)
        requests.get(uri7)
    except requests.exceptions.RequestException:
        return True        
    return False

def headers():
    """Header object for API requests"""
    return {'Content-Type': 'application/json'}

def get_week():
    """Input ISO Calendar week as ww"""
    return str(date.today().isocalendar()[1])

def get_year():
    """Input ISO Calendar year as yyyy"""
    return str(date.today().isocalendar()[0])

def primary1():
    """Request Primary1 from ML model webservice"""
    # Data to score for Primary1
    data1 = {"data":
            [
                [
                    get_week(),
                    get_year()
                ]
            ]
            }
    # Convert to JSON string
    input_data1 = json.dumps(data1)
    # Get Scoring uri from config.json file, check for request error
    uri1 = config.get('scoring_uri1')
    # Make the request and return Primary1
    resp1 = requests.post(uri1, input_data1, headers=headers())
    #First check if container is online. Then check if response has only one digit and hack trailing \ away, otherwise return two digits.
    if  resp1.status_code != 200:
        return "Larvaus1 sleeping"
    elif resp1.text[18] == "\\":
        return resp1.text[17]
    return resp1.text[17:19]

def primary2():
    """Request Primary2 from ML model webservice"""
    data2 = {"data":
            [
                [
                    get_week(),
                    get_year(),
                    primary1()
                ]
            ]
            }
    input_data2 = json.dumps(data2)
    uri2 = config.get('scoring_uri2')
    resp2 = requests.post(uri2, input_data2, headers=headers())
    if  resp2.status_code != 200:
        return "Larvaus2 sleeping"
    elif resp2.text[18] == "\\":
        return resp2.text[17]
    return resp2.text[17:19]

def primary3():
    """Request Primary3 from ML model webservice"""
    data3 = {"data":
            [
                [
                    get_week(),
                    get_year(),
                    primary1(),
                    primary2()
                ]
            ]
            }
    input_data3 = json.dumps(data3)
    uri3 = config.get('scoring_uri3')
    resp3 = requests.post(uri3, input_data3, headers=headers())
    if  resp3.status_code != 200:
        return "Larvaus3 sleeping"
    elif resp3.text[18] == "\\":
        return resp3.text[17]
    return resp3.text[17:19]

def primary4():
    """Request Primary4 from ML model webservice"""
    data4 = {"data":
            [
                [
                    get_week(),
                    get_year(),
                    primary1(),
                    primary2(),
                    primary3()
                ]
            ]
            }
    input_data4 = json.dumps(data4)
    uri4 = config.get('scoring_uri4')
    resp4 = requests.post(uri4, input_data4, headers=headers())
    if  resp4.status_code != 200:
        return "Larvaus4 sleeping"
    elif resp4.text[18] == "\\":
        return resp4.text[17]
    return resp4.text[17:19]

def primary5():
    """Request Primary5 from ML model webservice"""
    data5 = {"data":
            [
                [
                    get_week(),
                    get_year(),
                    primary1(),
                    primary2(),
                    primary3(),
                    primary4()
                ]
            ]
            }
    input_data5 = json.dumps(data5)
    uri5 = config.get('scoring_uri5')
    resp5 = requests.post(uri5, input_data5, headers=headers())
    if  resp5.status_code != 200:
        return "Larvaus5 sleeping"
    elif resp5.text[18] == "\\":
        return resp5.text[17]
    return resp5.text[17:19]

def primary6():
    """Request Primary6 from ML model webservice"""
    data6 = {"data":
            [
                [
                    get_week(),
                    get_year(),
                    primary1(),
                    primary2(),
                    primary3(),
                    primary4(),
                    primary5()
                ]
            ]
            }
    input_data6 = json.dumps(data6)
    uri6 = config.get('scoring_uri6')
    resp6 = requests.post(uri6, input_data6, headers=headers())
    if  resp6.status_code != 200:
        return "Larvaus6 sleeping"
    elif resp6.text[18] == "\\":
        return resp6.text[17]
    return resp6.text[17:19]

def primary7():
    """Request Primary7 from ML model webservice"""
    data7 = {"data":
            [
                [
                    get_week(),
                    get_year(),
                    primary1(),
                    primary2(),
                    primary3(),
                    primary4(),
                    primary5(),
                    primary6()
                ]
            ]
            }
    input_data7 = json.dumps(data7)
    uri7 = config.get('scoring_uri7')
    resp7 = requests.post(uri7, input_data7, headers=headers())
    if  resp7.status_code != 200:
        return "Larvaus7 sleeping"
    elif resp7.text[18] == "\\":
        return resp7.text[17]
    return resp7.text[17:19]

@app.route("/", methods=['GET', 'POST'])
def index():
    """Return the index.html"""
    # Start with index.html to introduce Larvaus
    picture = config.get('pic3')
    return render_template('index.html', pic=picture)

@app.route("/larvaus/", methods=['GET', 'POST'])
def larvaus():
    """Return the results to be shown as webservice output"""
    # If HTTP errors out, render error.html
    picture = config.get('pic2')
    if error_out() == True:
        return render_template('error.html', pic=picture)
    else:
        # Render larvaus.html
        picture = config.get('pic1')
        return render_template('larvaus.html',
            pic=picture,
            round=get_week() + " - " + get_year(),
            data=primary1() + " - " + primary2() + " - " + primary3() + " - " +primary4() + " - " + primary5() + " - " + primary6() + " - " + primary7()        
        )

if __name__ == '__main__':
    app.debug = os.environ.get('FLASK_DEBUG', True)
    app.run(port=6000)
