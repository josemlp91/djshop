

![Djshop](resources/images/logos/logo.png)


Test shop in Django.

# What's this?

Djshop is a test shop made in Django. Do not use in production!

# Installation

Create a file settings_local.py in **/src/djshop/settings_local.py** with this structure:

````python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xxx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DOMAIN = "localhost"
ALLOWED_HOSTS = [DOMAIN]

DATABASES = {
    'default': {
        'ENGINE': '<your django db backend>',
        'NAME': '<djshop database>',
        'USER': '<djshop database user>',
        'PASSWORD': '<djshop database password>',
        'HOST': '',
        'PORT': ''
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = "Europe/Madrid"

EMAIL_USE_TLS = True
EMAIL_HOST = '<email host>'
EMAIL_PORT = <email host port>
EMAIL_HOST_USER = '<user email>'
EMAIL_HOST_PASSWORD = '<user email password>'
DEFAULT_FROM_EMAIL = '<default from email>'
````

# Legal notice

The license of this project is [BSD](LICENSE) and the logos have been created with [Mark Maker](http://emblemmatic.org/markmaker).


# Questions? Suggestions?

Don't hesitate to contact me, write me to diegojREMOVETHISromeroREMOVETHISlopez@REMOVETHISgmail.REMOVETHIScom.

(remove REMOVETHIS to see the real email address)