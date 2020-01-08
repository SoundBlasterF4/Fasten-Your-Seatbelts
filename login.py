#!/usr/bin/python
import sys
import os
import subprocess
import urllib.parse as urlparse
import mysql.connector as mariadb
#Value to set login True or False for now its empty
login = None
#Esatabilish connection with the database
mariadb_connection = mariadb.connect(user='anonymous', password='corendon', database='corendon')
cursor = mariadb_connection.cursor()

#Iptables rules
#os.system("cd /var/www/fys/wsgi && ./iptablesStart.sh")

#Try to fetch the data from the database
try:
    cursor.execute("SELECT * FROM Passengers")
except mariadb.Error as error:
    print("Error: {}".format(error))
data = cursor.fetchall() #Fetch
#Start of html
def application(environ, start_response):
    status = '200 OK'
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)

    html = ''
    html += ' <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional// \n'
    html += '          EN" "http://www.w3.org/TR/xhtml/DTD/xhtml-transitional.dtd"> \n '
    html += '<html lang="en" dir="ltr"> \n '
    html += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> \n'
    html += '<meta name="keywords" content="login, corendon, captiveportal, flight" /> \n '
    html += '<meta name="description" content="login to gain access to the internet" /> \n '
    html += '<meta name="copyright" content="All rights reserved Corendon" /> \n '
    html += '<meta name="publisher" content="InterDefense" /> \n '
    html += '<meta name="author" content="InterDefense" /> \n '
    html += '<!-- Bootstrap framework has been used --> \n '

    html += '<head> \n'
    html += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> \n'
    html += '<link rel="shorcut-icon" href="../html/image/icon/favicon.ico"> \n'
    html += '<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"> \n '
    html += '<meta http-equiv="Pragma" content="no-cache"> \n'
    html += '<meta http-equiv="Expires" content="0"> \n '
    html += '<meta charset="utf-8"> \n'
    html += '<meta name="viewport" content="width=device-width, initial-scale=1.0"> \n'
    html += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script> \n'
    html += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script> \n'
    html += '<script src="../html/js/bootstrap.min.js"></script> \n'
    html += '<script src="../html/script/slide.js" type="text/javascript"></script> \n'
    html += '<link rel="stylesheet" href="../html/css/bootstrap.css" type="text/css"> \n'
    html += '<link rel="shortcut icon" href="../html/images/splash.jpg" type="image/x-icon"> \n'
    html += '<link rel="stylesheet" type="text/css" href="../html/style.css"> \n'

#    html += str(data) #Hardcoded database show

    html += '<title>Corendon Captive Portal.</title> \n'
    html += '</head> \n'
    html +=  '<body> \n'

    environmentVars = ['REQUEST_METHOD', 'REQUEST_URI', 'QUERY_STRING', 'SCRIPT_NAME', 'HTTP_REFERER']

    # check HTTP request method and get parameters from request
    method = environ.get('REQUEST_METHOD', '')
    params = {}

    if method == 'GET':
     params = urlparse.parse_qs(environ['QUERY_STRING'])
    elif method == 'POST':
     input = environ['wsgi.input'].read().decode()
     params = urlparse.parse_qs(input)
    #Get values of Name and ticketnmbr through the input of the html
    name = params.get('inputName')
    ticket = params.get('ticketNumber')
#    html += str(name)
#    html += str(ticket)
    ticket = str(ticket)
    ticket = ticket.replace('[', '')
    ticket = ticket.replace(']', '')
    name = str(name)
    name = name.replace('[','')
    name = name.replace(']','')
    #Querry to match the input with the database
    querry = "SELECT * FROM Passengers WHERE ticketnumber=" + ticket + " AND firstname=" + name
#    html += str(querry)

    html +=  '<!-- box containing captive portal --> \n'
    html +=  '<div class="container"> \n'
    html +=    '<img style="margin-top:1em; " src="../html/image/Logo_Coredon.png" width="100%"> \n'

    #Execute querry
    try:
     cursor.execute(querry)
     fetch = cursor.fetchall()
     count = cursor.rowcount #Get count value

 #    html += str(count)
     #If value = 1 then it means its in the database, otherwise its not so it fails
     if count == 1:
      html += '<b style="font-type:bold; font-size: 3vh;">Login Success!</b>'
      login = True #Set value of login that was None

     else:
      html += 'Login Fail!'
      login = False
     #If value = True then redirect to the login other wise to back to login
     if login == True:
      #Add iptable rule
      ipAddr = environ.get('REMOTE_ADDR')
      html += str(ipAddr)
      #Allow user IPTABLE
      port80 = 'sudo iptables -t nat -I PREROUTING -i wlan0 -p tcp --dport 80 -s ' + ipAddr + ' -j ACCEPT'
      port430 = 'sudo iptables -t nat -I PREROUTING -i wlan0 -p tcp --dport 430 -s ' + ipAddr + ' -j ACCEPT'
      port443 = 'sudo iptables -t nat -I PREROUTING -i wlan0 -p tcp --dport 443 -s ' + ipAddr + ' -j ACCEPT'

      os.system(port80)
      os.system(port430)
      os.system(port443)
      html += '<meta http-equiv="Refresh" content="2; url=../html/htmlPage2.html" />'
     elif login == False:
      #Add iptable rule
      html += '<meta http-equiv="Refresh" content="2; url=index" />'
     else:
         html +='<a>Error</a>' #Give error
     html += '</div>\n'
     html += '</body>\n'
     html += '</html>\n'
    except mariadb.Error as error:
     print("Error: {}".format(error))

    return [bytes(html, 'utf-8')]

if __name__ == '__main__':
     page = application({}, print)
     print(page[0].decode())
