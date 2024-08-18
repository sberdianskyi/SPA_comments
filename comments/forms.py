from captcha.fields import CaptchaField
from django import forms

from comments.models import Comment, User, Reply


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'homepage']


class CommentForm(forms.ModelForm):
    user_form = UserForm()
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["username"] = self.user_form.fields["username"]
        self.fields["email"] = self.user_form.fields["email"]
        self.fields["homepage"] = self.user_form.fields["homepage"]

        self.order_fields(["username", "email", "homepage", "text", "captcha"])

    class Meta:
        model = Comment
        fields = ["text"]

    def save(self, commit=True):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        homepage = self.cleaned_data["homepage"]
        user, created = User.objects.get_or_create(
            username=username,
            email=email,
            defaults={"homepage": homepage},
        )
        self.instance.user = user
        return super().save(commit=commit)


class ReplyForm(forms.ModelForm):
    user_form = UserForm()
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields["username"] = self.user_form.fields["username"]
        self.fields["email"] = self.user_form.fields["email"]
        self.fields["homepage"] = self.user_form.fields["homepage"]

        self.order_fields(["username", "email", "homepage", "text", "captcha"])

    class Meta:
        model = Reply
        fields = ["text"]

    def save(self, commit=True):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        homepage = self.cleaned_data["homepage"]
        user, created = User.objects.get_or_create(
            username=username,
            email=email,
            defaults={"homepage": homepage},
        )
        self.instance.user = user
        return super().save(commit=commit)
