# Generated by Django 3.2.4 on 2022-03-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASsAAACoCAMAAACPKThEAAAAV1BMVEWZmZn///+WlpaUlJSRkZH7+/vX19fn5+fHx8fDw8O9vb2zs7O+vr709PTS0tKcnJzu7u6jo6Orq6vh4eG3t7fi4uLx8fGurq7V1dXq6uqnp6fNzc2KiooGKZhbAAAKuklEQVR4nO1d6YKrLAyVBNz3pVad93/Oj7DYZWrn9sf9Orfk/BnrIMoxhABJjCIGg8FgMBgMBoPBYDAYDAaDwWAwGAwGg8FgMBgMBoPx/wMAkKD/vvtRfjMAZbSO6XaO47je8rkhxt79UL8RIKM8PokbqCntJTJdNwDZpK14CBXPzNYFIOfpMVEW1WzJ6t78nO8HyOJApHb0hitUdeACJtflB6bEJE3BWITNFcD5J6aEWIkiKIQoQuYK++pWkSdxmo/zPJZb3Cp3cjBiBUqokKmS6U1XyzqQZIMaoIQ1Teh8Y4oOQsT47gd+H6j9HksJ8l5sQJ9KqzMxBLkuE/A4iBelPvXfiHJwU51GF0rk//l0vwqwG+ntIVMecvEqPkjgblRlPzEVYbpbDiFCJl6omovG1h2u6fr1vix0ImRtJb1ZFV+ECqDIyqJvvhem3lqHOgiaYY2Q7h0Lu62eHy5aYU2WV7DKqttVlTuBXVw3j9cToKeSeahcyfaWKsB66I76GKqQ7QXILFW1p2pt80Mu9JQ5ZMUeOQPU8SPzqjnsYTBS0S1UxY52DPTaWm7tMyao6ClUqsx8RcMtdspteaKLpFkw7a7ELigdb0wAMqzsr+z0hCrUmq3aLvwA9tt3++uDYcXKHsOsnpSE9XoGBDLahiwPyHpwg2DqVJBbSz8oq9xCnwbimLTZNoxZOIJlbSun2GXybOqi54xe6mR3VlM6JON2LsIRLKvZrREAhXpG1ebNdegSMW2ntoyTPE6DoQrssrHtR6jG44aTZeXMdeJXLelQZfFwbIp9HOxajDVDIa+Ox0CzEGMplTRyTonY4qoIaa4DRqysOMnqierRet0OACDN5FkkZ7H9uCr4SbCLBgLc8XHTSf7IXAdZ+FXB4WpVMIT5obUYrBrC+HgTy3S7FTBKaQMxPp/UtF53vy4AwwHNqsFmu6A63EdGmjGfv1ZTOm4Q5Z1rUfdtofnzYFW75WgVR4qa7HWhcmOJLeujUhDAdj2e9tUoeDIT9Nvzohofq3N4Ymx8Cmh0c0b7sbq6bIelh1usZQBcGWGxqn3ZHrfX6rS7ge++niwQruyCFVaPZcOZFQeKyhfK/s7z/SoYk8GICx64U5GjlbatHisqb1dB+rce8PfAyNXwlKsIFlGVB4qqc2TB9nee7zfBcDU95yrC7tDzePVcnT9fX2F1MdvV6wtRMAfElVnpOznd/vpKFORuboPD53OFtC9jF/gwed2nEUp/MHz+NpjdxDHCgednm12PAV4UmwC4sg4yZj9CH77OlTNfoQjB1d14yFiju3u6h/MQqzPXYQthg0Kq3cCS1atuCpC6pRhcQljsQ/LTVnYgPD9Zbj+42JELr175T8L6vfSuE84v9STovboqwwgLQON5ZTth+5pvsZycdSXbAJb6It8J7Vbq+JLPOqy+C3avj6D/JGC+2vQ6vWJiSa/Q8RxGF3TTHMsR9C/4zEK+MxSMS6Q1R61Wl7H44+uaytGK9esG/78KSWsNrW0uqPYP2y1PXp83r9uw/yys2eA8YFbv4PcD5OC9j+QQjli5TULngYWj2P6g6TL2Hu5QhBXwZSaFg3cY3f3cjyHjS1cV50AGQQsT4yZy22ZZiul5tgqAZPH8yCS0yBy7Ve/6EhaiWp/59/Vq12lyC0ixe5j9Z+eMDc1JbEeiBXgWewQK5gGGUBjvDlH5EDgKqM/wAQsImUh2t0dN1RDQGOjhdky9mz82sVBbc+M5BCi7Wly5PcpRPA1H+VgYFytR7eEjGNVKVHXRgJTkbwXNeK5EMl82VbXwnYLTVRaWLDFfIlNxjsmkr5YkaelgypqrCF89H2oDpUpzM1tX9ys+EKEv0zqut6ygrGpXhbvK7VeHCehMNpn2xiHG5Ee5z9YHFBfws8n6yQDnahVHTyUGZKFJHYOmSkMW1t1xaw5d120usSmgeIkjANTOiW9+kMUQKJFfZdxG3/Fwvw5kWhmouGik11QmqxOuKSWSUT9nUQkG2NTe8fg0pPm8dl3Xj9k5MWfbnJOMXgPlOOx+2teo6pVl6h6gLastueHrNGTdozkig1QU5Z0byyxNy7zo7sNKGPfw6fqYJgaDwWAwGAwGg8FgMBgMBoPBYIQBoC2Wfftg33C59gLSwP3I/3Dl5b73YP7rD6OrauwdfMgguj+39ZjfEN1XdHsH/5TvWsWHjaKuWpdTVcYuBqtRPisOlq0Q6txABGN7Mkh8I6Gj7cBkNmRQnqtqo3ZAfnKRNs0pByhaiDB2n10aE6oXx4U2qHcPN1gnJVoTMQ6wVUK0JV7uoAbjswttZl9Z/aYoaSSXc3B5nSH3SRdqF3QaYSK2uc8q0URQijEn+KRVOIpkXMeJPmYGplwqVGMy1NmYCLmIFHSlYKqhU7oOMCmM6rnXL8HF8kIv4nnejGtko1Taz7VYDKe5uwOxBC78B4c3Rd87riqbL1z/ta9fFDZ6RA6iId8ELICY/LreyNItzKT+JfMc5KBMOWgrNNn8qHGUMnrnqjUBdFAq/WMTHRWWO+lToivCaKXUGK25X0Put/sdMkrEAqI1IVLv5qogJ2qZLJuJQIa0+qoNa53PFgPfswvIxQWM6NasLuILGlECZFVJyRsaMaqdq3oj2TVcgcjQV2ofYvF+yZpmn46AciL6iFc5VPSUc0uv9N1c9bl+1bloasMVam3VUOthM13RChPJlfm2rru0uWTdgdpHecshQcjUV9tK2SZfF67ir6SyXJkTvlJ7earlz6hzzZqPbVIbNj6SWgtYB/qNAoVIvZurWU4n/bqlabNuDOonSuixSI9DvW1bTm1MCK0NV9aytGe8xMk7gWp2iSup5asUusEXrhDUJIkrNMILm651H0Bqrc7rTt9VpXu/HOR8CUvUPGmusBclvp0riIRaJBquZLVJlKvoNFekpGEahkqLSy6ylOAoWi9xpThcuKoMV6SrcsAbrjqRSpIry9UwDKc95wBGeaxEiqh8RjtMBtnfcwW62lW+nSsYtZgYrmAWuh1DLHTzUqOiEGVsuPq68VG4RO7C5lWZTAbDlT7QuuaGKxo351zRnSJbaXqVn0FbWFqjyckHzRkJcwHVpL0a0qpAg80vkCvowXKlVXxNiEWjtdZosxFZrm50O06uqXoEa1y4F9BgYLgyudNuuaJPWmU0DrrvNMHOlbUyUd9sdF+lIOWpr3L5OM0wYrjSA2USv50r80tzRXrIqHBZ1agVSU/DOSZWrvBWuQ+IYGROmwGFLic7yr1tuTL13XJFBhcp+MwU1hd6rk65ts21euoodKyjigqTcbrzd6DubrmizOZvir/HmF7dNVdGqRPM+K3NxikrtWmqe2kp6LPp8Z5QVI9Oqs5qRW3QpC5bOhhHf32h52q3rxZ3kaK4Qc1skuX6Qt/FUlHVWWzCL7VRO6TbYgPB6A5nugNF0IEtTiriPVxBTso09gb0qCcp8R7aF/e6XWu8tEOuewnMscOupiBNTlNqNJgtZ0JNYPaTEKh1j+x1eUh9YLT5F3a1Llzuqg+jdEji2aYRKYZ2ObtvXek7TPoOto+e7VNi+a4Mrrah178ufnhWBeneaE+B7YF3QVz7jHYvdzW5BT933k0p+Hahvxqv/nX1McOrO1w/MoPBYDAYDAaDwWAwGAwGg8FgMBgMBoPBYDAYjF+O/wAAk2NcPy25RgAAAABJRU5ErkJggg==', max_length=5000),
        ),
    ]
