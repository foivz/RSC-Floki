import simplejson as json

__author__ = 'Davor Obilinovic'

def bar_chart(institutions):
    bar = []
    for institution in institutions:
        d = {
            "y":institution["Name"],
            "0-": institution.get0minus(),
            "0+": institution.get0plus(),
            "A-": institution.getAminus(),
            "A+": institution.getBplus(),
            "B-": institution.getBminus(),
            "B+": institution.getBplus(),
            "AB-": institution.getABminus(),
            "AB+": institution.getABplus()
        }
        bar.append(d)
    return json.dumps(bar)

# [{
#     y: '2006',
#     a: 100,
#     b: 90
# }, {
#     y: '2007',
#     a: 75,
#     b: 65
# }]