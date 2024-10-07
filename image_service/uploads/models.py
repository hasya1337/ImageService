from django.db import models


class Image(models.Model):
    image = models.ImageField("Uploaded Image", upload_to="uploads/")
    uploaded_at = models.DateTimeField("Uploaded At", auto_now_add=True)

    def __str__(self):
        return self.image.url
