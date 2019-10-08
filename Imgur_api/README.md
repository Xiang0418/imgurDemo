# API 使用筆記

###取得相簿所有圖片網址

```python
api = API(client_id, client_secret)
api.get_album_image_urls('相簿ID')
```
![](images/albumId.png)<br>
取得Album Id

### 取得 favorites 的所有圖片網址

```python
client_id = 'YOUR ID'
client_secret = 'YOUR SECRET'
api = API(client_id, client_secret)
print(api.get_album_image_urls('Album ID'))
print(api.get_favorites_image_urls("UserName"))
```
####第一步
![](images/favorites1.png)

紅線的地方是你的UserName<br>
![](images/favorites2.png)<br>

```python
結果:
['https://i.imgur.com/EiX3ZLT.png']
['https://imgur.com/gallery/R2JcSdk', 'https://imgur.com/gallery/Ve0Ha59']

```