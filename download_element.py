import bs4, requests


def getPrice (productUrl):
    
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html body.appdomain-45 div#page-wrapper div#react-container div#inner-wrapper.campaigns-page.touch-device div.articleDetailsWrapper___wrapper___bQc6g.core___container___JLara div section.articleDetailsWrapper___image-info-wrapper___1pNOr section.ArticleInformation___wrapper___23R3G div.articlePrice___wrapper___1J5gR div div.articlePrice___special___D3rkB span span')

    # Dlaczego nie pokazuje listy elementów, tylko [] ??

    elems[0].text
    return elems[0].text.strip()


price = getPrice('https://www.zalando-lounge.pl/campaigns/ZZLR41/categories/5435792/articles/ZZLJ2S028-G00')
print('The price is' + price)
