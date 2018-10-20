from django import forms


class CreatePostForm(forms.Form):
    post_title = forms.CharField(label='Post Title', max_length=200)
    post_text = forms.CharField(label='Post Text', max_length=500)


class CreateCommentForm(forms.Form):
    comment_text = forms.CharField(label='Comment Text', max_length=500)
