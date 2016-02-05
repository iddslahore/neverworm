heroku buildpacks:clear
heroku buildpacks:set https://github.com/heroku/heroku-buildpack-python
#heroku buildpacks:add https://github.com/andreipetre/heroku-buildpack-django-migrate
heroku buildpacks:add https://github.com/CBien/heroku-buildpack-gettext --index 1
