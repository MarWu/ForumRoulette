from django import forms


class CreatePostForm(forms.Form):
    post_title = forms.CharField(label='Post Title', max_length=200)
    post_text = forms.CharField(widget=forms.Textarea, label='Post Text', max_length=500)
    post_image = forms.ImageField(label='Post Image (optional)', required=False)


class CreateCommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea, label='Comment Text', max_length=500)
