import argparse
import requests
import pyquery

def login(session, email, password):
    '''
    Attempt to login to Facebook. Returns user ID, xs token and
    fb_dtsg token. All 3 are required to make requests to
    Facebook endpoints as a logged in user. Returns False if
    login failed.
    '''

    # Navigate to Facebook's homepage to load Facebook's cookies.
    response = session.get('https://m.facebook.com')

    # Attempt to login to Facebook
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)

    # If c_user cookie is present, login was successful
    if 'c_user' in response.cookies:

        # Make a request to homepage to get fb_dtsg token
        homepage_resp = session.get('https://m.facebook.com/home.php')

        dom = pyquery.PyQuery(homepage_resp.text.encode('utf8'))
        fb_dtsg = dom('input[name="fb_dtsg"]').val()
        for k,v in response.cookies.iteritems():
            print k+":"+v

        return True, response, homepage_resp
        #return fb_dtsg, response.cookies['c_user'], response.cookies['xs']
    else:
        return False, False, False


def call_login(email, password):

    parser = argparse.ArgumentParser(description='Login to Facebook')
    parser.add_argument('email', help='Email address')
    parser.add_argument('password', help='Login password')

    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
    })

    flag, res, home = login(session, email, password)

    if flag == True:
        print "Login Success"
        return res, home
    else:
        print 'Login Failed'