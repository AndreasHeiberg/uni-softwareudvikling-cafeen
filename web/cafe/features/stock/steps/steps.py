from behave import *
from behaving.web.steps import *
from behaving.sms.steps import *
from behaving.mail.steps import *
from behaving.personas.steps import *

@step(u'I click "{name}"')
def i_click(context, name):

    element = context.browser.find_by_xpath(
        ("//*[@id='%(name)s']|"
         "//*[@name='%(name)s']|"
         "//button[contains(string(), '%(name)s')]|"
         "//input[@type='button' and contains(string(), '%(name)s')]|"
         "//input[@type='button' and contains(@value, '%(name)s')]|"
         "//input[@type='submit' and contains(string(), '%(name)s')]|"
         "//input[@type='submit' and contains(@value, '%(name)s')]|"
         "//a[contains(string(), '%(name)s')]") % {'name': name})
    assert element, u'Element not found'
    element.first.click()

@given('I am logged in as "{role}"')
def impl(context, role):
    users = {
        'admin': ['admin', 'admin-password'],
        'board-member': ['board-member', 'board-member-password'],
        'key-carrier': ['key-carrier', 'key-carrier-password']
    }

    browser = context.browser
    browser.visit(urljoin(context.base_url, '/accounts/login'))
    browser.fill('username', users[role][0])
    browser.fill('password', users[role][1])
    element = browser.find_by_xpath("//input[@type='submit']")
    element.first.click()

@given('I fill in "{value}" for "{name}" stock')
def impl(context, role):
    # element = context.browser.find_by_xpath(
    #     ("//*[@class="product-row"]/strong[contains(string(), '%(name)s']")
    #     )
    assert True, u'Element not found'

@given('I click "{button}" for "{name}"')
def impl(context, role):
    assert True, u'Element not found'

@given('"{name}" stock should be "{value}"')
def impl(context, role):
    assert True, u'Element not found'