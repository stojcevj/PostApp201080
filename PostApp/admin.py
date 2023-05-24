from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Post, BlockedPostUsers, PostComment
from django.core import serializers


class MyUserAdmin(UserAdmin):
    list_filter = ()
    list_display = ('username',)

    def has_change_permission(self, request, obj=None):
        if request.user == obj or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)


class BlockedPostUsersAdmin(admin.StackedInline):
    model = BlockedPostUsers
    extra = 0


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("comment_user", "comment_timestamp", "comment_content", "comment_post_id")

    def has_change_permission(self, request, obj=None):

        if obj is None:
            return True
        if request.user == obj.comment_user or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        if Post.objects.filter(id=obj.comment_post_id.id).values().get()['post_user_id'] == request.user.id:
            return True
        if request.user == obj.comment_user or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        if obj is None:
            return True
        if Post.objects.filter(id=obj.comment_post_id.id).values().get()['post_user_id'] == request.user.id:
            return True
        if request.user == obj.comment_user or request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        obj.comment_user = request.user
        form.save()


admin.site.register(PostComment, PostCommentAdmin)


class PostCommentAdminInline(admin.StackedInline):
    model = PostComment
    extra = 0
    fields = ("comment_content", "comment_timestamp")

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False

    def has_view_permission(self, request, obj=None):
        return True


class PostAdmin(admin.ModelAdmin):
    inlines = [BlockedPostUsersAdmin, PostCommentAdminInline]
    search_fields = ["post_title", "post_content"]
    list_filter = ("post_created",)
    list_display = ("post_title", "post_user")

    def save_model(self, request, obj, form, change):
        obj.post_user = request.user
        form.save()

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True

        if request.user == obj.post_user or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True

        if request.user == obj.post_user or request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        blocked_users = BlockedPostUsers.objects.filter(post=obj).values_list('user_id', flat=True)
        if blocked_users.count() == 0:
            return True
        if request.user.is_superuser:
            return True
        if request.user.id in blocked_users:
            return False
        return True


admin.site.register(Post, PostAdmin)
