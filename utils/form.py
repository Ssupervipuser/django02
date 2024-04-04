from django import forms


class myModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # 添加样式装饰
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}





# from django import forms
#
#
# class myModelForm:
#     bootstrap_exclude_fields = []
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # 循环ModelForm中的所有字段，给每个字段的插件设置
#         for name, field in self.fields.items():
#             if name in self.bootstrap_exclude_fields:
#                 continue
#             # 字段中有属性，保留原来的属性，没有属性，才增加。
#             if field.widget.attrs:
#                 field.widget.attrs["class"] = "form-control"
#                 field.widget.attrs["placeholder"] = field.label
#             else:
#                 field.widget.attrs = {
#                     "class": "form-control",
#                     "placeholder": field.label
#                 }
#
#
# class BootStrapModelForm(myModelForm, forms.ModelForm):
#     pass
#
#
# class BootStrapForm(myModelForm, forms.Form):
#     pass

