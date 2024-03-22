
# 0xpH Scrapper

Membuat ip:port proxy ke protocol://ip:port 
```git
git clone https://github.com/0xpH/Scrapper.git
```
```
merge.py to all txt file and store it to /proxy
```
```
fresh.py to delete all txt file in the main directory
```
## Acknowledgements

 - [Yakumo](https://github.com/elliottophellia/yakumo)
 - [Proxy](https://github.com/search?q=proxy+scraper&type=repositories&s=updated&o=desc)
 

## Contoh


```python
python main.py https://yakumo.rei.my.id/SOCKS4 socks4:// socks4.txt
```

```python
python main.py https://yakumo.rei.my.id/SOCKS5 socks5:// socks5.txt
```
```python
python main.py https://yakumo.rei.my.id/HTTP http:// http.txt
```
```python
python main.py https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt http:// http2.txt
```

```python
python main.py https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt https:// https.txt
```

```python
python main.py https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt socks5:// socks5.txt
```
```python
python main.py https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt socks4:// socks42.txt
```
