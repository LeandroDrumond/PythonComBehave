from selenium.webdriver import Chrome, ChromeOptions

def DriverInit(context):
    browser = context.config.userdata.get('browser')
    browsers = {
        'chrome': [Chrome, ChromeOptions]
    }
    opts = browsers[browser][1]()
    opts.add_argument("user-agent=mrbean")
    opts.add_argument("--start-maximized")
    context.browser = browsers[browser][0](options = opts)
    return context.browser