
# 0xpH Scrapper

Convert ip:port proxies to protocol://ip:port.

## How to use:
1. Clone this repo:
```git
git clone https://github.com/0xpH/Scrapper.git
```

2. Run:
```python
py main.py https://yakumo.rei.my.id/SOCKS4 socks4 socks4.txt
```

```python
py main.py https://yakumo.rei.my.id/SOCKS5 socks5 socks5.txt
```
```python
py main.py https://yakumo.rei.my.id/HTTP http http.txt
```

Another Features:
1. merge.py to all txt file and store it to /proxy
```
py merge.py
```

2. fresh.py to delete all txt file in the main directory
```
py fresh.py
```
3. split.py to split all proxies list into 2k each files.
```
cd proxy && py split.py
```

## Sources:
 - [Yakumo](https://github.com/elliottophellia/yakumo)
 - [Proxy](https://github.com/search?q=proxy+scraper&type=repositories&s=updated&o=desc)
 

