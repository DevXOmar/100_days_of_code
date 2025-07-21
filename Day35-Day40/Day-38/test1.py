import datetime as dt
data = {'exercises': [{'tag_id': 63, 'user_input': 'swam', 'duration_min': 10, 'met': 6, 'nf_calories': 70, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise//63_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise//63_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 18310, 'name': 'swimming', 'description': None, 'benefits': None}]}
EXERCISE = data["exercises"][0]["name"]
TIME = data["exercises"][0]["duration_min"]
CALORIES = data["exercises"][0]["nf_calories"]

print(EXERCISE)