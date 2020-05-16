INPUT_FILENAME = '/home/damoklov/PycharmProjects/python-logparse-iot/access_log_Jul95'
OUTPUT_FILENAME = '/home/damoklov/PycharmProjects/python-logparse-iot/parsed_logs.log'

SAMPLE_QUERY = '^[a-zA-Z0-9\-\.]+[\s\-]{5}\[01\/Jul\/1995:01:3[5-8]:[0-9]{2}\s-[0-9]{4}\]\s"[A-Z]{3,7}\s[\/\-\w\.\?\,\~]+\s?(HTTP\/1\.[01])?"\s[0-9]{3}\s[0-9\-]+$'
DOMAIN_OR_IP_REGEX = '[a-zA-Z0-9\-\.]+'
DELIMETER_REGEX = '[\s\-]{5}'
TIMESTAMP_REGEX = '01\/Jul\/1995:01:3[5-8]:[0-9]{2}\s-[0-9]{4}'
METHOD_REGEX = '[A-Z]{3,7}'
FILE_REGEX = '[ -~]+'
ERROR_REGEX = '[45][0-9]{2}'
PROTOCOL_REGEX = '(HTTP\/1\.[01])'
BYTES_REGEX = '[0-9\-]+'

FINAL_REGEX = '^{DOMAIN_OR_IP}{DELIMETER}\[{TIMESTAMP}\]\s"{METHOD}\s{FILE}\s?{PROTOCOL}?"\s{ERROR}\s{BYTES}$'.format(
    DOMAIN_OR_IP=DOMAIN_OR_IP_REGEX,
    DELIMETER=DELIMETER_REGEX,
    TIMESTAMP=TIMESTAMP_REGEX,
    METHOD=METHOD_REGEX,
    FILE=FILE_REGEX,
    PROTOCOL=PROTOCOL_REGEX,
    ERROR=ERROR_REGEX,
    BYTES=BYTES_REGEX
)