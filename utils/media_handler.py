import cloudinary.uploader as uploader
from cloudinary.api import delete_resources
from rest_framework.exceptions import ValidationError
from django.utils.datastructures import MultiValueDictKeyError

class CloudinaryResourceHandler:
    """This class contains methods for handling Cloudinary
    Resources, ie images and vidoes."""
    def upload_image(self, image):
        """Upload an image to cloudinary and return the url.
        The image should be an instance of Django's UploadedFile
        class. Read more about the UploadedFile class here
        https://docs.djangoproject.com/en/2.2/ref/files/uploads/#django.core.files.uploadedfile.UploadedFile
        Image file is first validated before being uploaded.
        """
        try:
            result = uploader.upload(image)
            url = result.get('url')
            return url
        # Cloudinary might still throw an error if validation fails.
        except Exception as e:
            raise ValidationError({
                'image':
                ('Image is either corrupted or of an unkown format. '
                    'Please try again with a different image file.')
            }) from e
    def upload_image_from_request(self, request):
        """Upload an image directly from a request object.
        params:
            request - incoming request object
        Return:
            the url if upload is successful.
        """
        try:
            image_main = request.FILES['image']
            if image_main:
                url = self.upload_image(image_main)
                return url
        except MultiValueDictKeyError:
            # This error will be raised if `image_main` is not an
            # uploaded file. There is no need to raise an error in that
            # case
            pass