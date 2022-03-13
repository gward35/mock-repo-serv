# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("/Users/gretchen.ward/Repositories/services")
# Your mock repo
mock_repo = git.Repo("/Users/ggward/Projects/mock-repo-pro")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['gretchen.ward@protenus.com', 'g.g.ward90@gmail.com'])
importer.import_repository()