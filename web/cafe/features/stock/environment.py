import os
from behaving import environment as benv
from cafe.apps import stock as app

PERSONAS = {}

def before_all(context):
    context.attachment_dir = os.path.join(os.path.dirname(app.__file__), 'tests/data')
    context.sms_path = os.path.join(os.path.dirname(app.__file__), '../../var/sms/')
    context.mail_path = os.path.join(os.path.dirname(app.__file__), '../../var/mail/')
    context.screenshots_dir = os.path.join(os.path.dirname(app.__file__), '../../var/screenshot/')
    context.base_url = "http://localhost:8000/"
    context.default_browser = "phantomjs"
    context.browser_args = {
        "service_args": ['--ignore-ssl-errors=true', '--ssl-protocol=any'],
    }
    benv.before_all(context)


def after_all(context):
    benv.after_all(context)


def before_feature(context, feature):
    benv.before_feature(context, feature)


def after_feature(context, feature):
    benv.after_feature(context, feature)


def before_scenario(context, scenario):
    benv.before_scenario(context, scenario)
    context.personas = PERSONAS

def after_scenario(context, scenario):
    benv.after_scenario(context, scenario)