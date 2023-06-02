from typing import List
from pathlib import Path
import os
import git
import yaml
from git import Repo

LOCALPATH = os.path.abspath("./") + f"/temp_file_location_REPOS"
BANNED_YAML = "/banned.yaml"
SPHINX_YAML = os.path.abspath("./") + "/sphinx_repositories.yaml"
LOCAL_REQUIREMENTS = os.path.abspath("./") + f"/requirements{uuid.uuid1()}.txt"

class MultRepoPuller:
    """
    A class for managing multiple Git repositories in a local folder.

    Args:
        repo_list (List[str]): A list of Git repository URLs.
        local_path (Path): The local path where the repositories will be cloned.
    """

    def __init__(self, repo_list: List[str], local_path=LOCALPATH):
        """
        Initialize the MultRepoPuller with the specified list of repository URLs and local path.

        Args:
            repo_list (List[str]): A list of Git repository URLs.
            local_path (Path): The local path where the repositories will be cloned.
        """
        self.local_path = Path(local_path)
        if os.path.exists(local_path):
            raise RepoPullException(
                f"Rerun program, {LOCALPATH} exists. Ensure that no data is being deleted"
            )
        os.makedirs(local_path)
        self.repo_list = []
        for repo_url in repo_list:
            repo_folder = os.path.join(
                local_path, self._get_repo_name_from_url(repo_url)
            )
            print(repo_folder)
            os.makedirs(repo_folder)
            self.repo_list.append(git.Repo.clone_from(repo_url, repo_folder))

    def __enter__(self):
        """
        Enter the context manager for the MultRepoPuller class.

        Returns:
            MultRepoPuller: The current instance.
        """
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        Exit the context manager for the MultRepoPuller class.

        Args:
            exc_type (Type): The type of the exception raised, if any.
            exc_value (Exception): The exception instance, if raised.
            exc_traceback (Traceback): The traceback object, if any.
        """
        pass

    def _get_repo_name_from_url(self, repo_path: str):
        """
        Extract the repository name from the given repository URL.

        Args:
            repo_path (str): The repository URL.

        Returns:
            str: The repository name.
        """
        repo_name = repo_path.split("/")[-1]
        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]
        return repo_name
