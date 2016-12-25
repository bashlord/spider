import argparse
import requests
import pyquery

def login(session, email, password):
    # Navigate to Facebook's homepage to load Facebook's cookies.
    response = session.get('')

    # Attempt to login to Facebook
    response = session.post('', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)

    # If c_user cookie is present, login was successful
    if 'c_user' in response.cookies:

        # Make a request to homepage to get fb_dtsg token
        homepage_resp = session.get('')

        dom = pyquery.PyQuery(homepage_resp.text.encode('utf8'))
        fb_dtsg = dom('input[name="fb_dtsg"]').val()
        for k,v in response.cookies.iteritems():
            print k+":"+v

        return True, response, homepage_resp
        #return fb_dtsg, response.cookies['c_user'], response.cookies['xs']
    else:
        return False, False, False


def call_login(email, password):

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('email', help='Email address')
    parser.add_argument('password', help='Login password')

    session = requests.session()
    session.headers.update({
        ''
    })

    flag, res, home = login(session, email, password)

    if flag == True:
        print "Login Success"
        return res, home
    else:
        print 'Login Failed'
