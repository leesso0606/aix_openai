from django.db import models

# Create your models here.
class Board(models.Model):
    bno =models.AutoField(primary_key=True)
    nickname =models.CharField(max_length=30) 
    btitle=models.CharField(max_length=1000)
    bcontent=models.TextField() #대용량 Text
    # 답변달기
    bgroup=models.IntegerField(default=0)
    bstep=models.IntegerField(default=0)
    bindent=models.IntegerField(default=0)    
    bhit=models.IntegerField(default=1)
    bdate=models.DateTimeField(auto_now=True, blank=True)
    bfile=models.ImageField(blank=True,upload_to='board') #upload폴더에 board폴더 생성후 저장

    def __str__(self):
        return f'{self.bno},{self.btitle},{self.bdate}'