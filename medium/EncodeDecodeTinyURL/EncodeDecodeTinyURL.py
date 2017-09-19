# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
class Codec:

    def __init__(self):
        self.urls = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        urlKey = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(6))
        while self.urls.has_key(urlKey):
            urlKey = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(6))
        self.urls[urlKey] = longUrl
        return urlKey

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))