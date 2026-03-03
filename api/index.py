import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1] / 'shri_ganesh'
sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shri_ganesh.settings')

from django.core.wsgi import get_wsgi_application  # noqa: E402

app = get_wsgi_application()
