from behave import given, when, then
from playwright.async_api import Page, expect

@given(u'I am on the Playwright website')
def step_impl(context):
    context.page.goto("https://playwright.dev/")
    context.page.pause()


@then(u'I should see "Playwright" in the title')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see "Playwright" in the title')


@when(u'I click on "Getting Started"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on "Getting Started"')


@then(u'I should see "Getting Started" in the title')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see "Getting Started" in the title')


@then(u'the Heading should be "Installation"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the Heading should be "Installation"')