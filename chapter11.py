import bs4, requests
def getPrice (productUrl):
    
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html.supports-no-cookies body.template__product.template--product.col-.add-to-cart-test-active main#MainContent.oo-main.global-banner-enabled div section.pdp-main.container.container--large div.product-right div.product-details form.product-form div.product-details div.price-and-stars.price-and-stars--wrap span.price-wrapper div.price-container span.flow-price.flow-price__item.actual-price.flow-localized span.money')
    elems[0].text
    return elems[0].text.strip()        #select method should return a list of match objects? why it isnt there?


price = getPrice('https://www.mvmtwatches.com/products/santa-monica')
print('The price is' + price)
