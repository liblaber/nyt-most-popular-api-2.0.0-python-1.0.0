from nyt_most_popular import NytMostPopular, Environment

sdk = NytMostPopular(api_key="", base_url=Environment.DEFAULT.value)

result = sdk.most_popular.get_emailed_period_json(period=1)

print(result)
