# Django-vote-system
A django application to vote any model

### Install
`pip install django-vote-system==0.0.1`

### Configuration

**/settings**

```python
INSTALLED_APPS += [
  django_vote_system
]
```

**/urls.py**
```python
urlpatterns += [
    path("vote/", include("django_vote_system.urls")),
]
```

### Usage

```
POST: vote/<app_label>/<model>/<id>/
  data:
    status=true|false
  result:
    status=true|false,
    upvote_count=int,
    downvote_count=int,
  
 GET: vote/<app_label>/<model>/<id>/
    "get votes with rest api"
  
  GET: is_vote/<username>/<app_label>/<model>/<id>/
    "to get is vote any user -> staus: true | false
```

### Templatetags
```
{% load vote%}

{{ model|upvote_count:"id" }}
{{ model|downvote_count:"id" }}
{% is_vote user model id %} result; True | False
```
