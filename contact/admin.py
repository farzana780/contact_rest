from django.contrib import admin
from .models import Contact_data, Email, Phone


class PostEmailAdmin(admin.StackedInline):
    model = Email


class PostPhoneAdmin(admin.StackedInline):
    model = Phone

@admin.register(Contact_data)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostEmailAdmin,PostPhoneAdmin]

    class Meta:
        model = Contact_data


@admin.register(Email)
class PostEmailAdmin(admin.ModelAdmin):
    pass


@admin.register(Phone)
class PostPhoneAdmin(admin.ModelAdmin):
    pass

