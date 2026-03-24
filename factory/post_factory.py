from post.models import Post
from django.contrib.auth.models import User

class PostFactory:
    @staticmethod
    def create_post(author , content):
        
        #if post_type not in dict(Post.POST_TYPES):
         #   raise ValueError("Invalid post type")


        # Validate
        if not isinstance(author, User):
            raise ValueError("A valid author is required.")

        if not content or not str(content).strip():
            raise ValueError("Post content cannot be empty.")


        return Post.objects.create(
            author=author,
            content=content,
        )

