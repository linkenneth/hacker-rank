# Enter your code here. Read input from STDIN. Print output to STDOUT

def sanitize_email(email):
    username, domain = email.split('@')
    username, domain = username.lower(), domain.lower()
    username = username.split('+')[0]
    username = username.translate(None, '.')
    return '%s@%s' % (username, domain)

def sanitize_street(street):
    street = street.lower()
    street = street.replace('street', 'st.')
    street = street.replace('road', 'rd.')
    return street

def sanitize_city(city):
    return city.lower()

def sanitize_state(state):
    state = state.lower()
    state = state.replace('illinois', 'il')
    state = state.replace('california', 'ca')
    state = state.replace('new york', 'ny')
    return state

def sanitize_zip_code(zip_code):
    zip_code = zip_code.translate(None, '-')
    return zip_code

N = int(raw_input())
email_deal_id = {}
address_deal_id = {}
fraudulent_orders = set()

for n in xrange(N):
    order_id, deal_id, email, street, city, state, zip_code, cc = raw_input().split(',')
    order_id, deal_id = int(order_id), int(deal_id)
    email = sanitize_email(email)
    street, city, state = sanitize_street(street), sanitize_city(city), sanitize_state(state)
    zip_code = sanitize_zip_code(zip_code)

    if (email, deal_id) in email_deal_id:
        cc_order_list = email_deal_id[(email, deal_id)]
        for old_cc, old_order_id in cc_order_list:
            if cc != old_cc:
                fraudulent_orders.add(order_id)
                fraudulent_orders.add(old_order_id)
                break
        cc_order_list.append( (cc, order_id) )
    else:
        email_deal_id[(email, deal_id)] = [(cc, order_id)]

    if (street, city, state, zip_code, deal_id) in address_deal_id:
        cc_order_list = address_deal_id[(street, city, state, zip_code, deal_id)]
        for old_cc, old_order_id in cc_order_list:
            if cc != old_cc:
                fraudulent_orders.add(order_id)
                fraudulent_orders.add(old_order_id)
                break
        cc_order_list.append( (cc, order_id) )
    else:
        address_deal_id[(street, city, state, zip_code, deal_id)] = [(cc, order_id)]

print ','.join(sorted(str(id) for id in fraudulent_orders))
