import simplejson as json

__author__ = 'Davor Obilinovic'

def bar_chart(institutions):
    sstr = "["
    _str = "["
    ys = []
    for institution in institutions:
        _y = "'"+institution.get_string_presentation()+"'"
        _str = _str+_y+","
        ys.append(_y)
        d = {
            "a": institution.get0minus(),
            "b": institution.get0plus(),
            "c": institution.getAminus(),
            "d": institution.getBplus(),
            "e": institution.getBminus(),
            "f": institution.getBplus(),
            "g": institution.getABminus(),
            "h": institution.getABplus()
        }
        sstr = sstr+"{y:"+_y+","
        for key in d.keys():
            sstr = sstr+key+":"+str(d[key])+","
        sstr=sstr.rstrip(',')+"},"
    _str = _str.rstrip(',')+"]"
    sstr = sstr.rstrip(",")+"]"
    return {"data":sstr,"y":[]}

# [{
#     y: '2006',
#     a: 100,
#     b: 90
# }, {
#     y: '2007',
#     a: 75,
#     b: 65
# }]