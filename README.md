# PxlsBot
It's simple a bot for pxls.space.

Installation:

    git clone https://github.com/Vavilontw/PxlsBot

    cd PxlsBot

    pip install -r requirements.txt

Launch:

    python main.py -t "token" -file "path_to_art" -x "art x" -y "art y" -p "pattern" [optional] -ua "user_agent" [optional]

or:

    python main.py -t "token" -link "template_link" -p "pattern" [optional] -ua "user_agent" [optional]

Getting Token

Your token is a cookie. To get this cookie, go to the Pxls site, open up the developer tools menu, switch to the Application tab (it may be collapsed, if so use the double arrow next to the other tab names), under storage click Cookies, then the website domain, and finally find the row with pxls-token, and copy the value next to that.

