#!usr/sbin/python
import urllib.parse as urlparse
import mysql.connector as mariadb

#Connection to database
mariadb_connection = mariadb.connect(user='anonymous', password='corendon', database='corendon')
cursor = mariadb_connection.cursor()

#Fetch data from databse
try:
    cursor.execute("SELECT * FROM Passengers")
except mariadb.Error as error:
    print("Error: {}".format(error))

data = cursor.fetchall()

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
    html += '<link rel="shorcut icon" href="../html/image/icon/favicon.ico"> \n'
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

    html += str(data)

    html += '<title>Corendon Captive Portal.</title> \n'
    html += '</head> \n'
    html +=  '<body> \n'

    html +=  '<!-- box containing captive portal --> \n'
    html +=  '<div class="container"> \n'
    html +=    '<img style="margin-top:1em; " src="../html/image/Logo_Coredon.png" width="100%"> \n'
    html +=    '<h1>Captive portal</h1> \n'
    html +=    '<h6>Login to gain access to internet</h6> \n'

    html +=    '<!-- Login Form --> \n'
    html +=    '<form method="POST" action="login.py"> \n'
    html +=      '<div class="form-group"> \n'
    html +=        '<label for="name"><b>Name:<b></label> \n'
    html +=        '<input type="name" class="form-control" id="inputName" name="inputName" placeholder="Name on ticket" required> \n'
    html += '<div class="form-group">\n'
    html += '<label for="ticketNumber"><b>Ticket Number:<b></label>\n'
    html += '<input type="text" class="form-control" id="ticketNumber" name="ticketNumber" aria-describedby="ticketHelp" placeholder="Enter ticket number" required>\n'
    html += '<small id="ticketHelp" class="form-text text-muted">Well never share your info with someone else </small> \n'
    html += '</div>\n'

    html += '<div class="form-group form-check">\n'
    html += '<input type="checkbox" class="form-check-input" id="exampleCheck1">\n'
    html += '<label class="form-check-label" for="exampleCheck1"><small>I accept the terms and service</small></label>\n'
    html += '</div>\n'

    html += '<input type="hidden" name="tok" value="$tok">\n'
    html += '<input type="hidden" name="redir" value="$redir">\n'
    html += '<input style="margin-bottom: 1em;" type="submit"  value="Continue" class="btn btn-primary">\n'
    html += '</form>\n'
    html += '</div>\n'

    html += '<!-- Button to Open the Modal -->\n'
    html += '<button type="button" class="modalbtn btnhelp" data-toggle="modal" data-target="#myModal">\n'
    html += '? \n'
    html += '</button>\n'
    html += '<!-- The Modal -->\n'
    html += '<div class="modal" id="myModal">\n'
    html += '<div class="modal-dialog">\n'
    html += '<div class="modal-content">\n'
    html += '<!-- Modal Header -->\n'
    html += '<div class="modal-header">\n'
    html += '<h4 class="modal-title">Help</h4>\n'
    html += '<button type="button" class="close" data-dismiss="modal">&times;</button>\n'
    html += '</div>\n'

    html += '<!-- Modal body -->\n'
    html += '<div class="modal-body">\n'
    html += '<h5><b>Why can \'t I access internet? </b></h5> \n'
    html += '<h5><b>Where can I find my ticketnumber?</b></h5>\n'
    html += '<img style="width:100%;"  src="../html/image/Ticket.png"</img> \n'
    html += '</div>\n'

    html += '<!-- Modal footer -->\n'
    html += '<div class="modal-footer">\n'
    html += '<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>\n'
    html += '</div>\n'
    html += '</div>\n'
    html += '</div>\n'
    html += '</div>\n'
    html += '</body>\n'
    html += '</html>\n'

    return [bytes(html, 'utf-8')]

if __name__ == '__main__':
     page = application({}, print)
     print(page[0].decode())

