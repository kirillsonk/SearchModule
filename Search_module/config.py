import os
import sys
from datetime import datetime


def start_config():
    timestamp_dir = datetime.now().strftime('%Y-%m-%d-%H-%M')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = base_dir + '/data/' + timestamp_dir + '/' + 'documents'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)