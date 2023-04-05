def question1(cash, exchange_rate, fee):
    '''
    Given an exchange rate, exchange money from one currency to another. For example, 
    the country of 1 US dollar can be exchanged for $1.5 Australian. 

    Fees are calculated before exchange, so 1 US dollar would be reduced to 0.9 US dollars. 

    '''
    return (cash-fee)*exchange_rate

print(question1(1, 1.5, 0.1))