from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSiteMap

sitemaps = {
    "posts": PostSiteMap,
}

urlpatterns = [
    path("blog/", include("blog.urls", namespace="blog")),
    path("admin/", admin.site.urls),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
