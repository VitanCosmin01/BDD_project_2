from behave import *


# Scenariu 1
@given("I am on the login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('I insert "{email}" email')
def step_impl(context, email):
    context.login_page.insert_email(email)


@when("I insert a password")
def step_impl(context):
    context.login_page.insert_any_password()


@when("I click the login button")
def step_impl(context):
    context.login_page.click_login_button()


@then("Main error is displayed")
def step_impl(context):
    context.login_page.main_error_is_displayed()


# Scenariu 2
@when("I insert " " email")
def step_impl(context):
    context.login_page.insert_email("")


@then("Email error is displayed")
def step_impl(context):
    context.login_page.email_error()


@then('Email error message contains "Please enter your email"')
def step_impl(context):
    context.login_page.email_error_message()
