from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import random as rd
from datetime import date
app = Flask(__name__)



########Checklist###########

# clean the code
# comment the code
# make it user friendly
# make it secure

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    msg = request.form.get('Body')
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    # resp.message("The Robots are coming! Head for the hills!")


    # print("hello",request.method['GET'])




    def pass_gen():
        global pass_wrd
        pass_lst = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4',
                    '5', '6', '7', '8',
                    '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P',
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd',
                    'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|',
                    '}', '~']
        att = ''
        pass_wrd = att.join(rd.choices(pass_lst, k=8))
        del[att]



    # def pass_check(att_no):
    #     global msg
    #     if msg==pass_wrd:
    #         resp.message("login success.")
    #     if att_no==0:
    #         resp.message("pls regen the key")
    #     else:
    #         resp.message("try again you have {} attempts left".format(pass_wrd))
    #     att_no=att_no-1
    #     pass_check(att_no)





        # return 0
    def var_satrt():
        order_dict = {}

    def start():
        global order_dict




    def final_order():
        global order_fin
        order_fin = {}
        resp.message("started but in func")
        return 0


    a = msg.split()

    if msg=="start":
        # start()
        final_order()

        resp.message("started")


    elif a[0]=="order":
        var_satrt()
        start()
        for i in range(1,len(a),2):
            order_dict.update({a[i]:int(a[i+1])})
        x=order_dict
        resp.message("item    :    qunat.  ")

        for i in order_dict:
            resp.message("{}   :    {}".format(i,x[i]))

        resp.message("to conform order type  conf_ord")

    elif msg=="conf_ord":
        for i in order_dict:
            if i in order_fin:
                order_fin.update({i: order_fin[i] + order_dict[i]})
            else:
                order_fin.update({i: order_dict[i]})
        resp.message("order conformed")
        order_dict={}
    elif msg=="!order":
        resp.message("  {} ".format(order_fin))











    elif a[0] =="host":
        try:
            if a[1]==pass_wrd:
                resp.message("success")
            else:
                resp.message("try again")
        except:
            resp.message("password not genrated")


    # elif msg=="Send1":




    elif msg=="date":
        resp.message("{}".format(date.today()))


    elif msg=="help":
        resp.message("The commands are :\n"
                     "'start' - for starting food orders\n"
                     "'order\nitem_1 quant.\nitem_2 quant.'\n- for ordering food \n"
                     "'!order' - for getting total orders\n"
                     "'host *password*' - for becoming host\n"
                     )



    elif msg=="gen_pass":
        pass_gen()
        resp.message("password created")










    elif msg=="pass":
        try:
            resp.message("{}".format(pass_wrd))
        except:
            resp.message("please gen the pass first")
    else:
        # resp.message("{}".format(msg))
        print(msg)
        resp.message("Your resp: \n{}".format(msg))


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)