from mbed_cloud_sdk.exceptions import CloudApiException

def error_handler(exceptions = [Exception], get_message = None, exit = 1):
    def wrap(f):

        def default_get_message(data):
            return ""

        def parse_exception(e):
            return {}

        @catch_exceptions(exceptions)
        def wrapped_f(*args, **kwargs):
            try:
                fn(*args, **kwargs)
            except CloudApiException, e:
                data = parse_exception(str(e))

                # Write error to stderr
                msg_func = default_get_message if not get_message else get_message
                sys.stderr.write(msg_func(data))
                sys.stderr.flush()

                # Optionally exit
                if exit >= 0:
                    sys.exit(exit)
        return wrapped_f
    return wrap

def catch_exceptions(*exceptions):
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            try:
                fn(*args, **kwargs)
            except exceptions:
                t, value, traceback = sys.exc_info()
                raise CloudApiException, value, traceback
        return wrapped_f
    return wrap
