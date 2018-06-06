from wit import Wit
from flask import session

import json
import sys, os
import csv
from pprint import pprint

scheduler_file = os.path.join(sys.path[0], "app/wit/jobs.csv")

def write_schedule_jobs_to_csv(request):
    with open(scheduler_file, 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        #wr.writerow(mylist)

"""
def send(session_id, context, msg):
    print(msg)
    session['answer'] = msg
   """ 
def send(request, response):
    print(response['text'])
    print 123123
    print request
    print response
    session['answer'] = response['text']

def first_entity_value(entities, entity):
    """
    get the entity from entities available
    :param entities:
    :param entity:
    :return:
    """
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def greeting(request):
    """
    action for greeting
    :param request:
    :return:
    """
    context = request['context']
    try:
        context['contact'] = first_entity_value(request['context']['entities'], 'contact')
    except:
        context['contact'] = None

    print context
    return context

def conti(request):
    """
    this function just continues the flow, some actions do not need any modifications
    :param request:
    :return:
    """
    print request
    pass

def test(request):
    print request

def get_bill_details(request):
    """
    process the bill details of user
    :param request:
    :return:
    """

    print request

    context = request['context']
    print context
    try:
        telephone_number = first_entity_value(request['entities'], 'phone_number')
        with open(os.path.join(sys.path[0], "app/wit/static/users.json"), "r") as data_file:
            data = json.load(data_file)
        customer_billing = data[telephone_number]['last_month_billing']
        print customer_billing

        customer_type = data[telephone_number]['type_customer']
        if customer_type == 'postpaid':

            reply = "Our Initial Investigation shows that you're a " + data[telephone_number]['type_customer'] + " Customer and currently using " + data[telephone_number]['plan_details'] + " plan type."
            if customer_billing['roaming'] == 'True':
                reply += "You had used your cellphone while on roaming for which you were charged extra."
            elif customer_billing['data_exhaust'] == 'True':
                reply += "You had used your data network after your allocated limit was exhausted. You were charged for these services"
            elif customer_billing['subscribed'] == 'True':
                reply += "You had subscribed to some promotional services for which you were charged in extra."
        else:
            reply = "Our Initial Investigation shows that you're a " + data[telephone_number]['type_customer'] + ". We believe that this might be a mistake from our side and would like you to speak to our customer care executives separately."


    except:
        telephone_number = None
        reply = "Your number is not subscribed with Airtel. Please contact your network operator for your query"


    print reply

    context['bill_details'] = reply

    return context


def in_out(request):
    print "In in and out functoin"
    print request


def schedule_callback(request):
    """
    This is used to log the requests to files which can later be analysed by our service engineers
    :param request:
    :return:
    """
    print "In schedule function"
    print request

    context = request['context']
    try:
        context['pincode'] = first_entity_value(request['context']['entities'], 'phone_number')
    except:
        context['pincode'] = None

    schedule_details = ['Pincode Network Issues']

def datapack_details(request):
    """
    process the datapack details
    :param request:
    :return:
    """
    print 'get datapack details'

    context = request['context']
    print context
    try:
        telephone_number = first_entity_value(request['entities'], 'phone_number')
        with open(os.path.join(sys.path[0], "app/wit/static/users.json"), "r") as data_file:
            data = json.load(data_file)
        network_details = data[telephone_number]['data_details']
        print network_details



        reply = "Our Initial Investigation shows that you're are currently using " + network_details['network_services_available'] + " and have subscribed for " + network_details['network_services_subscribed'] + "."
        if network_details['megabytes_available'] == 0:
            reply += " You have exhausted your datapack. Change your network settings to use pay2go plan or recharge now with available datapacks. Please check http://www.airtel.in/Airtel3G/tariff.html"
        elif network_details['network_services_available'] != network_details['network_services_subscribed']:
            reply += " Your subscribed datapack settings does not match with services available. Please change your network settings"

    except:
        telephone_number = None
        reply = "Your number is not subscribed with Airtel. Please contact your network operator for your query"

    context['datapack'] = reply

    return context



# actions
actions = {
    'send': send,
    'greeting': greeting,
    'test_intent': test,
    'post_pre': conti,
    'in_out': in_out,
    'mall_other': conti,
    'home_office': conti,
    'under_above':conti,
    'get_bill_details': get_bill_details,
    'area_outdoor': conti,
    'schedule_request' : schedule_callback,
    'get_datapack_details': datapack_details,
    'time': conti,
}

# Client key of my wit.api app
client = Wit('JBAOZNWZAHBPJBAR5GF2NOBB37AOVIN3', actions)
#client.interactive()