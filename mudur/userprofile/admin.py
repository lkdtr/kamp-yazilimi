from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from training.models import Course

from userprofile.models import (
    Accommodation,
    AgreementCategory,
    AgreementText,
    InstructorInformation,
    TrainessNote,
    UserAccomodationPref,
    UserAgreementInfo,
    UserFeedback,
    UserProfile,
    UserProfileBySite,
    UserVerification,
)

admin.site.unregister(User)


def make_needs_document(modeladmin, request, queryset):
    for obj in queryset:
        up = UserProfileBySite.objects.get_or_create(user=obj)
        up.needs_document = True
        up.save()


make_needs_document.short_description = "Seçili nesneleri evrak gerekiyor olarak işaretle"


def remove_needs_document(modeladmin, request, queryset):
    for obj in queryset:
        up = UserProfileBySite.objects.get_or_create(user=obj)
        up.needs_document = False
        up.save()


remove_needs_document.short_description = "Seçili nesnelerin evrak gerekiyor işaretini kaldır"


class UserVerificationInline(admin.StackedInline):
    model = UserVerification
    extra = 0


@admin.register(UserProfile)
class UserProfileAdmin(ForeignKeyAutocompleteAdmin):
    """Bu admin modeli admin arayuzunde gozukmeyecek
    fakat autocomplete'in calismasi icin register edilmesi gerekli"""

    search_fields = ["user__first_name", "user__last_name", "user__email"]

    def has_change_permission(self, request, obj=None):
        return True

    def get_readonly_fields(self, request, obj=None):
        fields = list(self.readonly_fields) + [field.name for field in obj._meta.fields]
        fields = list(set(fields))
        return fields

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0


class UserProfileBySiteInline(admin.StackedInline):
    model = UserProfileBySite
    extra = 0


class UserAgreementInfoInline(admin.StackedInline):
    model = UserAgreementInfo
    extra = 0
    readonly_fields = (
        "agreement",
        "date",
    )


class UserSiteFilter(admin.SimpleListFilter):
    title = _("Trainees Site")
    parameter_name = "treessite"

    def lookups(self, request, model_admin):
        return (
            User.objects.all()
            .values_list("userprofile__trainess__site__id", "userprofile__trainess__site__name")
            .distinct()
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(userprofile__trainess__site__in=self.value())
        else:
            return queryset


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = ["username", "first_name", "last_name", "tckimlikno", "gender"]
    list_filter = AuthUserAdmin.list_filter + (UserSiteFilter,)
    search_fields = ("username", "first_name", "last_name", "userprofile__tckimlikno")
    actions = [make_needs_document, remove_needs_document]
    inlines = [
        UserProfileInline,
        UserVerificationInline,
        UserProfileBySiteInline,
        UserAgreementInfoInline,
    ]

    def is_instructor(self, obj):
        if obj.userprofile:
            courses = Course.objects.filter(site__is_active=True, trainer=obj.userprofile)
            if courses:
                return True
        else:
            return False

    def tckimlikno(self, obj):
        return obj.userprofile.tckimlikno

    def gender(self, obj):
        return obj.userprofile.gender


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "gender",
    ]
    list_filter = ("gender",)


@admin.register(UserAccomodationPref)
class UserAccomodationPrefAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "usertype",
        "preference_order",
        "approved",
    ]
    list_filter = ("usertype", "preference_order", "accomodation")
    search_fields = ("user__user__username",)


@admin.register(InstructorInformation)
class InstructorInformationAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "transportation", "arrival_date", "departure_date"]
    list_filter = ("transportation", "arrival_date", "departure_date")
    search_fields = ("user__user__username",)


@admin.register(TrainessNote)
class TrainessNoteAdmin(admin.ModelAdmin):
    list_display = ["note_to_profile", "note_from_profile", "site", "note", "label"]
    list_filter = ("label",)
    search_fields = ("note_from_profile__user__username", "note_to_profile__user__username")


@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ["site", "title", "status", "creation_date"]
    list_filter = ("site", "creation_date", "status")
    search_fields = ("title", "body")
    readonly_fields = ("status", "title", "body", "user", "site", "attachment")
    fieldsets = (
        (
            "Geribildirim",
            {"fields": ("user", "site", "status", "title", "body", "attachment")},
        ),
        ("Cevap", {"fields": ("answer",)}),
    )

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = list(super().get_readonly_fields(request, obj))
        if obj and obj.status == UserFeedback.STATUS_CLOSED:
            read_only_fields.append("answer")
        return tuple(read_only_fields)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        user_feedback = get_object_or_404(UserFeedback, id=object_id)
        if user_feedback.status == UserFeedback.STATUS_NEW:
            user_feedback.status = UserFeedback.STATUS_PROCESSING
        user_feedback.save()
        return super().change_view(
            request,
            object_id,
            form_url,
            extra_context=extra_context,
        )

    def save_model(self, request, obj, form, change):
        if obj.answer:
            obj.status = UserFeedback.STATUS_CLOSED
        super().save_model(request, obj, form, change)


@admin.register(AgreementCategory)
class AgreementCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active"]
    search_fields = ("title",)


@admin.register(AgreementText)
class AgreementTextAdmin(admin.ModelAdmin):
    list_display = ["title", "version", "category"]
    list_filter = ("category",)
    search_fields = ("title", "body")
