from yelpapi import YelpAPI


def findlocalRestaurants(lat, lng):
    apikey = "0mUxxplp8zsGAYPnrGKJj3fSdZyiFaxoe8N9jkwAzvAyM3mkyhrcSftbtLCnsFqlYTtpCUS6cl-G5k9UnofpTYE_iEonxxfnC_tGSFduhFzs4lqHR_jeF2Cma005XHYx"
    yelp_api = YelpAPI(apikey)
    search_results = yelp_api.search_query(latitude=lat, longitude=lng, categories="Restaurants", radius=8000)
    return search_results
