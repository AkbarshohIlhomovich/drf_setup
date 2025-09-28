from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm
from django.utils.html import format_html
from django.urls import reverse, path
from django.utils.safestring import mark_safe
from django.shortcuts import redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.admin.views.main import ChangeList
from django import forms
from unfold.admin import ModelAdmin, TabularInline
from unfold.decorators import display
from unfold.widgets import UnfoldAdminTextInputWidget, UnfoldAdminEmailInputWidget
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Majburiy maydon",
        widget=UnfoldAdminEmailInputWidget()
    )
    first_name = forms.CharField(
        required=False,
        max_length=150,
        help_text="Ixtiyoriy",
        widget=UnfoldAdminTextInputWidget()
    )
    last_name = forms.CharField(
        required=False,
        max_length=150,
        help_text="Ixtiyoriy",
        widget=UnfoldAdminTextInputWidget()
    )
    phone_number = forms.CharField(
        required=False,
        max_length=20,
        help_text="Ixtiyoriy",
        widget=UnfoldAdminTextInputWidget()
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "phone_number", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = UnfoldAdminTextInputWidget()

        # Password fieldlar uchun Unfold styling
        unfold_input_class = 'border border-base-200 bg-white font-medium min-w-20 placeholder-base-400 rounded-default shadow-xs text-font-default-light text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-primary-600 group-[.errors]:border-red-600 focus:group-[.errors]:outline-red-600 dark:bg-base-900 dark:border-base-700 dark:text-font-default-dark dark:group-[.errors]:border-red-500 dark:focus:group-[.errors]:outline-red-500 dark:scheme-dark group-[.primary]:border-transparent disabled:!bg-base-50 dark:disabled:!bg-base-800 px-3 py-2 w-full max-w-2xl'

        password_attrs = {
            'class': unfold_input_class,
            'autocomplete': 'new-password'
        }
        self.fields['password1'].widget = forms.PasswordInput(attrs=password_attrs)
        self.fields['password2'].widget = forms.PasswordInput(attrs=password_attrs)

        self.fields['password1'].help_text = "Parol kamida 8 ta belgidan iborat bo'lishi kerak"
        self.fields['password2'].help_text = "Tasdiqlash uchun yuqoridagi parolni qayta kiriting"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phone_number = self.cleaned_data["phone_number"]
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class CustomAdminPasswordChangeForm(AdminPasswordChangeForm):
    password1 = forms.CharField(
        label="Yangi parol",
        widget=forms.PasswordInput(attrs={
            'class': 'border border-base-200 bg-white font-medium min-w-20 placeholder-base-400 rounded-default shadow-xs text-font-default-light text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-primary-600 group-[.errors]:border-red-600 focus:group-[.errors]:outline-red-600 dark:bg-base-900 dark:border-base-700 dark:text-font-default-dark dark:group-[.errors]:border-red-500 dark:focus:group-[.errors]:outline-red-500 dark:scheme-dark group-[.primary]:border-transparent disabled:!bg-base-50 dark:disabled:!bg-base-800 px-3 py-2 w-full max-w-2xl',
            'autocomplete': 'new-password'
        }),
        help_text="Parol kamida 8 ta belgidan iborat bo'lishi kerak"
    )
    password2 = forms.CharField(
        label="Parolni tasdiqlash",
        widget=forms.PasswordInput(attrs={
            'class': 'border border-base-200 bg-white font-medium min-w-20 placeholder-base-400 rounded-default shadow-xs text-font-default-light text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-primary-600 group-[.errors]:border-red-600 focus:group-[.errors]:outline-red-600 dark:bg-base-900 dark:border-base-700 dark:text-font-default-dark dark:group-[.errors]:border-red-500 dark:focus:group-[.errors]:outline-red-500 dark:scheme-dark group-[.primary]:border-transparent disabled:!bg-base-50 dark:disabled:!bg-base-800 px-3 py-2 w-full max-w-2xl',
            'autocomplete': 'new-password'
        }),
        help_text="Tasdiqlash uchun yuqoridagi parolni qayta kiriting"
    )


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    change_password_form = CustomAdminPasswordChangeForm

    list_display = ('get_profile_photo', 'username', 'email', 'get_full_name', 'phone_number', 'is_staff', 'date_joined')
    list_display_links = ('get_profile_photo', 'username')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')
    ordering = ('-date_joined',)
    list_per_page = 25
    list_max_show_all = 100

    filter_horizontal = ('groups', 'user_permissions')


    fieldsets = (
        (None, {'fields': ('username', 'password_change_link')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'profile_photo')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
            'classes': ('collapse',)
        }),
        ('Advanced permissions', {
            'fields': ('groups', 'user_permissions'),
            'classes': ('collapse',)
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'phone_number', 'profile_photo', 'password1', 'password2'),
        }),
        ('Permissions', {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )

    readonly_fields = ('last_login', 'date_joined', 'password_change_link')

    def password_change_link(self, obj):
        if obj.pk:
            try:
                change_password_url = reverse('admin:accounts_user_password_change', args=[obj.pk])
                return mark_safe(f'<a href="{change_password_url}" class="button" style="background: #417690; color: white; padding: 8px 16px; text-decoration: none; border-radius: 4px;">Parolni o\'zgartirish</a>')
            except:
                # Fallback to direct URL
                change_password_url = f"/admin/accounts/user/{obj.pk}/password/"
                return mark_safe(f'<a href="{change_password_url}" class="button" style="background: #417690; color: white; padding: 8px 16px; text-decoration: none; border-radius: 4px;">Parolni o\'zgartirish</a>')
        return "User yaratilgandan keyin parolni o'zgartirish mumkin"
    password_change_link.short_description = "Parol"

    @display(description="Profile Photo")
    def get_profile_photo(self, obj):
        if obj.profile_photo:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius: 50%; object-fit: cover;" />',
                obj.profile_photo.url
            )
        return format_html(
            '<div style="width: 40px; height: 40px; border-radius: 50%; background: #6c757d; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">{}</div>',
            obj.username[0].upper() if obj.username else 'U'
        )

    @display(description="Full Name")
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or "-"


