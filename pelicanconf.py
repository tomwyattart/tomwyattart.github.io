AUTHOR = 'Tom Wyatt'
SITENAME = 'Tom Wyatt'
SITEURL = 'https://tomwyatt.art'

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'EN'

PLUGINS = [
    'pelican_youtube',
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Buy me a coffee', 'https://www.buymeacoffee.com/tomwyatt'),
         ('My GitHub account', 'https://github.com/tomwyattart'), )

# Social widget
SOCIAL = (('Reddit', 'https://www.reddit.com/user/TomWyattArt'),
          ('Twitter', 'https://twitter.com/TomWyattArt/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
