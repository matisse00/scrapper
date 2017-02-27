# scrapper

If you want to run app by docker-compose use:
```
docker-compose up -d db
docker-compose up web
```
In `blogscrapper/settings.py` you can make your own scrapper settings.
```
SITE_CONFIG = {
    'name': 'build.sh' # put your spider name here
    'allowed_domains': ['build.sh'], # put your domains in this array
    'start_urls': ['http://build.sh/kickstarter-we-are-a-backer/'], # put your urls in this array
    'text_selector': 'article section.post-content p::text', # put your post-text selector
    'author_selector': 'footer.post-footer span.author-content h4::text', # put your post-author selector
    'next_page_selector': 'li.pull-right a::attr(href)' # put selector to next page
}
```
Change your database settings in `blogscrapper/settings.py` and `web/web/settings.py` (change `'host'` to `'localhost'` if you want to use app local.)

If you already have postgres client on port 5432 and you cannot run db container try `sudo service postgresql stop`
