"""Website function creates an html page with a link to Nasa image of the day"""

# Tommy May
# A01086435

import requests, json


def website():
    """ Creates an html page with a link to Nasa image of the day

    POSTCONDITION: an html page called index is created with a link to Nasa image of the day
    """
    url = 'https://api.nasa.gov/planetary/apod?api_key=tubHcfkXSjslikbUgyI8vmuOCcIQG9vmwnFAejSM'
    response = requests.get(url)
    response.raise_for_status()
    nasa_info = json.loads(response.text)
    nasa_url = nasa_info['url']

    name = input('Enter your name')
    description = input('Write a sentence to describe yourself')
    with open('index.html', 'w') as f_obj:
        contents = '<!doctype html>\n'\
                   '<html lang = "en">\n'\
                   '<head>\n'\
                   '<meta charset = "utf-8">\n'\
                   '<title> Introduction </title>\n'\
                   '<meta name = "description" content = "User’s webpage">\n'\
                   '<meta name = "author" content = name>\n'\
                   '<link rel = "stylesheet" href = "css/styles.css?v=1.0">\n'\
                   '</head>\n'\
                   '<body>\n'\
                   '<center>\n'\
                   '<h1>' + name + '</h1>\n'\
                   '</center>\n'\
                   + description + '<br>\n'\
                   '<a href =' + nasa_url + '> link to nasa Image Of The Day</a>\n'\
                   '</body>\n'\
                   '</html>\n'
        f_obj.write(contents)


def main():
    website()


if __name__ == "__main__":
    main()
