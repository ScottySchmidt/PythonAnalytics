'''
Apple Product Counts https://platform.stratascratch.com/coding/10141-apple-product-counts?code_type=2

Find the number of Apple product users and the number of total users with a device and group the counts by language. 
Assume Apple products are only MacBook-Pro, iPhone 5s, and iPad-air. Output the language along with the total number of Apple users and users with any device. Order your results based on the number of total users in descending order.

'''

import pandas as pd

# Original Two Datasets:
df = playbook_events
df2 = playbook_users

# JOIN:
joinDF=df.merge(df2, on='user_id', how='inner')

# Apple Data:
appleDF= joinDF[joinDF['device'].isin(['macbook pro', 'iphone 5', 'macbook air'])]
apple_count_df = appleDF.groupby('language')['user_id'].size().reset_index(name='apple_users')

# Total Data:
total_count_df = joinDF.groupby('language')['user_id'].size().reset_index(name='total_users')

# Languages Join Together:
finalDF=apple_count_df.merge(total_count_df, on='language', how='inner')
finalDF.sort_values('total_users', ascending=False)
finalDF
