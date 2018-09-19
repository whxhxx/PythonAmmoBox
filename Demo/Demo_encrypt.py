from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto import Random
from binascii import b2a_hex


# 1
# 要加密的明文
# data = '南来北往'
# # 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
# # 目前AES-128足够用
# key = b'this is a 16 key'
# # 生成长度等于AES块大小的不可重复的密钥向量
# iv = Random.new().read(AES.block_size)
#
#
#
# pass
# #
# # 使用key和iv初始化AES对象, 使用MODE_CFB模式
# mycipher = AES.new(key, AES.MODE_CFB, iv)
# # 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数
# # 将iv（密钥向量）加到加密的密文开头，一起传输
# ciphertext = iv + mycipher.encrypt(data.encode())
#
# # 解密的话要用key和iv生成新的AES对象
# mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
# # 使用新生成的AES对象，将加密的密文解密
# decrypttext = mydecrypt.decrypt(ciphertext[16:])
#
# d = decrypttext.decode("utf-8")
# pass

# # 2
# import hashlib
#
# # 待加密信息
# str = '这是一个测试'
#
# # 创建md5对象
# hl = hashlib.md5()
#
# # 此处必须声明encode
# # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
# hl.update(str.encode(encoding='utf-8'))
#
# hl2 = hashlib.md5()
#
#
# print('MD5加密前为 ：' + str)
# print('MD5加密后为 ：' + hl.hexdigest())

# 3
# from Crypto.Cipher import AES
#
# # 加密与解密所使用的密钥，长度必须是16的倍数
# secret_key = "ThisIs SecretKey".encode("utf-8")
# # 要加密的明文数据，长度必须是16的倍数
# plain_data = "Hello, World123!".encode("utf-8")
# # IV参数，长度必须是16的倍数
# iv_param = 'This is an IV456'.encode("utf-8")
#
# # 数据加密
# aes1 = AES.new(secret_key, AES.MODE_CBC, iv_param)
# cipher_data = aes1.encrypt(plain_data)
# print('cipher data：', cipher_data)
#
# # 数据解密
# aes2 = AES.new(secret_key, AES.MODE_CBC, iv_param)
# plain_data2 = aes2.decrypt(cipher_data)  # 解密后的明文数据
# dd = plain_data2.decode("utf-8")
# print('plain text：', plain_data2)


# 4 RSA
# from rsa import PrivateKey, PublicKey

# from common.mysql_utils import MysqlUtil
# from common import constant
# import rsa

# RSA = "rsa"

# key = rsa.newkeys(512)#生成随机秘钥
# privateKey = key[1]#私钥
# p_n = privateKey.n
# p_p = privateKey.p
# p_q = privateKey.q
# p_d = privateKey.d
# p_e = privateKey.e

# publicKey = key[0]#公钥

# remake_pri_key = PrivateKey(n=p_n, p = p_p, q = p_q, d = p_d, e= p_e)
# # file = "./mima.json"
# # set_json_config(file=file, section="rsa", key="public", value=publicKey)
# # set_json_config(file=file, section="rsa", key="private", value=privateKey)


# message ='sanxi Now is better than never.'
# print('Before encrypted:',message)
# message = message.encode()
# cryptedMessage = rsa.encrypt(message, publicKey)
# print('After encrypted:\n',cryptedMessage)

# message = rsa.decrypt(cryptedMessage, remake_pri_key)
# message = message.decode()
# print('After decrypted:',message)
