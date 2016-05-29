import os.path

TORCH_RNN_DIR = os.path.expanduser('~/torch-rnn') # NOTE: point this as necessary

BACHBOT_DIR = os.path.abspath(os.path.join(os.path.realpath(__file__), '..', '..'))
SCRATCH_DIR = BACHBOT_DIR + '/scratch'

START_DELIM = unichr(1111)
END_DELIM = unichr(1115)
#START_DELIM = "HELLO"
#END_DELIM = "BYE"
