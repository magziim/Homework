# RSS reader

RSS reader is a command-line utility which receives RSS URL and prints results in human-readable format.

```
	python rss_reader.py ...
```

## --json
Example:
```	
	{
		"Title": "title",
		"Date": "2021-10-28 17:54:34",
		"Link": "link"
	}
```

## --date
It takes a date in %Y%m%d format. 
For example: 
	--date 20191020 
Here date means actual publishing date.

## --to_pdf
Convert caching articles to .pdf

## --to_html
Convert caching articles to .html

### How to run tests
```
python rss_parser/test_cacher.py
```

## News caching
If `--date` is passed, then news are always fetched from cache. 
If `--source` is passed together with `--date`, then news are fetched from cache only for specified source. 
Fresh news are fetched when only `--source` is passed without `--date`
