import bs4, requests


def getPrice (productUrl, headers):
    
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-transform3d.-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.a-ember.a-ws body.a-m-us.a-aui_149818-t1.a-aui_152852-c.a-aui_157141-c.a-aui_158613-c.a-aui_160684-c.a-aui_57326-c.a-aui_72554-c.a-aui_accessibility_49860-c.a-aui_attr_validations_1_51371-c.a-aui_bolt_62845-c.a-aui_perf_130093-c.a-aui_tnr_v2_180836-c.a-aui_ux_113788-c.a-aui_ux_114039-c.a-aui_ux_145937-c.a-aui_ux_60000-c.a-meter-animate div#a-page div#dp.book.en_US div#dp-container.a-container div#rightCol div#unifiedBuyBox_feature_div.feature div#combinedBuyBox.a-section.a-spacing-medium form#addToCart.a-content div#buybox.a-row.a-spacing-medium div.a-box-group div.a-box.rbbSection.selected.dp-accordion-active div.a-box-inner div.a-section.a-spacing-none.a-padding-none div#buyNewSection.rbbHeader.dp-accordion-row h5 div.a-row div.a-column.a-span8.a-text-right.a-span-last div.inlineBlock-display span.a-size-medium.a-color-price.offer-price.a-text-normal')
    elems[0].text
    return elems[0].text.strip()


price = getPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994', {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; W…) Gecko/20100101 Firefox/65.0'})
print('The price is' + price)
