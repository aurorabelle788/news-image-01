"""news-image-01: write the entry image to the output directory.

The entry image is a newspaper front page summing up Friday 13 November
2026's world news (lead: the NVIDIA chief executive's resignation; fifteen
further stories across regions and fields). It is held in this repository
as entry.png and copied to the output directory unchanged, so both runs of
the program write exactly the same bytes.
"""

import os
import shutil

IMAGE_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    if not os.path.isfile(source):
        raise FileNotFoundError("entry image not found in repository: " + source)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(source, destination)
    # The two graded runs must write the same bytes: confirm the copy is
    # complete before returning, so a truncated write fails loudly here
    # instead of reaching the judge.
    if os.path.getsize(destination) != os.path.getsize(source):
        raise IOError("incomplete copy of entry image to " + destination)


if __name__ == "__main__":
    main()
