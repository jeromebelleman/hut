import datetime

colours = [
    '#7EB26D', '#EAB839', '#6ED0E0', '#EF843C', '#E24D42', '#1F78C1',
    '#BA43A9', '#705DA0', '#508642', '#CCA300', '#447EBC', '#C15C17',
    '#890F02', '#0A437C', '#6D1F62', '#584477', '#B7DBAB', '#F4D598',
    '#70DBED', '#F9BA8F', '#F29191', '#82B5D8', '#E5A8E2', '#AEA2E0',
    '#629E51', '#E5AC0E', '#64B0C8', '#E0752D', '#BF1B00', '#0A50A1',
    '#962D82', '#614D93', '#9AC48A', '#F2C96D', '#65C5DB', '#F9934E',
    '#EA6460', '#5195CE', '#D683CE', '#806EB7', '#3F6833', '#967302',
    '#2F575E', '#99440A', '#58140C', '#052B51', '#511749', '#3F2B5B',
    '#E0F9D7', '#FCEACA', '#CFFAFF', '#F9E2D2', '#FCE2DE', '#BADFF4',
    '#F9D9F9', '#DEDAF7',
]

def include(path):
    with open(path) as fhl:
        return fhl.read().replace('\n', '\\n')

def now():
    return datetime.datetime.now().strftime('%c')

def pulldowns(enable=True):
    return '''"pulldowns": [
    {
      "type": "query",
      "collapse": true,
      "enable": %s
    },
    {
      "type": "filtering",
      "collapse": true,
      "enable": %s
    }
  ]''' % (str(enable).lower(), str(enable).lower())

def nav(enable=True):
    return '''"nav": [
    {
      "type": "timepicker",
      "enable": %s,
      "timefield": "@timestamp",
      "filter_id": 0
    }
  ]''' % str(enable).lower()

def loader():
    return '''"loader": {
    "save_gist": true,
    "save_default": false,
    "load_gist": true,
    "load_local": true
  }'''

def links(path):
    with open(path) as fhl:
        contents = fhl.read().replace('\n', '\\n').replace('"', '\\"')

    # HTML mode to support &bull;
    return '''{
      "height": "0px",
      "panels": [
        {
          "span": 12,
          "title": "Links",
          "content": "%s",
          "type": "text",
          "mode": "html"
        }
      ]
    }''' % contents
