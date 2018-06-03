class AgreementMiddleware(object):
    def process_request(self, request):
        from userprofile.models import AgreementText, AgreementCategory, UserAgreementInfo
        from django.shortcuts import redirect
        from django.urls import reverse
        if request.path == reverse("accept_agreement"):
            return

        if request.user.is_authenticated:
            categories = AgreementCategory.objects.filter(is_active=True)
            for category in categories:
                latest_agreement = AgreementText.objects.filter(category=category).order_by("-version").first()
                if not UserAgreementInfo.objects.filter(user=request.user, agreement=latest_agreement).exists():
                    request.session["agreement_id"] = latest_agreement.id
                    request.session["next"] = request.path
                    return redirect(reverse("accept_agreement"))
