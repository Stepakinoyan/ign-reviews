import json
import requests
from app.news.parser_settings import cookies, headers, params
from io import StringIO
from app.news.schema import FeedItem, ReviewContentFeed, Reviews
from newspaper import Article, Config
from fake_useragent import UserAgent


class ReviewsData:
    def __init__(self):
        self.config = Config()
        self.config.browser_user_agent = UserAgent().random

    def get_data_from_api(self):
        response = requests.get('https://mollusk.apis.ign.com/graphql', params=params, cookies=cookies, headers=headers)
        
        return response.text
    
    def get_article(self, url: str):
        article = Article(url, config=self.config)
        article.download()
        article.parse()


        return article.text
    
    def convert_str_data_to_json(self):
        api_data = self.get_data_from_api()
        io = StringIO(api_data)

        return json.load(io)
    
    def parse_content(self):
        converted_api_data = self.convert_str_data_to_json()
        model = ReviewContentFeed(**converted_api_data.get('data').get("reviewContentFeed"))

        return model.model_dump()
    
    def return_all_reviews(self):
        reviews = []
        content = self.parse_content()
        for item in content["feedItems"]:
            feeditem = FeedItem(**item)
            review = Reviews(**item, text=self.get_article(url=f"https://www.ign.com{feeditem.content.url}"))

            reviews.append(review.model_dump(mode="json"))
        
        return reviews
    
reviews = ReviewsData()


# with open("results.json", 'w') as file:
#     json.dump(reviews.return_all_reviews(), file, indent=4)