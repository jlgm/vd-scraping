# vd-scraping

A web scraper for Github repositories created in Python with BeautifulSoup.

## Requirements:
- Python 2.7
- Pip 10.0.1
- BeautifulSoup 4.4.0

## How to run:

- First install all dependencies with `make setup`
- Make sure the `repositories.txt` follows this format:
```
jlgm/QuakeParser
jlgm/vd-scraping
```
- Run with `make start`

## Example output:

```
jlgm/QuakeParser
5785 lines in total
242485 bytes in total
+-----------+------------+--------------+
| Extension |   Lines    |    Bytes     |
+-----------+------------+--------------+
|     md    |  89 (1%)   |  3681 (1%)   |
|    log    | 5307 (91%) | 227264 (93%) |
|     rb    |  386 (6%)  |  11510 (4%)  |
|  <other>  |   3 (0%)   |   30 (0%)    |
+-----------+------------+--------------+
[QuakeParser]
├── [log]
│   └── quake.log (5307 lines)
├── [spec]
│   ├── game_spec.rb (66 lines)
│   ├── parser_spec.rb (56 lines)
│   └── spec_helper.rb (92 lines)
├── [src]
│   ├── game.rb (54 lines)
│   ├── main.rb (41 lines)
│   └── parser.rb (77 lines)
├── .rspec (3 lines)
└── README.md (89 lines)
```

## Tests:

- TODO
