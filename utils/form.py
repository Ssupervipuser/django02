from django import forms


class myModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # 添加样式装饰
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}
