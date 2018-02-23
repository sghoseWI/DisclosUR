import sqlite3

def find_corps(legislators):
    '''
    Returns the unique (no exact matches) corporations 
    affiliated with legislators.

    Input: legislators (list) ['LAST, FIRST']
    Output: corporations (list)
    '''
    if legislators == None:
        return []
    db = sqlite3.connect('cpi.db')

    query = '''
            SELECT employer_business_interest
            FROM cpi
            WHERE lawmaker = ?
            '''
    for i in range(len(legislators) - 1):
        query += " OR lawmaker = ?"

    c = db.cursor()
    r = c.execute(query, legislators)
    corps = r.fetchall()
    db.close()
    return list({corp[0] for corp in corps})

def legislator_to_corps(legislators):
    '''
    Same as above, but returns a dict.
    '''
    rv = {}
    if legislators == None:
        return rv
    db = sqlite3.connect('cpi.db')

    query = '''
            SELECT employer_business_interest
            FROM cpi
            WHERE lawmaker = ?
            '''

    c = db.cursor()
    for legislator in legislators:
      print(legislator)
      r = c.execute(query, [legislator])
      corps = r.fetchall()
      corps = list({corp[0] for corp in corps})
      rv[legislator] = corps

    db.close()
    return rv