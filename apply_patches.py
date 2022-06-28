import os

from models.db_patch import DBPatch
from services.configurator import configurator
from services.database import db

PATCHES_DIR = os.path.join(configurator.BASE_DIR, 'db_patches')


last_patch = db.session.query(DBPatch).order_by(DBPatch.id.desc()).first()

patch_name = (f'{last_patch.date}v{last_patch.version}'
              if last_patch.version else str(last_patch.date)) + '.sql'
patch_name = patch_name.replace('-', '_')

files = sorted(os.listdir(PATCHES_DIR))
files = [f for f in files if f > patch_name]

for f in files:
    with open(os.path.join(PATCHES_DIR, f)) as patch:
        db.session.execute(patch.read())
        db.session.commit()

