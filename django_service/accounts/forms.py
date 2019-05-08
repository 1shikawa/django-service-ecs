from django import forms


class ContactForm(forms.Form):
    """お問い合わせフォーム"""
    name = forms.CharField(label='お名前', max_length=255)
    email = forms.EmailField(label='メールアドレス')
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)

    # すべてのfieldのclass属性に'form-control'を指定する
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # Bootstrap4対応
